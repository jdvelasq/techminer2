"""
TopicDynamics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore 
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.emerg.topic_trend.bursts import TopicDynamics  # type: ignore
    >>> df = (
    ...     TopicDynamics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # KLEINBERG BURST:
    ...     .using_kleinberg_burst_rate(2.0)
    ...     .using_kleinberg_burst_gamma(1.0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15)  # doctest: +NORMALIZE_WHITESPACE
                                        LEVEL  START   END  DURATION   OCC
    ITEM                                                                  
    learning systems 0343:003524            2   2025  2025         0   343
    green computing 0057:000761             2   2025  2025         0    57
    controllers 0067:001148                 1   2022  2022         0    67
    the internet of things 0075:001833      1   2023  2024         1    75
    tinyml 1175:011915                      1   2024  2025         1  1175
    machine learning 0807:009343            1   2024  2025         1   807
    tiny machine learning 0480:005025       1   2024  2025         1   480
    accuracy 0413:003917                    1   2024  2025         1   413
    internet of things 0354:005877          1   2024  2025         1   354
    microcontrollers 0316:003886            1   2024  2025         1   316
    deep learning 0288:004416               1   2024  2025         1   288
    neural networks 0281:003048             1   2024  2025         1   281
    edge computing 0257:003298              1   2024  2025         1   257
    models 0209:001874                      1   2024  2025         1   209
    microcontroller 0178:001770             1   2024  2025         1   178


    >>> df = (
    ...     TopicDynamics()
    ...     #
    ...     # FIELD:
    ...     .with_analysis_unit(AnalysisUnit.CONCEPT)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # KLEINBERG BURST:
    ...     .using_kleinberg_burst_rate(2.0)
    ...     .using_kleinberg_burst_gamma(1.0)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15)  # doctest: +NORMALIZE_WHITESPACE
                            LEVEL  START   END  DURATION   OCC
    ITEM                                                      
    learning systems            2   2025  2025         0   343
    green computing             2   2025  2025         0    57
    controllers                 1   2022  2022         0    67
    the internet of things      1   2023  2024         1    75
    tinyml                      1   2024  2025         1  1175
    machine learning            1   2024  2025         1   807
    tiny machine learning       1   2024  2025         1   480
    accuracy                    1   2024  2025         1   413
    internet of things          1   2024  2025         1   354
    microcontrollers            1   2024  2025         1   316
    deep learning               1   2024  2025         1   288
    neural networks             1   2024  2025         1   281
    edge computing              1   2024  2025         1   257
    models                      1   2024  2025         1   209
    microcontroller             1   2024  2025         1   178

    
"""

from math import log

import numpy as np
import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin, remove_counters
from tm2p.portfolio.perform_metr.trend import Trends


class TopicDynamics(
    ParamsMixin,
):
    """:meta private:"""

    def kleinberg_burst_detection(self, timestamps, rate=2.0, gamma=1.0, n=None):
        timestamps = sorted(timestamps)
        if len(timestamps) < 2:
            return [], []

        T = timestamps[-1] - timestamps[0]
        if T == 0:
            return [], []

        num_events = len(timestamps)
        gaps = np.diff(timestamps).astype(float)
        # Add tiny jitter to avoid zero gaps (same-year events)
        gaps = np.where(gaps == 0, 1e-6, gaps)
        m = len(gaps)

        if n is None:
            n = max(2, int(np.ceil(1 + log(num_events, rate))))

        avg_rate = num_events / T
        rates = np.array([avg_rate * (rate**q) for q in range(n)])

        def emit_cost(gap, q):
            return rates[q] * gap - log(rates[q])

        def trans_cost(i, j):
            return max(0, (j - i) * gamma * log(n))

        INF = float("inf")
        cost = np.full((m, n), INF)
        prev = np.zeros((m, n), dtype=int)

        for q in range(n):
            cost[0, q] = emit_cost(gaps[0], q) + trans_cost(0, q)

        for t in range(1, m):
            for q in range(n):
                options = [cost[t - 1, p] + trans_cost(p, q) for p in range(n)]
                best_p = int(np.argmin(options))
                cost[t, q] = options[best_p] + emit_cost(gaps[t], q)
                prev[t, q] = best_p

        states = np.zeros(m, dtype=int)
        states[-1] = np.argmin(cost[-1])
        for t in range(m - 2, -1, -1):
            states[t] = prev[t + 1, states[t + 1]]

        bursts = []
        for level in range(1, n):
            in_burst = False
            start = None
            for t in range(m):
                if states[t] >= level and not in_burst:
                    in_burst = True
                    start = timestamps[t]
                elif states[t] < level and in_burst:
                    bursts.append((level, start, timestamps[t]))
                    in_burst = False
            if in_burst:
                bursts.append((level, start, timestamps[-1]))

        return bursts, states.tolist()

    def counts_to_timestamps(self, series: pd.Series) -> list:

        timestamps = []
        for year, count in series.items():
            if count > 0:
                # Spread events evenly across the year
                offsets = np.linspace(0, 1, int(count) + 2)[1:-1]
                year = float(year)  # type: ignore
                timestamps.extend([year + float(o) for o in offsets])
        return sorted(timestamps)

    def detect_bursts_from_df(self, df):

        scaling = self.params.kleinberg_burst_rate
        gamma = self.params.kleinberg_burst_gamma

        years = [int(c) for c in df.columns]
        df.columns = years

        results = {}
        for item in df.index:
            series = df.loc[item]
            total = series.sum()

            timestamps = self.counts_to_timestamps(series)
            bursts, _ = self.kleinberg_burst_detection(
                timestamps, rate=scaling, gamma=gamma
            )

            if bursts:
                max_level = max(b[0] for b in bursts)
                results[item] = {
                    "bursts": bursts,
                    "max_level": max_level,
                    "total": int(total),
                }

        return results

    def burst_summary_table(self, results, year_start=None, year_end=None):

        rows = []
        for item, data in results.items():
            for level, start, end in data["bursts"]:
                s_yr = int(start)
                e_yr = int(end)
                if year_start and s_yr < year_start:
                    continue
                if year_end and e_yr > year_end:
                    continue
                rows.append(
                    {
                        "item": item,
                        "level": level,
                        "start": s_yr,
                        "end": e_yr,
                        "duration": e_yr - s_yr,
                        "total_occ": data["total"],
                    }
                )

        summary = pd.DataFrame(rows)
        if not summary.empty:
            summary = summary.sort_values(["level", "start"], ascending=[False, True])
        return summary.reset_index(drop=True)

    def run(self):

        use_counters = self.params.use_counters
        self.params.use_counters = True
        df = Trends().update(**self.params.__dict__).run()
        results = self.detect_bursts_from_df(df)
        summary = self.burst_summary_table(results)

        summary = summary.rename(
            columns={
                "item": "ITEM",
                "level": "LEVEL",
                "start": "START",
                "end": "END",
                "duration": "DURATION",
                "total_occ": "OCC",
            }
        )

        summary = summary.set_index("ITEM")

        if use_counters is False:
            self.params.use_counters = False
            summary.index = summary.index.map(remove_counters)

        return summary


#

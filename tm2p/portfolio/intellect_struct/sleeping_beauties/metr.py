"""
Metrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.portfolio.intellect_struct.sleeping_beauties import Metrics  # type: ignore
    >>> df = (
    ...     Metrics()
    ...     .using_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-wos/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> assert type(df).__name__ == 'DataFrame'
    >>> assert df.shape[0] > 0
    >>> assert df.shape[1] > 0
    >>> print(df.head(10).to_string())  # doctest: +NORMALIZE_WHITESPACE
                                                  DOC  PUB_YEAR  GCS  LCS    BC  AWAKENING_YEAR  SLEEP_YEARS
    0           Khan S, 2009, ENV MODEL SOFTW 1:00084      2009   84    8  7.50            2017            8
    1            Wei SK, 2012, EUR J OPER RES 1:00105      2012  105    8  6.00            2022           10
    2         Ciplak N, 2012, WASTE MANAG RES 1:00034      2012   34    5  5.50            2018            6
    3  Nozari H, 2014, J IRRIG DRAIN ENG-ASCE 1:00019      2014   19    4  5.00            2022            8
    4  Marzouk M, 2014, RESOUR CONSERV RECYCL 1:00300      2014  300   12  3.44            2022            8
    5         Abadi LSK, 2015, KSCE J CIV ENG 1:00041      2015   41    5  3.00            2021            6
    6        Liu JK, 2020, ENV SCI POLLUT RES 1:00207      2020  207    7  3.00            2025            5
    7              Miller GR, 2012, ECOHYDROL 1:00034      2012   34    3  3.00            2017            5
    8             Ding ZK, 2018, J CLEAN PROD 1:00178      2018  178    8  2.50            2022            4
    9           Wang JY/1, 2015, J CLEAN PROD 1:00143      2015  143    6  2.00            2022            7



"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .trajectories import Trajectories  # type: ignore


class Metrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> pd.DataFrame:

        trajectory = Trajectories().update(**self.params.__dict__).run()

        records = []

        for doc_id, row in trajectory.iterrows():

            # --- parse label fields ---
            parts = doc_id.split(", ")
            pub_year = int(parts[1])
            gcs = int(parts[2].split(":")[1])

            # --- slice from publication year onward ---
            series = row.loc[pub_year:].dropna()
            series = series[series.index <= trajectory.columns.max()]

            if series.sum() == 0:
                continue

            # --- beauty coefficient ---
            counts = series.values.astype(float)
            years = series.index.to_numpy(dtype=float)

            t_max_idx = counts.argmax()
            t_max = years[t_max_idx] - years[0]
            c_max = counts[t_max_idx]

            if t_max == 0:
                bc = 0.0
            else:
                bc = sum(
                    (c_max * (years[i] - years[0]) / t_max - counts[i])
                    / max(1.0, counts[i])
                    for i in range(t_max_idx + 1)
                )

            awakening_year = int(years[t_max_idx])
            sleep_years = awakening_year - pub_year
            lcs = int(series.sum())

            records.append(
                {
                    "DOC": doc_id,
                    "PUB_YEAR": pub_year,
                    "GCS": gcs,
                    "LCS": lcs,
                    "BC": round(bc, 2),
                    "AWAKENING_YEAR": awakening_year,
                    "SLEEP_YEARS": sleep_years,
                }
            )

        result = (
            pd.DataFrame(records)
            .sort_values("BC", ascending=False)
            .reset_index(drop=True)
        )

        result = (
            pd.DataFrame(records)
            .sort_values(["BC", "SLEEP_YEARS"], ascending=[False, False])
            .reset_index(drop=True)
        )

        return result

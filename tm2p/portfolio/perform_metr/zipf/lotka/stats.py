"""
Stats
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.perform_metr.lotka import Stats  # type: ignore
    >>> df = (
    ...     Stats()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.to_string())  # doctest: +NORMALIZE_WHITESPACE
                                      VALUE
    STAT
    Total authors                 4392.0000
    Total absolute deviation         0.3506
    Mean absolute deviation          0.0159
    Maximum absolute deviation       0.1751
    Kolmogorov-Smirnov statistic     0.1751
    Chi-square goodness of fit     657.1418
    Chi-square p-value               0.0000
    Root mean square error           0.0396


"""

import pandas as pd  # type: ignore
from scipy.stats import chisquare  # type: ignore

from tm2p._intern import ParamsMixin

from .metr import Metrics


class Stats(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        metrics = Metrics().update(**self.params.__dict__).run()

        stats = {}

        stats["Total authors"] = metrics["N_AUTH_OBS"].sum()
        stats["Total absolute deviation"] = metrics["ABS_DIFF"].sum()
        stats["Mean absolute deviation"] = metrics["ABS_DIFF"].mean().round(4)
        stats["Maximum absolute deviation"] = metrics["ABS_DIFF"].max().round(4)

        metrics["CUM_PROP_AUTH_OBS"] = metrics["PROP_AUTH_OBS"].cumsum()
        metrics["CUM_PROP_AUTH_THEO"] = metrics["PROP_AUTH_THEO"].cumsum()

        stats["Kolmogorov-Smirnov statistic"] = (
            metrics["CUM_PROP_AUTH_OBS"].sub(metrics["CUM_PROP_AUTH_THEO"]).abs().max()
        )

        chi2_stat, p_value = chisquare(
            f_obs=metrics["N_AUTH_OBS"],
            f_exp=metrics["N_AUTH_THEO"]
            * metrics["N_AUTH_OBS"].sum()
            / metrics["N_AUTH_THEO"].sum(),
        )

        stats["Chi-square goodness of fit"] = chi2_stat.round(4)
        stats["Chi-square p-value"] = p_value.round(4)

        stats["Root mean square error"] = (
            (metrics["PROP_AUTH_OBS"] - metrics["PROP_AUTH_THEO"]) ** 2
        ).mean() ** 0.5

        df = pd.DataFrame(stats, index=[0]).T.reset_index()
        df.columns = ["STAT", "VALUE"]
        df["VALUE"] = df["VALUE"].round(4)
        df = df.set_index("STAT")

        return df

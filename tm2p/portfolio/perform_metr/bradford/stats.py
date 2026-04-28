"""
Stats
===============================================================================

Smoke tests:
    >>> from tm2p.portfolio.perform_metr.bradford import Stats  # type: ignore
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
    Total sources                  701
    Total records                 1481
    Core sources                    31
    Core source percentage      0.0442
    Core records                   477
    Core record percentage      0.3221
    Bradford multiplier         2.5161
    Zone ratio               31:78:592
    Mean records per source     2.1127
    Max records per source        42.0


"""

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin

from .metr import Metrics


class Stats(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        metrics = Metrics().update(**self.params.__dict__).run()

        stats = {}

        stats["Total sources"] = metrics["N_SRC"].sum()
        stats["Total records"] = metrics["N_REC"].sum()
        stats["Core sources"] = metrics[metrics["ZONE"] == 1]["N_SRC"].sum()
        stats["Core source percentage"] = (
            stats["Core sources"] / stats["Total sources"]
        ).round(4)
        stats["Core records"] = metrics[metrics["ZONE"] == 1]["N_REC"].sum()
        stats["Core record percentage"] = (
            stats["Core records"] / stats["Total records"]
        ).round(4)

        z1 = metrics.loc[metrics["ZONE"] == 1, "N_SRC"].sum()
        z2 = metrics.loc[metrics["ZONE"] == 2, "N_SRC"].sum()
        z3 = metrics.loc[metrics["ZONE"] == 3, "N_SRC"].sum()
        bradford_multiplier = z2 / z1

        stats["Bradford multiplier"] = bradford_multiplier.round(4)
        stats["Zone ratio"] = f"{z1}:{z2}:{z3}"

        stats["Mean records per source"] = (
            metrics["N_REC"].sum() / metrics["N_SRC"].sum()
        ).round(4)

        stats["Max records per source"] = (
            (metrics["N_REC"] / metrics["N_SRC"]).max().round(4)
        )

        df = pd.DataFrame(stats, index=[0]).T.reset_index()
        df.columns = ["STAT", "VALUE"]
        df = df.set_index("STAT")

        return df

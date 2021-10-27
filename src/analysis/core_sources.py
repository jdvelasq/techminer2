import numpy as np
import pandas as pd
from techminer.utils.datastore import load_datastore
from techminer.utils.explode import explode


class CoreSources:
    """
    CoreSources class.
    """

    def __init__(
        self,
        datastorepath="./",
    ):
        self._datastorepath = datastorepath
        self._datastore = load_datastore(self._datastorepath)
        self._table = None

    def _compute_core_sources(self):
        """
        Compute core sources.
        """
        # x = filter_records(pd.read_csv("corpus.csv"))
        x = self._datastore.copy()

        x["num_documents"] = 1
        x = explode(
            x[
                [
                    "publication_name",
                    "num_documents",
                    "record_id",
                ]
            ],
            "publication_name",
        )
        m = x.groupby("publication_name", as_index=True).agg(
            {
                "num_documents": np.sum,
            }
        )
        m = m[["num_documents"]]
        m = m.groupby(["num_documents"]).size()
        w = [str(round(100 * a / sum(m), 2)) + " %" for a in m]
        m = pd.DataFrame(
            {"Num Sources": m.tolist(), "%": w, "Documents published": m.index}
        )

        m = m.sort_values(["Documents published"], ascending=False)
        m["Acum Num Sources"] = m["Num Sources"].cumsum()
        m["% Acum"] = [
            str(round(100 * a / sum(m["Num Sources"]), 2)) + " %"
            for a in m["Acum Num Sources"]
        ]

        m["Tot Documents published"] = m["Num Sources"] * m["Documents published"]
        m["Num Documents"] = m["Tot Documents published"].cumsum()
        m["Tot Documents"] = m["Num Documents"].map(
            lambda w: str(round(w / m["Num Documents"].max() * 100, 2)) + " %"
        )

        bradford1 = int(len(self._datastore) / 3)
        bradford2 = 2 * bradford1

        m["Bradford's Group"] = m["Num Documents"].map(
            lambda w: 3 if w > bradford2 else (2 if w > bradford1 else 1)
        )

        m = m[
            [
                "Num Sources",
                "%",
                "Acum Num Sources",
                "% Acum",
                "Documents published",
                "Tot Documents published",
                "Num Documents",
                "Tot Documents",
                "Bradford's Group",
            ]
        ]

        m = m.reset_index(drop=True)

        self._table = m

    @property
    def table_(self):
        """
        Core sources table.

        """
        if self._table is None:
            self._compute_core_sources()
        return self._table

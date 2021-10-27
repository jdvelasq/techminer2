import numpy as np
import pandas as pd
from techminer.plots import worldmap
from techminer.utils.datastore import load_datastore
from techminer.utils.explode import explode

# from techminer.core.filter_records import filter_records


class WorldMap:
    def __init__(
        self,
        datastorepath="./",
        top_by="num_documents",
    ):
        self._datastorepath = datastorepath
        self._datastore = load_datastore(self._datastorepath)
        self._table = None
        self.column = "countries"

        if top_by == "num_documents":
            self._top_by = "num_documents"
        elif top_by == "global_citations":
            self._top_by = "global_citations"
        else:
            raise NotImplementedError

    def plot(self, colormap="Greys", figsize=(8, 6)):
        x = self._datastore.copy()
        x["num_documents"] = 1
        x = explode(
            x[
                [
                    self.column,
                    "num_documents",
                    "global_citations",
                    "record_id",
                ]
            ],
            self.column,
        )
        result = x.groupby(self.column, as_index=True).agg(
            {
                "num_documents": np.sum,
                "global_citations": np.sum,
            }
        )

        return worldmap(
            x=result[self._top_by],
            figsize=figsize,
            cmap=colormap,
        )

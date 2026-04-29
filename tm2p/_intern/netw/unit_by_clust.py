from abc import ABC, abstractmethod

import pandas as pd  # type: ignore

from tm2p._intern import ParamsMixin


class BaseUnitByCluster(
    ABC,
    ParamsMixin,
):
    """:meta private:"""

    @abstractmethod
    def cluster_to_units(self):
        pass

    def run(self):

        c2u = self.cluster_to_units().update(**self.params.__dict__).run()  # type: ignore

        df = pd.DataFrame.from_dict(c2u, orient="index").T
        df = df.fillna("")
        df = df.sort_index(axis=1)

        df.columns.name = "CLUSTER"
        df.index.name = "UNIT"

        return df

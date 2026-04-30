from abc import ABC, abstractmethod

from tm2p._intern import ParamsMixin


class BaseClusterToUnits(
    ABC,
    ParamsMixin,
):
    """:meta private:"""

    @abstractmethod
    def unit_to_cluster(self):
        pass

    def run(self):

        use_counters = self.params.use_counters

        u2c = (
            self.unit_to_cluster()
            .update(**self.params.__dict__)  # type: ignore
            .using_counters(True)
            .run()
        )

        c2u = {}
        for unit, cluster in u2c.items():
            if cluster not in c2u:
                c2u[cluster] = []
            c2u[cluster].append(unit)

        if use_counters is False:

            for cluster, units in c2u.items():
                c2u[cluster] = [" ".join(unit.split(" ")[:-1]) for unit in units]

        return c2u

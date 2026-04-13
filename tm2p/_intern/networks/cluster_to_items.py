from abc import ABC, abstractmethod

from tm2p._intern import ParamsMixin


class BaseClusterToItems(
    ABC,
    ParamsMixin,
):
    """:meta private:"""

    @abstractmethod
    def item_to_cluster(self):
        pass

    def run(self):

        use_counters = self.params.counters

        i2c = (
            self.item_to_cluster()
            .update(**self.params.__dict__)  # type: ignore
            .using_counters(True)
            .run()
        )

        c2i = {}
        for item, cluster in i2c.items():
            if cluster not in c2i:
                c2i[cluster] = []
            c2i[cluster].append(item)

        if use_counters is False:

            for cluster, items in c2i.items():
                c2i[cluster] = [" ".join(item.split(" ")[:-1]) for item in items]

        return c2i

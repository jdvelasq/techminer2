"""
ClusterToItems
===============================================================================



"""

from tm2p._intern.networks.cluster_to_items import BaseClusterToItems

from ._item_to_cluster import ItemToCluster


class ClusterToItems(
    BaseClusterToItems,
):
    """:meta private:"""

    def item_to_cluster(self):
        return ItemToCluster()

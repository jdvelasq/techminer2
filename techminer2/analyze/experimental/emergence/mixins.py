# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.analyze.metrics.emergence import DataFrame
from techminer2.analyze.networks.co_occurrence.descriptors import ClustersToTermsMapping


class RecursiveClusteringMixin:

    def internal__computer_recursive_clusters(self):

        metrics = (
            DataFrame().update(**self.params.__dict__).with_field("descriptors").run()
        )

        self.terms_with_metrics = metrics.index.tolist()

        # ------------------------------------------------------------------
        # remove the first 0 in the metrics
        #
        for _ in range(10):
            if all(t.split(" ")[1].startswith("0") for t in self.terms_with_metrics):
                self.terms_with_metrics = [
                    t.split(" ")[0] + " " + t.split(" ")[1][1:]
                    for t in self.terms_with_metrics
                ]
            else:
                break
        #
        # ------------------------------------------------------------------

        self.selected_terms = [t.split(" ")[0] for t in self.terms_with_metrics]
        discovered_clusters = [self.selected_terms]

        while True:

            new_clusters = []

            for terms in discovered_clusters:

                if len(terms) <= self.params.minimum_terms_in_cluster:

                    new_clusters.append(terms)

                else:

                    mapping = (
                        ClustersToTermsMapping()
                        .update(**self.params.__dict__)
                        #
                        # rewrite the parameters used by the recursive clustering:
                        .having_items_in_top(None)
                        .having_items_ordered_by("OCC")
                        .having_item_occurrences_between(None, None)
                        .having_item_citations_between(None, None)
                        .having_items_in(terms)
                        #
                        .using_item_counters(False)
                        #
                        .run()
                    )

                    for key in mapping.keys():
                        new_clusters.append(mapping[key])

            if len(new_clusters) == len(discovered_clusters):
                break
            else:
                discovered_clusters = new_clusters
                sys.stderr.write(f"\n  New clusters generated: {len(new_clusters)}")

        sys.stderr.write("\n")
        self.discovered_clusters = sorted(
            discovered_clusters, key=lambda x: len(x), reverse=True
        )


#        )
#

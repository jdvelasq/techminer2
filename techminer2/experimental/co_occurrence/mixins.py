# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.co_occurrence.descriptors import ClustersToTermsMapping
from techminer2.visualization import DataFrame  # type: ignore


class RecursiveClusteringMixin:

    def internal__computer_recursive_clusters(self):

        metrics = (
            DataFrame().update(**self.params.__dict__).with_field("descriptors").run()
        )

        self.terms_with_metrics = metrics.counters.tolist()
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
                        .having_terms_in_top(None)
                        .having_terms_ordered_by("OCC")
                        .having_term_occurrences_between(None, None)
                        .having_term_citations_between(None, None)
                        .having_terms_in(terms)
                        #
                        .using_term_counters(False)
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
                if len(new_clusters) >= self.params.minimum_number_of_clusters:
                    break

        sys.stderr.write("\n")
        self.discovered_clusters = sorted(
            discovered_clusters, key=lambda x: len(x), reverse=True
        )


#

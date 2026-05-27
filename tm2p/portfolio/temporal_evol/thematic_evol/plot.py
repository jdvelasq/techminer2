"""
Plot
===============================================================================

.. raw:: html

    <iframe src="../_generated/px.portfolio.temporal_evol.thematic_evol.thematic_evol_plot.html"
    height="800px" width="100%" frameBorder="0"></iframe>


Smoke test:
    >>> from tm2p.portfolio.perform_metr.main import Metrics as MainMetrics
    >>> main_metrics = (
    ...     MainMetrics()
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(main_metrics.head(10).to_string())
                                                        VALUE
    CATEGORY ITEM                                            
    GENERAL  Annual growth rate %                       21.62
             Average annual citations per document       0.26
             Average citations per document              9.53
             Average documents per source                1.54
             Average references per document            75.38
             Documents                                   1149
             Document average age                        8.25
             Number of sources                            745
             Timespan                               1991:2026
             Total cited references                     86608

    
    >>> from tm2p.enum import AssociationIndex  # type: ignore
    >>> from tm2p.enum import AnalysisUnit  # type: ignore
    >>> from tm2p.enum import GraphClusteringAlgorithm  # type: ignore
    >>> from tm2p.enum import UnitOrderBy  # type: ignore
    >>> from tm2p.portfolio.thematic_struct.co_occur.direct import ClusterToUnits  # doctest: +ELLIPSIS
    Note...
    
    >>> mapping0 = (
    ...     ClusterToUnits()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(1991, 2005)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ) 
    >>> from pprint import pprint
    >>> pprint(mapping0) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS       
    {0: ['computer simulation',
         'system dynamics',
         'decision making',
         'mathematical models',
         'water supply',
         'water management',
    ...    
    
    >>> mapping1 = (
    ...     ClusterToUnits()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(2006, 2015)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )    
    >>> pprint(mapping1) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS           
    {0: ['system dynamics',
         'system theory',
         'computer simulation',
         'simulation',
         'system dynamics model',
         'computer software',
    ...


    >>> mapping2 = (
    ...     ClusterToUnits()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_analysis_unit(AnalysisUnit.KW)
    ...     #
    ...     .having_top_n_units(100)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # CLUSTERING:
    ...     .using_clustering(GraphClusteringAlgorithm.LOUVAIN)
    ...     .using_max_recursive_clustering_depth(1)
    ...     .using_min_recursive_cluster_size(8)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/system-dynamics-scopus/")
    ...     .where_record_years_range(2016, 2025)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )            
    >>> pprint(mapping2) # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS           
    {0: ['system dynamics',
         'system theory',
         'system dynamics modeling',
         'computer software',
         'system dynamics model',
         'decision making',
         'sensitivity analysis',
    ...

    >>> from tm2p.portfolio.temporal_evol.thematic_evol import Plot  # type: ignore
    >>> fig = (
    ...     Plot()
    ...     #
    ...     .using_title_text("Thematic Evolution Map")
    ...     .using_tmap_minimum_shared_units(2)
    ...     .using_tmap_mininum_jaccard_similarity(0.15)
    ...     .using_tmap_minimum_inclusion_index(0.40)
    ...     .using_clusters_per_period(
    ...         (mapping0, mapping1, mapping2),
    ...     )
    ...     .using_tmap_period_headers(["1995-2005", "2006-2005", "2016-2025"])
    ...     .using_tmap_n_labels_per_cluster(3)
    ...     #
    ...     .run()
    ... )
    >>> assert type(fig).__name__ == 'Figure'
    >>> fig.write_html("docsrc/_generated/px.portfolio.temporal_evol.thematic_evol.thematic_evol_plot.html")



    


"""

from pydoc import text

import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import ParamsMixin
from tm2p._intern.packag_data.templates import data

from .metr import Metrics  # type: ignore


class Plot(
    ParamsMixin,
):
    """:meta private:"""

    def run(self) -> go.Figure:

        df = Metrics().update(**self.params.__dict__).run()

        data = df.copy()

        data["SOURCE"] = (
            "P"
            + data["PERIOD_FROM"].astype(str)
            + " · C"
            + data["CLUSTER_FROM"].astype(str)
        )

        data["TARGET"] = (
            "P"
            + data["PERIOD_TO"].astype(str)
            + " · C"
            + data["CLUSTER_TO"].astype(str)
        )

        for i, row in data.iterrows():

            period_from = row["PERIOD_FROM"]
            cluster_from = row["CLUSTER_FROM"]
            period_to = row["PERIOD_TO"]
            cluster_to = row["CLUSTER_TO"]

            source = self.params.tmap_clusters_per_period[period_from][cluster_from][
                : self.params.tmap_n_labels_per_cluster
            ]
            target = self.params.tmap_clusters_per_period[period_to][cluster_to][
                : self.params.tmap_n_labels_per_cluster
            ]

            source = "<br>".join(source)
            target = "<br>".join(target)

            data.at[i, "SOURCE"] = source
            data.at[i, "TARGET"] = target

        nodes = pd.Index(pd.concat([data["SOURCE"], data["TARGET"]]).drop_duplicates())

        node_id = {label: i for i, label in enumerate(nodes)}

        source = data["SOURCE"].map(node_id)
        target = data["TARGET"].map(node_id)

        value = data["N_SHARED_TERMS"]
        # alternative:
        # value = data["LINK_STRENGTH"]

        hover_text = (
            "From: "
            + data["SOURCE"]
            + "<br>To: "
            + data["TARGET"]
            + "<br>Shared terms: "
            + data["N_SHARED_TERMS"].astype(str)
            + "<br>Jaccard: "
            + data["JACCARD"].round(3).astype(str)
            + "<br>Inclusion: "
            + data["INCLUSION"].round(3).astype(str)
            + "<br>Link strength: "
            + data["LINK_STRENGTH"].round(3).astype(str)
            + "<br><br>Terms: "
            + data["SHARED_TERMS"]
        )

        fig = go.Figure(
            data=[
                go.Sankey(
                    arrangement="snap",
                    node=dict(
                        pad=18,
                        thickness=18,
                        line=dict(width=0.5),
                        label=list(nodes),
                    ),
                    link=dict(
                        source=source,
                        target=target,
                        value=value,
                        customdata=hover_text,
                        hovertemplate="%{customdata}<extra></extra>",
                    ),
                )
            ]
        )

        fig.update_layout(
            title=self.params.title_text,
            font=dict(size=12),
            # width=1100,
            # height=700,
        )

        x_range = 1.0
        n_divs = len(self.params.tmap_period_headers) - 1
        x_div = x_range / n_divs
        x_positions = [i * x_div for i in range(len(self.params.tmap_period_headers))]

        for i, (x_pos, text) in enumerate(
            zip(x_positions, self.params.tmap_period_headers)
        ):

            if i == 0:
                xanchor = "left"
            elif i == len(self.params.tmap_period_headers) - 1:
                xanchor = "right"
            else:
                xanchor = "center"

            fig.add_annotation(
                x=x_pos,
                y=1.05,
                text=text,
                showarrow=False,
                font=dict(size=14, color="black"),
                xanchor=xanchor,
            )

        return fig

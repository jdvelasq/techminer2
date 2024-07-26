# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Collaboration Metrics
===============================================================================

>>> from techminer2.metrics import collaboration_metrics_frame
>>> collaboration_metrics_frame(
...     #
...     # PARAMS:
...     field="countries",
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
               OCC  global_citations  ...  multiple_publication  mp_ratio
countries                             ...                                
United States   16              3189  ...                     8      0.50
China            8              1085  ...                     5      0.62
Germany          7              1814  ...                     3      0.43
South Korea      6              1192  ...                     2      0.33
Australia        5               783  ...                     4      0.80
<BLANKLINE>
[5 rows x 6 columns]
    
"""
from .._core.metrics.extract_top_n_terms_by_metric import extract_top_n_terms_by_metric
from .._core.read_filtered_database import read_filtered_database


def collaboration_metrics_frame(
    #
    # PARAMS:
    field,
    #
    # ITEM FILTERS:
    top_n,
    occ_range,
    gc_range,
    custom_terms,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """:meta private:"""

    #
    # Computes the number of single and multiple publications
    # and the ratio between them.
    #
    def compute_collaboration_metrics(
        #
        # PARAMS:
        field,
        custom_terms,
        #
        # DATABASE PARAMS:
        root_dir,
        database,
        year_filter,
        cited_by_filter,
        **filters,
    ):
        #
        # Read documents from the database
        records = read_filtered_database(
            #
            # DATABASE PARAMS:
            root_dir=root_dir,
            database=database,
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            sort_by=None,
            **filters,
        )

        #
        # Add a column to represent the number of occurrences of a document
        records = records.assign(OCC=1)

        #
        # Add columns to represent single and multiple publications for a document
        records["single_publication"] = records[field].map(lambda x: 1 if isinstance(x, str) and len(x.split(";")) == 1 else 0)
        records["multiple_publication"] = records[field].map(lambda x: 1 if isinstance(x, str) and len(x.split(";")) > 1 else 0)

        #
        # Split multi-topic documents into individual documents with one topic each
        exploded = records[
            [
                field,
                "OCC",
                "global_citations",
                "local_citations",
                "single_publication",
                "multiple_publication",
                "article",
            ]
        ].copy()
        exploded[field] = exploded[field].str.split(";")
        exploded = exploded.explode(field)
        exploded[field] = exploded[field].str.strip()

        #
        # Compute collaboration indicators for each topic
        metrics = exploded.groupby(field, as_index=False).agg(
            {
                "OCC": "sum",
                "global_citations": "sum",
                "local_citations": "sum",
                "single_publication": "sum",
                "multiple_publication": "sum",
            }
        )

        #
        # Compute the multiple publication ratio for each topic
        metrics["mp_ratio"] = metrics["multiple_publication"] / metrics["OCC"]
        metrics["mp_ratio"] = metrics["mp_ratio"].round(2)

        #
        # Sort the topics by number of occurrences, global citations, and local
        # citations
        metrics = metrics.sort_values(
            by=["OCC", "global_citations", "local_citations"],
            ascending=[False, False, False],
        )

        #
        # Set the index to the criterion column
        metrics = metrics.set_index(field)

        #
        #  Filter the metrics
        if custom_terms is None:
            custom_terms = extract_top_n_terms_by_metric(
                indicators=metrics,
                metric="OCC",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

        metrics = metrics[metrics.index.isin(custom_terms)]

        return metrics

    #
    # MAIN CODE:
    #
    metrics = compute_collaboration_metrics(
        #
        # PARAMS:
        field=field,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return metrics

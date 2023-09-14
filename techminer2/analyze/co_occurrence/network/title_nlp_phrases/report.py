# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Report
===============================================================================


>>> from techminer2.network.co_occurrence.title_nlp_phrases import report
>>> report(
...     #
...     # COLUMN PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     association_index="association",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_0_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_1_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_2_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_3_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_4_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_5_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_6_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_7_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_8_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_9_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_0_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_1_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_2_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_3_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_4_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_5_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_6_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_7_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_8_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_9_prompt.txt' was created.





"""
from .....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from .....nx_create_co_occurrence_report import nx_create_co_occurrences_report

FIELD = "title_nlp_phrases"


def report(
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    association_index="association",
    #
    # REPORT PARAMS:
    report_dir="co_occurrence/network/co_occurrence/" + FIELD + "/",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """
    :meta private:
    """
    # --------------------------------------------------------------------------
    # TODO: REMOVE DEPENDENCES:
    #
    #
    # NODES:
    node_size_min = 30
    node_size_max = 70
    textfont_size_min = 10
    textfont_size_max = 20
    #
    # EDGES:
    edge_width_min = 0.8
    edge_width_max = 3.0
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # --------------------------------------------------------------------------

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=FIELD,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        association_index=association_index,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        #
        # EDGES:
        edge_width_min=edge_width_min,
        edge_width_max=edge_width_max,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return nx_create_co_occurrences_report(
        #
        # REPORT PARAMS:
        nx_graph=nx_graph,
        rows_and_columns=FIELD,
        report_dir=report_dir,
        top_n=top_n,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

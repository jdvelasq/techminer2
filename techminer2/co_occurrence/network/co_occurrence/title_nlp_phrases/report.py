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


>>> from techminer2.co_occurrence.network.co_occurrence.title_nlp_phrases import report
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
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_04_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_05_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_06_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_07_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_08_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_09_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_10_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_11_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_12_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_03_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_04_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_05_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_06_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_07_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_08_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_09_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_10_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_11_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_occurrence/network/co_occurrence/title_nlp_phrases/CL_12_prompt.txt' was created.



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
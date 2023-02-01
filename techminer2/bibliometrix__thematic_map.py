"""
Thematic Map
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix__thematic_map
>>> nnet = bibliometrix__thematic_map(
...     criterion="author_keywords",
...     topics_length=20,
...     directory=directory,
...     method="louvain",
...     nx_k=0.5,
...     nx_iterations=10,
...     delta=1.0,    
... )


>>> file_name = "sphinx/_static/bibliometrix__thematic_map_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__thematic_map_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> nnet.communities_.head()
                          CL_00  ...                         CL_03
0                regtech 69:461  ...     financial services 05:135
1  regulatory technology 12:047  ...    financial inclusion 05:068
2             compliance 12:020  ...  anti-money laundering 04:030
3   financial technology 09:032  ...   financial innovation 04:007
4   financial regulation 08:091  ...                              
<BLANKLINE>
[5 rows x 4 columns]


>>> file_name = "sphinx/_static/bibliometrix__thematic_map_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__thematic_map_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                              group  betweenness  closeness  pagerank
accountability 04:022             0     0.002144   0.575758  0.028472
anti-money laundering 04:030      3     0.002437   0.575758  0.024943
big data 04:027                   1     0.006391   0.655172  0.067830
crowdfunding 04:030               1     0.014529   0.678571  0.093745
cryptocurrency 04:029             1     0.011062   0.655172  0.058653

"""
from .bibliometrix__co_occurrence_network import \
    bibliometrix__co_occurrence_network


def bibliometrix__thematic_map(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    # summarize=False,
    directory_for_results="thematic_map/",
    n_keywords=10,
    # n_abstracts=50,
    # n_phrases_per_algorithm=5,
    method="louvain",
    nx_k=0.5,
    nx_iterations=10,
    delta=1.0,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Thematic map network analysis"""

    return bibliometrix__co_occurrence_network(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        normalization="association",
        # summarize=summarize,
        directory_for_results=directory_for_results,
        n_keywords=n_keywords,
        # n_abstracts=n_abstracts,
        # n_phrases_per_algorithm=n_phrases_per_algorithm,
        method=method,
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        delta=delta,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

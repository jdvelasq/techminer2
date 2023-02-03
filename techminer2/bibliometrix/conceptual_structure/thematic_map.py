"""
Thematic Map
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.conceptual_structure.thematic_map(
...     criterion="author_keywords",
...     topics_length=60,
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
                            CL_00  ...                         CL_07
0                  regtech 28:329  ...        smart contracts 02:022
1                  fintech 12:249  ...  algorithmic standards 01:021
2               regulation 05:164  ...   document engineering 01:021
3       financial services 04:168  ...                              
4  artificial intelligence 04:023  ...                              
<BLANKLINE>
[5 rows x 8 columns]

>>> file_name = "sphinx/_static/bibliometrix__thematic_map_degree_plot.html"
>>> nnet.degree_plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__thematic_map_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.indicators_.head()
                              group  betweenness  closeness  pagerank
algorithmic standards 01:021      7          0.0   0.415325  0.018361
bahrain 01:007                    5          0.0   0.371607  0.006982
business management 01:011        1          0.0   0.377280  0.020363
business models 01:153            0          0.0   0.422425  0.017482
business policy 01:011            1          0.0   0.377280  0.020363

"""
from .co_occurrence_network import co_occurrence_network


def thematic_map(
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

    return co_occurrence_network(
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

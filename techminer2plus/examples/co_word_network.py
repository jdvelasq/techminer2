# flake8: noqa
"""
Co-word Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.examples.co_word_network(
...     field="author_keywords",
...     top_n=50,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.5, 'nx_iterations': 10},
... )
--INFO-- The file 'data/regtech/reports/co_word_network/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_04_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_03_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/co_word_network/CL_04_prompt.txt' was created.



>>> file_name = "sphinx/_static/examples/conceptual_structure/co_word_network/co_word_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/conceptual_structure/co_word_network/co_word_network.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> print(nnet.communities_.to_markdown())
|    | CL_00                          | CL_01                                      | CL_02                            | CL_03                                            | CL_04                             |
|---:|:-------------------------------|:-------------------------------------------|:---------------------------------|:-------------------------------------------------|:----------------------------------|
|  0 | REGTECH 28:329                 | REGULATORY_TECHNOLOGY 07:037               | FINTECH 12:249                   | FINANCIAL_REGULATION 04:035                      | INNOVATION 03:012                 |
|  1 | COMPLIANCE 07:030              | ANTI_MONEY_LAUNDERING 05:034               | REGULATION 05:164                | DATA_PROTECTION 02:027                           | CORONAVIRUS 01:011                |
|  2 | BLOCKCHAIN 03:005              | ARTIFICIAL_INTELLIGENCE 04:023             | FINANCIAL_SERVICES 04:168        | DIGITAL_IDENTITY 01:024                          | DIGITAL_TECHNOLOGY 01:011         |
|  3 | SMART_CONTRACTS 02:022         | CHARITYTECH 02:017                         | RISK_MANAGEMENT 03:014           | EUROPEAN_UNION 01:024                            | REGULATIONS_AND_COMPLIANCE 01:011 |
|  4 | ACCOUNTABILITY 02:014          | ENGLISH_LAW 02:017                         | SUPTECH 03:004                   | GENERAL_DATA_PROTECTION_REGULATION (GDPR) 01:024 | SMART_TREASURY 01:011             |
|  5 | DATA_PROTECTION_OFFICER 02:014 | COUNTER_TERROR_FINANCE 01:014              | SEMANTIC_TECHNOLOGIES 02:041     | OPEN_BANKING 01:024                              |                                   |
|  6 | GDPR 02:014                    | BUSINESS_MANAGEMENT 01:011                 | FINANCE 02:001                   | PAYMENT_SERVICES_DIRECTIVE_2 (PSD_2) 01:024      |                                   |
|  7 | SANDBOXES 02:012               | BUSINESS_POLICY 01:011                     | REPORTING 02:001                 |                                                  |                                   |
|  8 | TECHNOLOGY 02:010              | CORPORATE_FINANCE 01:011                   | BUSINESS_MODELS 01:153           |                                                  |                                   |
|  9 | ALGORITHMIC_STANDARDS 01:021   | INTERNATIONAL_FINANCE 01:011               | FUTURE_RESEARCH_DIRECTION 01:153 |                                                  |                                   |
| 10 | DOCUMENT_ENGINEERING 01:021    | KNOW_YOUR_CUSTOMER (KYC)_COMPLIANCE 01:011 | STANDARDS 01:033                 |                                                  |                                   |
| 11 | CHINA 01:013                   | SUSTAINABLE_BUSINESS 01:011                |                                  |                                                  |                                   |
| 12 | FINANCIAL_DEVELOPMENT 01:013   |                                            |                                  |                                                  |                                   |
| 13 | FINANCIAL_CRIME 01:010         |                                            |                                  |                                                  |                                   |
| 14 | MONEY_LAUNDERING 01:010        |                                            |                                  |                                                  |                                   |

>>> file_name = "sphinx/_static/examples/conceptual_structure/co_word_network/degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/conceptual_structure/co_word_network/degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> nnet.network_metrics__table_.head()
                              Degree  Betweenness  ...  Centrality  Density
REGTECH 28:329                    39     0.510223  ...        28.0     77.0
FINTECH 12:249                    25     0.116439  ...        12.0     44.0
REGULATORY_TECHNOLOGY 07:037      20     0.230668  ...         7.0     23.0
COMPLIANCE 07:030                 15     0.043643  ...         7.0     25.0
REGULATION 05:164                 15     0.028463  ...         5.0     22.0
<BLANKLINE>
[5 rows x 6 columns]



# pylint: disable=line-too-long
"""

from ..analyze.matrix import co_occurrence_matrix
from ..analyze.network import (
    cluster_network,
    matrix_normalization,
    network_communities,
    network_degree_plot,
    network_metrics,
    network_report,
    network_viewer,
)
from ..classes import CoWordsNetwork


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def co_word_network(
    #
    # 'co_word_matrix' params:
    field,
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # 'cluster_field' params:
    normalization="association",
    algorithm_or_estimator="louvain",
    #
    # report:
    report_dir="co_word_network/",
    concordances_top_n=10,
    #
    # Results params:
    network_viewer_dict=None,
    network_degree_plot_dict=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Co-occurrence network."""

    if network_degree_plot_dict is None:
        network_degree_plot_dict = {}

    if network_viewer_dict is None:
        network_viewer_dict = {}

    coc_matrix = co_occurrence_matrix(
        columns=field,
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    norm_coc_matrix = matrix_normalization(
        coc_matrix, index_name=normalization
    )

    graph = cluster_network(
        norm_coc_matrix, algorithm_or_estimator=algorithm_or_estimator
    )

    degree_plot = network_degree_plot(graph=graph, **network_degree_plot_dict)

    metrics = network_metrics(graph=graph)

    network_report(
        graph=graph,
        field=field,
        report_dir=report_dir,
        #
        # Concordances
        top_n=concordances_top_n,
        #
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    network = CoWordsNetwork()
    network.plot_ = network_viewer(graph=graph, **network_viewer_dict)
    network.graph_ = graph
    network.communities_ = network_communities(graph=graph)

    network.network_metrics__table_ = metrics.table_
    network.network_metrics__prompt_ = metrics.prompt_

    network.degree_plot__plot_ = degree_plot.plot_
    network.degree_plot__table_ = degree_plot.table_
    network.degree_plot__prompt_ = degree_plot.prompt_

    return network

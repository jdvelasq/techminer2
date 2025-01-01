# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Clusters to Terms Map
===============================================================================

>>> import pprint
>>> from sklearn.cluster import KMeans
>>> from techminer2.analyze.document_clustering import ClustersToTermsMapping
>>> mapping = (
...     ClustersToTermsMapping()
...     .set_analysis_params(
...         sklearn_estimator=KMeans(
...             n_clusters=4,
...             init="k-means++",
...             n_init=10,
...             max_iter=300,
...             tol=0.0001,
...             algorithm="lloyd",
...             random_state=0,
...         ),
...     #
...     .set_output_params(
...         retain_counters=True,
...     #
...     ).set_item_params(
...         field='descriptors',
...         top_n=50,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... )
>>> pprint.pprint(mapping)
{0: ['INNOVATION 08:0990',
     'FINANCIAL_SERVICES_INDUSTRY 06:1370',
     'BUSINESS_MODELS 04:1441',
     'INFORMATION_SYSTEMS 04:0830',
     'BLOCKCHAIN 03:0881',
     'FINTECH_REVOLUTION 03:0731',
     'BANKING 03:0370',
     'STUDY_AIMS 03:0283',
     'ACADEMIC_RESEARCH 02:0691',
     'CURRENT_STATE 02:0691'],
 1: ['FINANCIAL_SERVICE 04:1036',
     'NEW_TECHNOLOGIES 02:0773',
     'COPYRIGHT_TAYLOR 02:0696',
     'FINANCIAL_SERVICES_INDUSTRIES 02:0696'],
 2: ['DISRUPTIVE_INNOVATION 02:0759'],
 3: ['FINTECH 32:5393',
     'FINANCIAL_TECHNOLOGY 18:2519',
     'FINANCIAL_SERVICES 12:1929',
     'FINANCE 11:1950',
     'FINANCIAL_INDUSTRY 09:2006',
     'FINTECH_STARTUPS 08:1913',
     'FINANCIAL_SECTOR 07:1562',
     'INFORMATION_TECHNOLOGY 07:1383',
     'FRANCIS_GROUP 05:1227',
     'FINTECH_COMPANIES 05:1072',
     'FINANCIAL_INNOVATION 05:0401',
     'FINANCIAL_INSTITUTIONS 04:0722',
     'FINANCIAL_SYSTEM 04:0688',
     'ARTIFICIAL_INTELLIGENCE 04:0495',
     'FINTECH_SERVICES 04:0468',
     'BIG_DATA 04:0467',
     'SUSTAINABLE_DEVELOPMENT 04:0306',
     'COMMERCE 03:0846',
     'FINANCIAL_MARKETS 03:0835',
     'DIGITAL_TECHNOLOGIES 03:0631',
     'FINANCIAL_INCLUSION 03:0590',
     'PRACTICAL_IMPLICATIONS 03:0531',
     'FINANCIAL_INSTITUTION 03:0488',
     'SURVEYS 03:0484',
     'ELSEVIER_LTD 03:0474',
     'FINANCIAL_REGULATION 03:0461',
     'TECHNOLOGY_ACCEPTANCE_MODEL 03:0405',
     'MARKET_PARTICIPANTS 03:0350',
     'FINANCIAL_STABILITY 03:0342',
     'CROWDFUNDING 03:0335',
     'MARKETPLACE_LENDING 03:0317',
     'ELECTRONIC_MONEY 03:0305',
     'FINTECH_MARKET 03:0297',
     'MOBILE_PAYMENT 03:0284',
     'SUSTAINABILITY 03:0227']}


"""
from typing import Dict, List

from .term_occurrence_by_cluster import term_occurrence_by_cluster


def clusters_to_terms_mapping(
    #
    # TF PARAMS:
    field,
    retain_counters=True,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    # FILTER PARAMS:
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # ESIIMATOR:
    sklearn_estimator=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    sort_by=None,
    **filters,
):
    """:meta private:"""

    contingency_table = term_occurrence_by_cluster(
        #
        # TF PARAMS:
        field=field,
        retain_counters=retain_counters,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # FILTER PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # ESIIMATOR:
        sklearn_estimator=sklearn_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        sort_by=sort_by,
        **filters,
    )

    themes = contingency_table.idxmax(axis=1)

    mapping: Dict[int, List[str]] = {}
    for word, theme in zip(themes.index, themes):
        if theme not in mapping:
            mapping[theme] = []
        mapping[theme].append(word)

    return mapping

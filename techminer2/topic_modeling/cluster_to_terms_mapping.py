# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cluster to Terms Mapping
===============================================================================


## >>> from techminer2.topic_modeling import cluster_to_terms_mapping
## >>> from sklearn.decomposition import LatentDirichletAllocation
## >>> mapping = cluster_to_terms_mapping(
## ...     field="author_keywords",
## ...     #
## ...     # TF PARAMS:
## ...     is_binary=True,
## ...     cooc_within=2,
## ...     #
## ...     # TF-IDF PARAMS:
## ...     norm=None,
## ...     use_idf=False,
## ...     smooth_idf=False,
## ...     sublinear_tf=False,
## ...     #
## ...     # TOP TERMS:
## ...     n_top_terms=5,
## ...     #
## ...     # ITEM FILTERS:
## ...     top_n=None,
## ...     occ_range=(None, None),
## ...     gc_range=(None, None),
## ...     custom_terms=None,
## ...     #
## ...     # ESTIMATOR:
## ...     sklearn_estimator=LatentDirichletAllocation(
## ...         n_components=10,
## ...         learning_decay=0.7,
## ...         learning_offset=50.0,
## ...         max_iter=10,
## ...         batch_size=128,
## ...         evaluate_every=-1,
## ...         perp_tol=0.1,
## ...         mean_change_tol=0.001,
## ...         max_doc_update_iter=100,
## ...         random_state=0,
## ...     ),
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> import pprint
## >>> pprint.pprint(mapping)
{0: ['FINTECH 31:5168',
     'FINANCIAL_SERVICES 04:0667',
     'FINANCIAL_TECHNOLOGY 03:0461',
     'INNOVATION 07:0911',
     'SERVICE_INNOVATION_STRATEGY 01:0079'],
 1: ['FINTECH 31:5168',
     'MARKETPLACE_LENDING 03:0317',
     'TECHNOLOGY 02:0310',
     'P2P_LENDING 02:0161',
     'BANKS 01:0084'],
 2: ['FINTECH 31:5168',
     'REGTECH 02:0266',
     'CYBER_SECURITY 02:0342',
     'PAYMENTS 01:0064',
     'BLOCKCHAINS 01:0064'],
 3: ['FINTECH 31:5168',
     'INNOVATION 07:0911',
     'CONTENT_ANALYSIS 02:0181',
     'POPULAR_PRESS 02:0181',
     'DIGITALIZATION 02:0181'],
 4: ['FINTECH 31:5168',
     'INNOVATION 07:0911',
     'INNOVATION_IN_FINANCIAL_SERVICES 01:0067',
     'COMPETITION 01:0067',
     'MOBILE_PAYMENT 02:0184'],
 5: ['MOBILE_PAYMENT_SERVICE 01:0125',
     'ELABORATION_LIKELIHOOD_MODEL 01:0125',
     'K_PAY 01:0125',
     'FINTECH 31:5168',
     'INNOVATION 07:0911'],
 6: ['FINTECH 31:5168',
     'FINANCIAL_INCLUSION 03:0590',
     'GOVERNMENTALITY 01:0314',
     'FINANCIALISATION 01:0314',
     'DIGITAL_TECHNOLOGIES 01:0314'],
 7: ['ARTIFICIAL_INTELLIGENCE 02:0327',
     'FINANCE 02:0309',
     'ROBOTS 02:0289',
     'TECHNOLOGY_ADOPTION 01:0225',
     'ROBO_ADVISORS 01:0225'],
 8: ['FINTECH 31:5168',
     'CROWDFUNDING 03:0335',
     'FINANCIAL_TECHNOLOGY 03:0461',
     'SUSTAINABLE_DEVELOPMENT 01:0071',
     'PEER_TO_PEER 01:0071'],
 9: ['FINTECH 31:5168',
     'INNOVATION 07:0911',
     'FINANCIAL_INCLUSION 03:0590',
     'MOBILE_PAYMENT 02:0184',
     'CASE_STUDY 02:0340']}



"""
from .components_by_term_frame import components_by_term_frame


def cluster_to_terms_mapping(
    field,
    #
    # TF PARAMS:
    is_binary: bool = True,
    cooc_within: int = 1,
    #
    # TF-IDF parameters:
    norm=None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
    #
    # TOP TERMS:
    n_top_terms=5,
    #
    # TERM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # ESTIMATOR:
    sklearn_estimator=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    theme_term_matrix = components_by_term_frame(
        field=field,
        #
        # TF PARAMS:
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # TOP TERMS:
        n_top_terms=n_top_terms,
        #
        # TERM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # ESTIMATOR:
        sklearn_estimator=sklearn_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    mapping = {}
    for i_row in range(theme_term_matrix.shape[0]):
        sorting_indices = theme_term_matrix.iloc[i_row, :].sort_values(ascending=False)
        theme_term_matrix = theme_term_matrix[sorting_indices.index]
        if n_top_terms is not None:
            mapping[i_row] = list(theme_term_matrix.columns[:n_top_terms])
        else:
            mapping[i_row] = list(theme_term_matrix.columns)

    return mapping

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Embedding
===============================================================================


>>> from techminer2.co_occurrence.factor.pca.co_occurrence_matrix.abstract_nlp_phrases import embedding
>>> embedding(
...     #
...     # PARAMS:
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # PCA PARAMS:
...     n_components=5,
...     whiten=False,
...     svd_solver="auto",
...     tol=0.0,
...     iterated_power="auto",
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0, 
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                                    DIM_0     DIM_1  ...     DIM_3     DIM_4
abstract_nlp_phrases                                 ...                    
REGULATORY_TECHNOLOGY 17:266    14.285131 -5.374639  ... -0.595423 -0.408645
FINANCIAL_INSTITUTIONS 15:194    9.061725  8.966662  ...  1.973129  1.080564
REGULATORY_COMPLIANCE 07:198     1.209422  0.152867  ...  3.555010  2.218155
FINANCIAL_SECTOR 07:169          1.678049 -2.410716  ... -2.574378  1.497101
ARTIFICIAL_INTELLIGENCE 07:033   0.257331  1.126518  ... -3.639499  4.836677
<BLANKLINE>
[5 rows x 5 columns]





"""
from ......factor_analysis import FactorAnalyzer

UNIT_OF_ANALYSIS = "abstract_nlp_phrases"


def embedding(
    #
    # PARAMS:
    association_index=None,
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # PCA PARAMS:
    n_components=None,
    whiten=False,
    svd_solver="auto",
    tol=0.0,
    iterated_power="auto",
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
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

    analyzer = FactorAnalyzer(field=UNIT_OF_ANALYSIS)

    analyzer.cooc_matrix(
        #
        # COOC PARAMS:
        association_index=association_index,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    analyzer.pca(
        #
        # PCA PARAMS:
        n_components=n_components,
        whiten=whiten,
        svd_solver=svd_solver,
        tol=tol,
        iterated_power=iterated_power,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
    )

    analyzer.compute_embedding()

    return analyzer.embedding()

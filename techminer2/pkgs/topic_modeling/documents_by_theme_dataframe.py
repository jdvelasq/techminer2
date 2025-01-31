# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Documents by Theme Frame
===============================================================================


## >>> from techminer2.analyze.topic_modeling import documents_by_theme_frame
## >>> from sklearn.decomposition import LatentDirichletAllocation
## >>> (
## ...     DocumentsByThemeDataFrame(
## ...         sklearn_estimator=LatentDirichletAllocation(
## ...             n_components=10,
## ...             learning_decay=0.7,
## ...             learning_offset=50.0,
## ...             max_iter=10,
## ...             batch_size=128,
## ...             evaluate_every=-1,
## ...             perp_tol=0.1,
## ...             mean_change_tol=0.001,
## ...             max_doc_update_iter=100,
## ...             random_state=0,
## ...         ),
## ...         n_top_terms=5,
## ...     .set_item_params(
## ...         field="author_keywords",
## ...         top_n=None,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     ).set_tf_params(
## ...         is_binary=True,
## ...         cooc_within=2,
## ...     #
## ...     ).set_tfidf_params(
## ...         norm=None,
## ...         use_idf=False,
## ...         smooth_idf=False,
## ...         sublinear_tf=False,
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ...     #
## ...     ).build()
## ... ).head()
cluster                                                0  ...         9
article                                                   ...          
Anagnostopoulos I., 2018, J ECON BUS, V100, P7  0.871422  ...  0.014286
Anshari M., 2019, ENERGY PROCEDIA, V156, P234   0.014286  ...  0.014286
Buchak G., 2018, J FINANC ECON, V130, P453      0.014287  ...  0.014287
Cai C.W., 2018, ACCOUNT FINANC, V58, P965       0.020003  ...  0.020001
Chen L., 2016, CHINA ECON J, V9, P225           0.025005  ...  0.774979
<BLANKLINE>
[5 rows x 10 columns]


"""
import pandas as pd  # type: ignore

from ...analyze.metrics import tfidf_frame


def documents_by_theme_frame(
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

    tf_matrix = tfidf_frame(
        #
        # TF PARAMS:
        field=field,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    sklearn_estimator.fit(tf_matrix)

    frame = pd.DataFrame(
        sklearn_estimator.transform(tf_matrix),
        index=tf_matrix.index,
        columns=range(sklearn_estimator.n_components),
    )
    frame.columns.name = "cluster"
    frame.index.name = "article"

    return frame

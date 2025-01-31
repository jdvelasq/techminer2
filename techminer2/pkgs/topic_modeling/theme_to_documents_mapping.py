# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Theme to Documents Mapping
===============================================================================


## >>> from techminer2.analyze.topic_modeling import theme_to_documents_mapping
## >>> from sklearn.decomposition import LatentDirichletAllocation
## >>> mapping = (
## ...     ThemeToDocumentsMapping()
## ...     .set_analysis_params(
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
## ...     .set_item_params(
## ...         field="author_keywords",
## ...         top_n=None,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> import pprint
## >>> pprint.pprint(mapping)
{0: ['Anagnostopoulos I., 2018, J ECON BUS, V100, P7',
     'Du W.D., 2019, J STRATEGIC INFORM SYST, V28, P50',
     'Gai K., 2017, LECT NOTES COMPUT SCI, V10135 LNCS, P236',
     'Gimpel H., 2018, ELECTRON MARK, V28, P245',
     'Haddad C., 2019, SMALL BUS ECON, V53, P81',
     'Jakšič M., 2019, RISK MANAGE, V21, P1',
     'Kang J., 2018, HUMCENTRIC COMPUT INF SCI, V8',
     'Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69',
     'Saksonova S., 2017, EUR RES STUD, V20, P961',
     'Schueffel P., 2016, J INNOV MANAG, V4, P32',
     'Zhao Q., 2019, SUSTAINABILITY, V11'],
 1: ['Jagtiani J., 2018, J ECON BUS, V100, P1',
     'Jagtiani J., 2018, J ECON BUS, V100, P43',
     'Li Y./2, 2017, FINANCIAL INNOV, V3',
     'Stewart H., 2018, INF COMPUT SECURITY, V26, P109'],
 2: ['Das S.R., 2019, FINANC MANAGE, V48, P981',
     'Gai K., 2018, J NETWORK COMPUT APPL, V103, P262',
     'Hu Z., 2019, SYMMETRY, V11',
     'Romanova I., 2016, CONTEMP STUD ECON FINANC ANAL, V98, P21'],
 3: ['Cai C.W., 2018, ACCOUNT FINANC, V58, P965',
     'Lee I., 2018, BUS HORIZ, V61, P35',
     'Shim Y., 2016, TELECOMMUN POLICY, V40, P168',
     'Zavolokina L., 2016, FINANCIAL INNOV, V2',
     'Zavolokina L., 2016, INT CONF INF SYST ICIS'],
 5: ['Kim Y., 2016, INT J APPL ENG RES, V11, P1058'],
 6: ['Gabor D., 2017, NEW POLIT ECON, V22, P423',
     'Ryu H.-S., 2018, IND MANAGE DATA SYS, V118, P541'],
 7: ['Gracia D.B., 2019, IND MANAGE DATA SYS, V119, P1411'],
 8: ['Anshari M., 2019, ENERGY PROCEDIA, V156, P234',
     'Buchak G., 2018, J FINANC ECON, V130, P453',
     'Deng X., 2019, SUSTAINABILITY, V11',
     'Dorfleitner G., 2017, FINTECH IN GER, P1',
     'Gomber P., 2017, J BUS ECON, V87, P537'],
 9: ['Chen L., 2016, CHINA ECON J, V9, P225',
     'Iman N., 2018, ELECT COMMER RES APPL, V30, P72',
     'Jagtiani J., 2019, FINANC MANAGE, V48, P1009',
     'Leong C., 2017, INT J INF MANAGE, V37, P92',
     'Wonglimpiyarat J., 2017, FORESIGHT, V19, P590']}

"""
from .documents_by_theme_dataframe import documents_by_theme_frame


def theme_to_documents_mapping(
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

    frame = documents_by_theme_frame(
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

    assigned_topics_to_documents = frame.idxmax(axis=1)

    mapping = {}
    for article, theme in zip(
        assigned_topics_to_documents.index, assigned_topics_to_documents
    ):
        if theme not in mapping:
            mapping[theme] = []
        mapping[theme].append(article)

    return mapping

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Theme to Documents Mapping
===============================================================================

>>> from sklearn.decomposition import LatentDirichletAllocation
>>> lda = LatentDirichletAllocation(
...     n_components=10,
...     learning_decay=0.7,
...     learning_offset=50.0,
...     max_iter=10,
...     batch_size=128,
...     evaluate_every=-1,
...     perp_tol=0.1,
...     mean_change_tol=0.001,
...     max_doc_update_iter=100,
...     random_state=0,
... )
>>> from techminer2.pkgs.topic_modeling.user import ThemeToDocumentsMapping
>>> mapping = (
...     ThemeToDocumentsMapping()
...     #
...     # FIELD:
...     .with_field("descriptors")
...     .having_terms_in_top(50)
...     .having_terms_ordered_by("OCC")
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     # DECOMPOSITION:
...     .using_decomposition_algorithm(lda)
...     .using_top_terms_by_theme(5)
...     #
...     # TFIDF:
...     .using_binary_term_frequencies(False)
...     .using_row_normalization(None)
...     .using_idf_reweighting(False)
...     .using_idf_weights_smoothing(False)
...     .using_sublinear_tf_scaling(False)
...     #
...     #
...     # DATABASE:
...     .where_root_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_range_is(None, None)
...     .where_record_citations_range_is(None, None)
...     .where_records_match(None)
...     #
...     .run()
... )
>>> import pprint
>>> pprint.pprint(mapping)
{0: ['Anshari M., 2019, ENERGY PROCEDIA, V156, P234',
     'Chen L./1, 2016, CHINA ECON J, V9, P225',
     'Das S.R., 2019, FINANC MANAGE, V48, P981',
     'Deng X., 2019, SUSTAINABILITY, V11, FINTECH AND SUSTAINABLE DEVEL',
     'Gabor D., 2017, NEW POLIT ECON, V22, P423',
     'Gai K., 2017, LECT NOTES COMPUT SCI, V10135 LNCS, P236',
     'Gai K., 2018, J NETWORK COMPUT APPL, V103, P262',
     'Gimpel H., 2018, ELECTRON MARK, V28, P245',
     'Gracia D.B., 2019, IND MANAGE DATA SYS, V119, P1411',
     'Haddad C., 2019, SMALL BUS ECON, V53, P81',
     'Hu Z., 2019, SYMMETRY, V11',
     'Kang J., 2018, HUMCENTRIC COMPUT INF SCI, V8',
     'Leong C., 2017, INT J INF MANAGE, V37, P92',
     'Lim S.H., 2019, INT J HUMCOMPUT INTERACT, V35, P886',
     'Mackenzie A., 2015, LONDON BUS SCH REV, V26, P50',
     'Magnuson W., 2018, VANDERBILT LAW REV, V71, P1167',
     'Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69',
     'Romanova I., 2016, CONTEMP STUD ECON FINANC ANAL, V98, P21',
     'Schueffel P., 2016, J INNOV MANAG, V4, P32',
     'Shim Y., 2016, TELECOMMUN POLICY, V40, P168',
     'Stewart H., 2018, INF COMPUT SECURITY, V26, P109',
     'Zhao Q., 2019, SUSTAINABILITY, V11'],
 1: ['Brummer C., 2019, GEORGET LAW J, V107, P235',
     'Dorfleitner G., 2017, FINTECH IN GER, P1',
     'Gomber P., 2017, J BUS ECON, V87, P537'],
 2: ['Jakšič M., 2019, RISK MANAGE, V21, P1'],
 3: ['Gomber P., 2018, J MANAGE INF SYST, V35, P220',
     'Gozman D., 2018, J MANAGE INF SYST, V35, P145',
     'Wonglimpiyarat J., 2017, FORESIGHT, V19, P590'],
 4: ['Zavolokina L., 2016, FINANCIAL INNOV, V2',
     'Zavolokina L., 2016, INT CONF INF SYST ICIS'],
 5: ['Chen M.A., 2019, REV FINANC STUD, V32, P2062',
     'Du W.D., 2019, J STRATEGIC INFORM SYST, V28, P50',
     'Lee I., 2018, BUS HORIZ, V61, P35'],
 6: ['Alt R., 2018, ELECTRON MARK, V28, P235',
     'Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373',
     'Goldstein I., 2019, REV FINANC STUD, V32, P1647',
     'Li Y./1, 2017, FINANCIAL INNOV, V3'],
 7: ['Anagnostopoulos I., 2018, J ECON BUS, V100, P7',
     'Demertzis M., 2018, J  FINANC REGUL, V4, P157',
     'Ryu H.-S., 2018, IND MANAGE DATA SYS, V118, P541'],
 8: ['Jagtiani J., 2019, FINANC MANAGE, V48, P1009'],
 9: ['Buchak G., 2018, J FINANC ECON, V130, P453',
     'Cai C.W., 2018, ACCOUNT FINANC, V58, P965',
     'Hinson R., 2019, CURR OPIN ENVIRON SUSTAINABILITY, V41, P1',
     'Iman N., 2018, ELECT COMMER RES APPL, V30, P72',
     'Jagtiani J., 2018, J ECON BUS, V100, P1',
     'Jagtiani J., 2018, J ECON BUS, V100, P43',
     'Kim Y., 2016, INT J APPL ENG RES, V11, P1058',
     'Saksonova S., 2017, EUR RES STUD, V20, P961']}



"""
from ...._internals.mixins import ParamsMixin
from .documents_by_theme_data_frame import DocumentsByThemeDataFrame


class ThemeToDocumentsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        frame = DocumentsByThemeDataFrame().update(**self.params.__dict__).build()

        assigned_topics_to_documents = frame.idxmax(axis=1)

        mapping = {}
        for article, theme in zip(
            assigned_topics_to_documents.index, assigned_topics_to_documents
        ):
            if theme not in mapping:
                mapping[theme] = []
            mapping[theme].append(article)

        return mapping

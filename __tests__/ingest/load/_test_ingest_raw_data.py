# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
#
# Check imported data
"""

## >>> from techminer2.prepare.database import Query

## >>> (
## ...     Query()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build(expr="SELECT record_id, raw_abstract_nlp_phrases FROM database LIMIT 5;")
## ... )
                                           record_id                           raw_abstract_nlp_phrases
0       Kim Y., 2016, INT J APPL ENG RES, V11, P1058  ACCEPTANCE; PAYMENT_TYPE_FINTECH_SERVICES; ELA...
1        Shim Y., 2016, TELECOMMUN POLICY, V40, P168  RAPID_DEVELOPMENT; INFORMATION_AND_COMMUNICATI...
2            Chen L./1, 2016, CHINA ECON J, V9, P225  TECHNOLOGY; FINANCE; FINANCE; REAL_LIFE; FINTE...
3  Romanova I., 2016, CONTEMP STUD ECON FINANC AN...  GLOBAL_ECONOMY; INNOVATIONS; WIDE_USE; BANKING...
4          Gabor D., 2017, NEW POLIT ECON, V22, P423  PAPER_EXAMINES; FINANCIAL_INCLUSION; DEVELOPME...


## >>> (
## ...     Query()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build(expr="SELECT record_id, raw_title_nlp_phrases FROM database LIMIT 5;")
## ... )
                                           record_id                              raw_title_nlp_phrases
0       Kim Y., 2016, INT J APPL ENG RES, V11, P1058         ADOPTION; MOBILE_PAYMENT_SERVICES; FINTECH
1        Shim Y., 2016, TELECOMMUN POLICY, V40, P168       CHINA_FINTECH_INDUSTRY; ACTOR_NETWORK_THEORY
2            Chen L./1, 2016, CHINA ECON J, V9, P225                FINTECH; FINTECH_DEVELOPMENT; CHINA
3  Romanova I., 2016, CONTEMP STUD ECON FINANC AN...                      BANKING; FINTECH; OPPORTUNITY
4          Gabor D., 2017, NEW POLIT ECON, V22, P423  DIGITAL_REVOLUTION; FINANCIAL_INCLUSION; INTER...


## >>> (
## ...     Query()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build(expr="SELECT record_id, local_citations FROM database LIMIT 5;")
## ... )
                                           record_id  local_citations
0       Kim Y., 2016, INT J APPL ENG RES, V11, P1058                0
1        Shim Y., 2016, TELECOMMUN POLICY, V40, P168                0
2            Chen L./1, 2016, CHINA ECON J, V9, P225                3
3  Romanova I., 2016, CONTEMP STUD ECON FINANC AN...                0
4          Gabor D., 2017, NEW POLIT ECON, V22, P423                4


## >>> (
## ...     Query()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build(expr="SELECT record_id, global_citations FROM database LIMIT 5;")
## ... )
                                           record_id  global_citations
0       Kim Y., 2016, INT J APPL ENG RES, V11, P1058               125
1        Shim Y., 2016, TELECOMMUN POLICY, V40, P168               146
2            Chen L./1, 2016, CHINA ECON J, V9, P225                96
3  Romanova I., 2016, CONTEMP STUD ECON FINANC AN...                96
4          Gabor D., 2017, NEW POLIT ECON, V22, P423               314


## >>> (
## ...     Query()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build(expr="SELECT record_id, global_references FROM database LIMIT 5;")
## ... )
                                           record_id                                  global_references
0       Kim Y., 2016, INT J APPL ENG RES, V11, P1058  Angst C.M., 2009, MIS QUART MANAGE INF SYST, V...
1        Shim Y., 2016, TELECOMMUN POLICY, V40, P168  Cresswell K.M., 2010, BMC MED INFORMATICS DECI...
2            Chen L./1, 2016, CHINA ECON J, V9, P225           Rajan R.G., 2001, AM ECON REV, V91, P206
3  Romanova I., 2016, CONTEMP STUD ECON FINANC AN...    Tallon P.P., 2010, J MANAGE INF SYST, V26, P219
4          Gabor D., 2017, NEW POLIT ECON, V22, P423  Agrawal R., 1993, SIGMOD REC, V22, P207; Aitke...


## >>> (
## ...     Query()
## ...     .set_database_params(
## ...         root_dir="example/",
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build(expr="SELECT record_id, local_references FROM database ORDER BY local_references LIMIT 5;")
## ... )
                                           record_id                                   local_references
0                         Hu Z., 2019, SYMMETRY, V11  Alt R., 2018, ELECTRON MARK, V28, P235; Gabor ...
1            Jagtiani J., 2018, J ECON BUS, V100, P1  Anagnostopoulos I., 2018, J ECON BUS, V100, P7...
2                 Zhao Q., 2019, SUSTAINABILITY, V11  Chen L./1, 2016, CHINA ECON J, V9, P225; Gombe...
3      Anshari M., 2019, ENERGY PROCEDIA, V156, P234           Dorfleitner G., 2017, FINTECH IN GER, P1
4  Hinson R., 2019, CURR OPIN ENVIRON SUSTAINABIL...          Gabor D., 2017, NEW POLIT ECON, V22, P423


"""
# noting to code

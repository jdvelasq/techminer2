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

>>> from techminer2.prepare.database import Query
>>> (
...     Query()
...     .set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(expr="SELECT record_id, local_citations FROM database LIMIT 5;")
... )
                                          record_id  local_citations
0   Goldstein I., 2019, REV FINANC STUD, V32, P1647              0.0
1          Zavolokina L., 2016, FINANCIAL INNOV, V2              3.0
2         Haddad C., 2019, SMALL BUS ECON, V53, P81              1.0
3  Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69              2.0
4            Gomber P., 2017, J BUS ECON, V87, P537              6.0

>>> (
...     Query()
...     .set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(expr="SELECT record_id, global_citations FROM database LIMIT 5;")
... )
                                          record_id  global_citations
0   Goldstein I., 2019, REV FINANC STUD, V32, P1647               197
1          Zavolokina L., 2016, FINANCIAL INNOV, V2               106
2         Haddad C., 2019, SMALL BUS ECON, V53, P81               258
3  Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69               253
4            Gomber P., 2017, J BUS ECON, V87, P537               489


>>> (
...     Query()
...     .set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(expr="SELECT record_id, global_references FROM database LIMIT 5;")
... )
                                          record_id                                  global_references
0   Goldstein I., 2019, REV FINANC STUD, V32, P1647  Biais B., 2019, REV FINANC STUD, V32, P1662; C...
1          Zavolokina L., 2016, FINANCIAL INNOV, V2  Cukier W., 2009, INF SYST J, V19, P175; Fichma...
2         Haddad C., 2019, SMALL BUS ECON, V53, P81  Ahlers G.K.C., 2015, ENTREP THEORY PRACT, V39,...
3  Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69  Alt R., 2012, ELECTRON MARK, V22, P203; Hackli...
4            Gomber P., 2017, J BUS ECON, V87, P537  Agrawal A., 2015, J ECON MANAGE STRATEG, V24, ...

>>> (
...     Query()
...     .set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     ).build(expr="SELECT record_id, local_references FROM database LIMIT 5;")
... )
                                          record_id                                  local_references
0   Goldstein I., 2019, REV FINANC STUD, V32, P1647                                              None
1          Zavolokina L., 2016, FINANCIAL INNOV, V2                                              None
2         Haddad C., 2019, SMALL BUS ECON, V53, P81  Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69
3  Puschmann T., 2017, BUSIN INFO SYS ENG, V59, P69                                              None
4            Gomber P., 2017, J BUS ECON, V87, P537                                              None


"""

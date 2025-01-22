# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
#
# Check field operations
"""


>>> from techminer2.database.tools import Query

>>> from techminer2.database.field_operators import operations__clean_text
>>> operations__clean_text(  
...     source="raw_abstract",
...     dest="raw_abstract_copy",
...     root_dir="example",
... )
>>> query = (
...     Query()
...     .set_database_params(
...         root_dir="example/",
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     )
... )
>>> text = (
...     query
...     .set_analysis_params(
...         expr="SELECT raw_abstract_copy FROM database LIMIT 1;",
...     ).build()
...     .values[0][0]
... )
>>> import textwrap
>>> print(textwrap.fill(text, width=80))
this paper examined the acceptance of payment type fintech services of users by
utilizing the elaboration likelihood model by petty and cacioppo [1] and by
applying variables associated with the technology acceptance model . in addition
, it analyzed the causal relationship between concern for information privacy
and self efficacy by adopting them as moderating variables . results suggested
that usefulness , ease of use and credibility had an effect on intention to use
, and self efficacy was found to have an moderating effect on independent and
dependent variables . further , concern for information privacy was found to be
a factor obstructing the path to intention to use . the implications of this
study are that in the promotion of payment type fintech services , convenience
and usefulness are the most critical and influential variables in terms of usage
, while government deregulation and stronger security are called for from an
institutional aspect . research india publications .



>>> from techminer2.database.field_operators import operations__highlight_nouns_and_phrases
>>> operations__highlight_nouns_and_phrases(
...     source="raw_abstract_copy",
...     dest="raw_abstract_copy",
...     root_dir="example",
... )
-- 001 -- Highlighting tokens in 'raw_abstract_copy' field.
>>> text = (
...     query
...     .set_analysis_params(
...         expr="SELECT raw_abstract_copy FROM database LIMIT 3;",
...     ).build()
... )

>>> print(textwrap.fill(text.values[0][0], width=80))
this PAPER examined the ACCEPTANCE of PAYMENT_TYPE_FINTECH_SERVICES of USERS by
utilizing the ELABORATION_LIKELIHOOD_MODEL by petty and CACIOPPO [1] and by
applying VARIABLES associated with the TECHNOLOGY_ACCEPTANCE_MODEL . in ADDITION
, it analyzed the CAUSAL_RELATIONSHIP between CONCERN for INFORMATION_PRIVACY
and SELF_EFFICACY by adopting THEM as moderating VARIABLES . RESULTS suggested
that USEFULNESS , EASE of USE and CREDIBILITY had an EFFECT on INTENTION to USE
, and SELF_EFFICACY was found to have an MODERATING_EFFECT on
INDEPENDENT_AND_DEPENDENT_VARIABLES . further , CONCERN for INFORMATION_PRIVACY
was found to be a FACTOR obstructing the PATH to INTENTION to USE . the
IMPLICATIONS of this STUDY are that in the PROMOTION of
PAYMENT_TYPE_FINTECH_SERVICES , CONVENIENCE and USEFULNESS are the
MOST_CRITICAL_AND_INFLUENTIAL_VARIABLES in TERMS of USAGE , while
GOVERNMENT_DEREGULATION and STRONGER_SECURITY are called for from an
INSTITUTIONAL_ASPECT . RESEARCH_INDIA_PUBLICATIONS .

>>> print(textwrap.fill(text.values[1][0], width=80))
the RAPID_DEVELOPMENT of INFORMATION_AND_COMMUNICATIONS_TECHNOLOGY is
transforming the ENTIRE_INDUSTRY_LANDSCAPE , heralding a NEW_ERA of
CONVERGENCE_SERVICES . as one of the DEVELOPING_COUNTRIES in the
FINANCIAL_SECTOR , CHINA is experiencing an UNPRECEDENTED_LEVEL of CONVERGENCE
between FINANCE and TECHNOLOGY . this STUDY applies the LENS of
ACTOR_NETWORK_THEORY ( ant ) to conduct a MULTI_LEVEL_ANALYSIS of the
HISTORICAL_DEVELOPMENT of CHINA_FINANCIAL_TECHNOLOGY_(_FINTECH_)_INDUSTRY . it
attempts to elucidate the PROCESS of BUILDING and disrupting a VARIETY of
NETWORKS comprising HETEROGENEOUS_ACTORS involved in the
NEWLY_EMERGING_CONVERGENCE_INDUSTRY . this RESEARCH represents a STEPPING_STONE
in exploring the INTERACTION between FINTECH and ITS yet unfolding
SOCIAL_AND_POLITICAL_CONTEXT . it also discusses POLICY_IMPLICATIONS for
CHINA_FINTECH_INDUSTRY , focusing on the CHANGING_ROLE of the STATE in fostering
the GROWTH of NATIONAL_INDUSTRY within and outside of CHINA . 2015_ELSEVIER_LTD
.

>>> print(textwrap.fill(text.values[2][0], width=80))
the PURPOSE of TECHNOLOGY is not to make FINANCE better , but to make FINANCE
serve REAL_LIFE better . FINTECH has grown much faster in CHINA than in the
UNITED_STATES . in CHINA , this SUCCESS has come not from an
INITIAL_TECHNOLOGY_ADVANTAGE , but from INTEGRATION between FINANCE and
REAL_LIFE needs . this EXPERIENCE has IMPORTANT_IMPLICATIONS for understanding
FINANCIAL_INNOVATIONS , and for the DEVELOPMENT of INCLUSIVE_FINANCE .
2016_INFORMA_UK limited , trading as TAYLOR_&_FRANCIS_GROUP .



>>> from techminer2.database.field_operators import operations__collect_nouns_and_phrases
>>> operations__collect_nouns_and_phrases(
...     source="raw_abstract_copy",
...     dest="noun_and_phrases",
...     root_dir="example",
... )
>>> text = (
...     query
...     .set_analysis_params(
...         expr="SELECT noun_and_phrases FROM database LIMIT 1;",
...     ).build()
... ).values[0][0]
>>> print(textwrap.fill(text, width=80))



>>> from techminer2.database.field_operators import operations__delete_field
>>> operations__delete_field(  
...     field="raw_abstract_copy",
...     root_dir="example",
... )
>>> operations__delete_field(  
...     field="noun_and_phrases",
...     root_dir="example",
... )


"""

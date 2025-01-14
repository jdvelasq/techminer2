# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Local Cited References (Example)
===============================================================================

## >>> from techminer2.analyze.documents import select_documents
## >>> documents = select_documents(
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="references",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ...     sort_by="local_cited_by_highest",
## ... )
## >>> print(documents[0])
Record-No: 282
AR Gomber P., 2017, J BUS ECON, V87, P537
TI Digital Finance and FinTech: current research and future research directions
AU Gomber P.; Koch J.-A.; Siering M.
TC 489
SO Journal of Business Economics
PY 2017
DE DIGITAL_FINANCE; E_FINANCE; FINTECH; FUTURE_RESEARCH_OPPORTUNITIES;
   LITERATURE_REVIEW; STATE_OF_THE_ART
** CURRENT_RESEARCH; DIGITAL_FINANCE; FUTURE_RESEARCH_DIRECTIONS
<BLANKLINE>


"""

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=import-outside-toplevel
"""
Most Global Cited References (Example)
===============================================================================

>>> from techminer2.documents import select_documents
>>> documents = select_documents(
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="references",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
...     sort_by="global_cited_by_highest",
... )
>>> print(documents[0])
Record-No: 1
AR Landis J.R., 1977, BIOMETRICS, V33, P159
AU Landis J.R.; Koch G.G.
TC 54055
SO Biometrics
PY 1977
ID MULTIVARIATE_ANALYSIS; OBSERVER; STATISTICS
** CATEGORICAL_DATA; OBSERVER_AGREEMENT
<BLANKLINE>


"""

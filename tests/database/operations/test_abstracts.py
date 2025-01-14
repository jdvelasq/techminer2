# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
#
# Check abstrats highlight
"""
>>> import textwrap
>>> import pandas as pd
>>> from techminer2.database.operations import operations__highlight_nouns_and_phrases
>>> from techminer2.database.tools import Query

>>> from techminer2.database.operations import operations__clean_text
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





>>> operations__highlight_nouns_and_phrases(
...     source="raw_abstract_copy",
...     dest="raw_abstract_copy",
...     root_dir="example",
... )
-- 001 -- Highlighting tokens in 'raw_abstract_copy' field.
>>> text = (
...     query
...     .set_analysis_params(
...         expr="SELECT raw_abstract_copy FROM database LIMIT 50;",
...     ).build()
... )


>>> print(textwrap.fill(text.values[35][0], width=80))



"""

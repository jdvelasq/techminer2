# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from typing import Dict, List, Optional, Tuple

from .get_field_values_from_database import internal__get_field_values_from_database


def internal__ends_with(params):

    dataframe = internal__get_field_values_from_database(params)
    dataframe = dataframe[dataframe.term.str.endswith(params.term_pattern)]
    dataframe = dataframe.dropna()
    dataframe = dataframe.sort_values("term", ascending=True)
    terms = dataframe.term.tolist()

    return terms

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
from techminer2.ingest.extract._helpers.get_values_from_field import (
    internal__get_values_from_field,
)


def internal__full_match(params):

    dataframe = internal__get_values_from_field(params)

    dataframe = dataframe[
        dataframe.term.str.fullmatch(
            pat=params.pattern,
            case=params.case_sensitive,
            flags=params.regex_flags,
        )
    ]

    dataframe = dataframe.dropna()
    dataframe = dataframe.sort_values("term", ascending=True)
    terms = dataframe.term.tolist()

    return terms

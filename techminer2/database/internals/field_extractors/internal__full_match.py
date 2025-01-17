# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


from .internal__get_field_values_from_database import (
    internal__get_field_values_from_database,
)


def internal__full_match(
    pattern,
    case,
    flags,
    field,
    root_dir,
):

    dataframe = internal__get_field_values_from_database(root_dir, field)
    dataframe = dataframe[
        dataframe.term.str.fullmatch(
            pat=pattern,
            case=case,
            flags=flags,
        )
    ]
    dataframe = dataframe.dropna()
    terms = dataframe.term.tolist()

    return terms

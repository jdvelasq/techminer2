# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ..field_operators.internal__fillna import internal__fillna


def internal__preprocess_abbr_source_title(root_dir):
    """:meta private:"""

    internal__fillna(
        fill_field="abbr_source_title",
        with_field="source_title",
        root_dir=root_dir,
    )

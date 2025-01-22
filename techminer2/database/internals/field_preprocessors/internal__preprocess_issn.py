# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...field_operators.operators__transform_field import internal__transform_field


def internal__preprocess_issn(root_dir):
    """:meta private:"""

    internal__transform_field(
        source="issn",
        dest="issn",
        func=lambda x: x,
        root_dir=root_dir,
    )

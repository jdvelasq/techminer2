# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ....field_operators.transform_field_operator import internal__transform_field


def internal__preprocess_index_keywords(root_dir):
    """Run authors importer."""

    internal__transform_field(
        field="raw_index_keywords",
        other_field="index_keywords",
        function=lambda x: x,
        root_dir=root_dir,
    )

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...field_operators.operators__transform_field import internal__transform_field


def internal__preprocess_isbn(root_dir):
    """Run authors importer."""

    internal__transform_field(
        source="isbn",
        dest="isbn",
        func=lambda x: x,
        root_dir=root_dir,
    )

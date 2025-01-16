# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...field_operators.operators__process_field import internal__process_field


def internal__preprocess_eissn(root_dir):
    """Run authors importer."""

    internal__process_field(
        source="eissn",
        dest="eissn",
        func=lambda x: x,
        root_dir=root_dir,
    )

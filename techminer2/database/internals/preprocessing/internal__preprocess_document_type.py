# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...operations.operations__process_field import internal__process_field


def internal__preprocess_document_type(root_dir):
    """:meta private:"""

    internal__process_field(
        source="raw_document_type",
        dest="document_type",
        func=lambda x: x,
        root_dir=root_dir,
    )

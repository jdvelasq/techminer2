# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import sys

from ....field_operators.transform_field_operator import internal__transform_field


def internal__preprocess_document_type(root_dir):
    """:meta private:"""

    sys.stdout.write("\nINFO  Processing 'document_type' column.")
    sys.stdout.flush()

    internal__transform_field(
        field="raw_document_type",
        other_field="document_type",
        function=lambda x: x.str.capitalize(),
        root_dir=root_dir,
    )

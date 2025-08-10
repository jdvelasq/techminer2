# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


import sys


def internal__preprocess_document_type(root_dir):
    """:meta private:"""

    from techminer2.database.operators.transform import internal__transform

    sys.stderr.write("INFO  Processing 'document_type' column\n")
    sys.stderr.flush()

    internal__transform(
        field="raw_document_type",
        other_field="document_type",
        function=lambda x: x.str.capitalize(),
        root_dir=root_dir,
    )


#

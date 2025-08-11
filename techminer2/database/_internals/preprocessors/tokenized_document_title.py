# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys


def internal__preprocess_tokenized_document_title(root_dir):
    """:meta private:"""

    from techminer2.database._internals.operators.tokenize import internal__tokenize

    sys.stderr.write("INFO  Creating 'tokenized_document_title' column\n")
    sys.stderr.flush()

    internal__tokenize(
        source="raw_document_title",
        dest="tokenized_document_title",
        root_dir=root_dir,
    )


#

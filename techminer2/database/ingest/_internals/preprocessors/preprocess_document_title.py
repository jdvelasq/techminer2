# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from ....._internals.log_message import internal__log_message
from ..operators.clean_text import internal__clean_text


def internal__preprocess_document_title(root_dir):
    """:meta private:"""

    sys.stderr.write("INFO  Cleaning 'document_title' column\n")
    sys.stderr.flush()

    internal__clean_text(
        source="raw_document_title",
        dest="document_title",
        root_dir=root_dir,
    )

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ..field_operations.internal__collect_tokens import internal__collect_tokens
from ..field_operations.internal__highlight_tokens import internal__highlight_tokens


def internal__preprocess_raw_document_title_nlp_phrases(root_dir):

    internal__highlight_tokens(
        source="document_title",
        dest="document_title",
        root_dir=root_dir,
    )

    internal__collect_tokens(
        source="document_title",
        dest="raw_document_title_nlp_phrases",
        root_dir=root_dir,
    )

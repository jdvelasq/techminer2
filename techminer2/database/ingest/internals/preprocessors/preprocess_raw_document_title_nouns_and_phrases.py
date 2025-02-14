# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ..operators.collect_nouns_and_phrases import internal__collect_nouns_and_phrases
from ..operators.highlight_nouns_and_phrases import (
    internal__highlight_nouns_and_phrases,
)


def internal__preprocess_raw_document_title_nouns_and_phrases(root_dir):

    internal__highlight_nouns_and_phrases(
        source="document_title",
        dest="document_title",
        root_dir=root_dir,
    )

    internal__collect_nouns_and_phrases(
        source="document_title",
        dest="raw_document_title_nouns_and_phrases",
        root_dir=root_dir,
    )

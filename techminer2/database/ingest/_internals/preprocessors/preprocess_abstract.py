# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=import-outside-toplevel
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import sys

from ..operators.highlight_nouns_and_phrases import (
    internal__highlight_nouns_and_phrases,
)


def internal__preprocess_abstract(root_dir):

    internal__highlight_nouns_and_phrases(
        source="cleaned_abstract",
        dest="abstract",
        root_directory=root_dir,
    )

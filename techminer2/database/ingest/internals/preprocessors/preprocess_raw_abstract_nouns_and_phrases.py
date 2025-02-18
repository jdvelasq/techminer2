# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....internals.log_message import internal__log_message
from ..operators.collect_nouns_and_phrases import internal__collect_nouns_and_phrases
from ..operators.highlight_nouns_and_phrases import (
    internal__highlight_nouns_and_phrases,
)


def internal__preprocess_raw_abstract_nouns_and_phrases(root_dir):

    internal__log_message(
        msgs=[
            "Processing 'raw_abstract_nouns_and_phrases' column.",
            "Highlighting noun and phrases.",
        ],
        prompt_flag=True,
    )

    internal__highlight_nouns_and_phrases(
        source="abstract",
        dest="abstract",
        root_dir=root_dir,
    )

    internal__log_message(
        msgs="Collecting noun and phrases.",
        prompt_flag=-1,
    )

    internal__collect_nouns_and_phrases(
        source="abstract",
        dest="raw_abstract_nouns_and_phrases",
        root_dir=root_dir,
    )

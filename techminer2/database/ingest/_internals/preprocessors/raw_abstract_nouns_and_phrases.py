# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from ....._internals.log_message import internal__log_message
from ..operators.collect_nouns_and_phrases import internal__collect_nouns_and_phrases


def internal__preprocess_raw_abstract_nouns_and_phrases(root_dir):

    sys.stderr.write("INFO  Collecting raw noun and phrases from abstract\n")
    sys.stderr.flush()

    internal__collect_nouns_and_phrases(
        source="abstract",
        dest="raw_abstract_nouns_and_phrases",
        root_dir=root_dir,
    )

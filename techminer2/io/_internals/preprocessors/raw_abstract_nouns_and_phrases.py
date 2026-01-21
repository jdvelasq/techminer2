# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.io._internals.operators.collect_uppercase_words import (
    collect_uppercase_words,
)


def _preprocess_raw_abstract_nouns_and_phrases(root_dir):

    sys.stderr.write("INFO: Collecting raw noun and phrases from abstract\n")
    sys.stderr.flush()

    collect_uppercase_words(
        source="abstract",
        target="raw_abstract_nouns_and_phrases",
        root_directory=root_dir,
    )


#

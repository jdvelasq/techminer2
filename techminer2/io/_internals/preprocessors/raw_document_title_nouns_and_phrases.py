# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.io._internals.operations.extract_uppercase import extract_uppercase


def _preprocess_raw_document_title_nouns_and_phrases(root_dir):

    sys.stderr.write("INFO: Collecting raw nouns and phrases from document title\n")
    sys.stderr.flush()

    extract_uppercase(
        source="document_title",
        target="raw_document_title_nouns_and_phrases",
        root_directory=root_dir,
    )


#

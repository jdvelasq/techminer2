# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.io.operators.merge import merge_columns


def _preprocess_raw_noun_and_phrases(root_dir):

    sys.stderr.write("INFO: Creating 'raw_nouns_and_phrases' column\n")
    sys.stderr.flush()

    merge_columns(
        sources=[
            "raw_document_title_nouns_and_phrases",
            "raw_abstract_nouns_and_phrases",
        ],
        target="raw_nouns_and_phrases",
        root_directory=root_dir,
    )


#

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys


def internal__preprocess_raw_noun_and_phrases(root_dir):

    from techminer2.database.operators.merge import internal__merge

    sys.stderr.write("INFO: Creating 'raw_nouns_and_phrases' column\n")
    sys.stderr.flush()

    internal__merge(
        source=[
            "raw_document_title_nouns_and_phrases",
            "raw_abstract_nouns_and_phrases",
        ],
        dest="raw_nouns_and_phrases",
        root_dir=root_dir,
    )


#

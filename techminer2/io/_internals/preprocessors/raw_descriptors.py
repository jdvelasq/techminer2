# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.operations.merge import merge_columns


def _preprocess_raw_descriptors(root_dir):

    sys.stderr.write("INFO: Creating 'raw_descriptors' column\n")
    sys.stderr.flush()

    merge_columns(
        sources=["raw_nouns_and_phrases", "raw_keywords"],
        target="raw_descriptors",
        root_directory=root_dir,
    )


#

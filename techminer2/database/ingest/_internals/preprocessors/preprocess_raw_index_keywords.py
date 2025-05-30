# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from ..operators.clean_raw_keywords import internal__clean_raw_keywords


def internal__preprocess_raw_index_keywords(root_dir):
    """Run importer."""

    sys.stderr.write("INFO  Cleaning 'raw_index_keywords' column\n")
    sys.stderr.flush()

    internal__clean_raw_keywords(
        source="raw_index_keywords",
        dest="raw_index_keywords",
        root_dir=root_dir,
    )

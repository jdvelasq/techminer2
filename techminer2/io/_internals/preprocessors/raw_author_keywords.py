# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.io._internals.operations.clean_raw_keywords import clean_raw_keywords


def preprocess_raw_author_keywords(root_directory):
    """Run importer."""

    clean_raw_keywords(
        source="raw_author_keywords",
        target="raw_author_keywords",
        root_directory=root_directory,
    )


#

#

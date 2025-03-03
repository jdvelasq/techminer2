# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import sys

from ....._internals.log_message import internal__log_message
from ..operators.count_terms_per_record import internal__count_terms_per_record


def internal__preprocess_num_authors(root_dir):
    """Run importer."""

    sys.stderr.write("INFO  Counting authors per document\n")
    sys.stderr.flush()

    internal__count_terms_per_record(
        source="authors",
        dest="num_authors",
        root_dir=root_dir,
    )

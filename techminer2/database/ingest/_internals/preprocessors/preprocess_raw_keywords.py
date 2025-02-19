# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import sys

from ....._internals.log_message import internal__log_message
from ....field_operators.merge_fields_operator import internal__merge_fields


def internal__preprocess_raw_keywords(root_dir):

    sys.stderr.write("\nINFO  Creating 'raw_keywords' column.")
    sys.stderr.flush()

    internal__merge_fields(
        source=[
            "raw_author_keywords",
            "raw_index_keywords",
        ],
        dest="raw_keywords",
        root_dir=root_dir,
    )

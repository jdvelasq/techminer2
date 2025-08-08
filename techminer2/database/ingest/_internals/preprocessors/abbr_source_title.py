# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import sys

from ....._internals.log_message import internal__log_message
from ..operators.fillna import internal__fillna


def internal__preprocess_abbr_source_title(root_dir):
    """:meta private:"""

    sys.stderr.write("INFO  Processing 'abbr_source_title' column\n")
    sys.stderr.flush()

    internal__fillna(
        fill_field="abbr_source_title",
        with_field="source_title",
        root_dir=root_dir,
    )

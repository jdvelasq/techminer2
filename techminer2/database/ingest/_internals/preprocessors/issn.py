# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import sys

from ....._internals.log_message import internal__log_message
from ....field_operators.transform_field_operator import internal__transform_field


def internal__preprocess_issn(root_dir):
    """:meta private:"""

    sys.stderr.write("INFO  Processing 'issn' column\n")
    sys.stderr.flush()

    internal__transform_field(
        field="issn",
        other_field="issn",
        function=lambda x: x,
        root_dir=root_dir,
    )

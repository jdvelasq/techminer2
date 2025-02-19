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


def internal__preprocess_global_citations(root_dir):
    """Run importer."""

    sys.stderr.write("\nINFO  Processing 'global_citations' column.")
    sys.stderr.flush()

    internal__transform_field(
        field="global_citations",
        other_field="global_citations",
        function=lambda w: w.fillna(0).astype(int),
        root_dir=root_dir,
    )

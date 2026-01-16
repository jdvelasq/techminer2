# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys

from techminer2.scopus._internals.operators.transform import internal__transform


def _preprocess_global_citations(root_dir):
    """Run importer."""

    sys.stderr.write("INFO: Processing 'global_citations' column\n")
    sys.stderr.flush()

    internal__transform(
        field="global_citations",
        other_field="global_citations",
        function=lambda w: w.fillna(0).astype(int),
        root_dir=root_dir,
    )


#

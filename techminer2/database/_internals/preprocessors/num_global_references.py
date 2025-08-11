# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys


def internal__preprocess_num_global_references(root_dir):
    """Run importer."""

    from techminer2.database._internals.operators.count import internal__count

    sys.stderr.write("INFO  Counting global references per document\n")
    sys.stderr.flush()

    internal__count(
        source="global_references",
        dest="num_global_references",
        root_dir=root_dir,
    )


#

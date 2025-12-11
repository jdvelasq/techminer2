# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import sys


def internal__preprocess_isbn(root_dir):
    """Run authors importer."""

    from techminer2.database.operators.transform import internal__transform

    sys.stderr.write("INFO: Processing 'isbn' column\n")
    sys.stderr.flush()

    internal__transform(
        field="isbn",
        other_field="isbn",
        function=lambda x: x,
        root_dir=root_dir,
    )


#

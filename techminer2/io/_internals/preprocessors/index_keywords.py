# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from techminer2.io.operators.transform import transform_column


def _preprocess_index_keywords(root_dir):
    """Run authors importer."""

    transform_column(
        source="raw_index_keywords",
        target="index_keywords",
        function=lambda x: x,
        root_directory=root_dir,
    )


#

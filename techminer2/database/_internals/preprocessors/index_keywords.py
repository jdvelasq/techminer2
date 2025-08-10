# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__preprocess_index_keywords(root_dir):
    """Run authors importer."""

    from techminer2.database.operators.transform import internal__transform

    internal__transform(
        field="raw_index_keywords",
        other_field="index_keywords",
        function=lambda x: x,
        root_dir=root_dir,
    )


#

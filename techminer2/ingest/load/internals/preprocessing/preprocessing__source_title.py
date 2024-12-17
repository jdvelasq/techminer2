# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from .....prepare.operations.process_database_field import fields__process


def preprocessing__source_title(root_dir):
    """Run importer."""

    #
    #              DYNA (Colombia)
    # Sustainability (Switzerland)
    #              npj Clean Water
    # Automotive Engineer (London)
    #
    fields__process(
        source="raw_source_title",
        dest="source_title",
        func=lambda w: w.str.replace("-", "_", regex=False).str.replace(
            "<.*?>", "", regex=True
        ),
        root_dir=root_dir,
    )

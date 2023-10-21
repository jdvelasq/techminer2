# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...refine.fields.process_field import _process_field


def run_source_title_importer(root_dir):
    """Run importer."""

    #
    #              DYNA (Colombia)
    # Sustainability (Switzerland)
    #              npj Clean Water
    # Automotive Engineer (London)
    #
    _process_field(
        source="raw_source_title",
        dest="source_title",
        func=lambda w: w.str.replace("-", "_", regex=False).str.replace(
            "<.*?>", "", regex=True
        ),
        root_dir=root_dir,
    )

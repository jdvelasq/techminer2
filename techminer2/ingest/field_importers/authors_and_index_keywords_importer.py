# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ...refine.fields.process_field import _process_field


def run_authors_and_index_keywords_importer(root_dir):
    """Run importer."""

    for source in ["raw_author_keywords", "raw_index_keywords"]:
        #
        _process_field(
            source=source,
            dest=source,
            func=lambda x: x.str.upper()
            .str.replace("&", " AND ", regex=False)
            .str.replace(r"\s+", " ", regex=True)
            .str.replace("<.*?>", "", regex=True)
            .str.replace("-", "_", regex=False)
            .str.replace('"', "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(" ", "_", regex=False)
            .str.replace(";_", "; ", regex=False)
            .str.replace("_+", "_", regex=True)
            .str.replace("_(", " (", regex=False)
            .str.replace(")_", ") ", regex=False)
            .str.replace("_[", " [", regex=False)
            .str.replace("]_", "] ", regex=False),
            root_dir=root_dir,
        )

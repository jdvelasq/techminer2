# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import re

from ...fields.process_field import _process_field


def run_authors_and_index_keywords_importer(root_dir):
    """Run importer."""

    for source in ["raw_author_keywords", "raw_index_keywords"]:
        #
        _process_field(
            source=source,
            dest=source,
            func=lambda x: x.str.upper()
            # -----------------------------------------------------------------------------
            # remove all non-ascii characters
            .str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")
            # -----------------------------------------------------------------------------
            # remove all html tags
            .str.replace("<.*?>", "", regex=True)
            # -----------------------------------------------------------------------------
            # remove appostrophes
            .str.replace("ʿ", "'", regex=False).str.replace("’", "'", regex=False).str.replace("'", "'", regex=False)
            # -----------------------------------------------------------------------------
            .str.replace("/", "_", regex=False).str.replace("\\", "_", regex=False)
            # -----------------------------------------------------------------------------
            # remove "'": e.g., "'approach'" -> "approach"
            .str.split("; ")
            .map(
                lambda x: [z.strip() for z in x],
                na_action="ignore",
            )
            .map(
                lambda x: [z[1:-1] if z.startswith("'") and z.endswith("'") else z for z in x],
                na_action="ignore",
            )
            .str.join("; ")
            # -----------------------------------------------------------------------------
            # remove '"': e.g., '"approach"' ->'approach'
            .str.split("; ")
            .map(
                lambda x: [z.strip() for z in x],
                na_action="ignore",
            )
            .map(
                lambda x: [z[1:-1] if z.startswith('"') and z.endswith('"') else z for z in x],
                na_action="ignore",
            )
            .str.join("; ")
            # -----------------------------------------------------------------------------
            # remove "'": e.g., "'approach" -> "approach"
            .str.split("; ")
            .map(
                lambda x: [z.strip() for z in x],
                na_action="ignore",
            )
            .map(
                lambda x: [z[1:] if z.startswith("'") and "'" not in z[1:] else z for z in x],
                na_action="ignore",
            )
            .str.join("; ")
            # -----------------------------------------------------------------------------
            # remove '"': e.g., '"approach' -> 'approach'
            .str.split("; ")
            .map(
                lambda x: [z.strip() for z in x],
                na_action="ignore",
            )
            .map(
                lambda x: [z[1:] if z.startswith('"') and '"' not in z[1:] else z for z in x],
                na_action="ignore",
            )
            .str.join("; ")
            # -----------------------------------------------------------------------------
            # replace posesives: e.g., "costumer's adoption" -> "costumer adoption"
            .str.replace("'S ", " ", regex=False)
            # -----------------------------------------------------------------------------
            # replace posesives: e.g., "costumers' adoption" -> "costumers adoption"
            .str.replace("' ", " ", regex=False)
            # -----------------------------------------------------------------------------
            # remove '&': e.g., 'a&m' -> "a and m"
            .str.replace("&", " AND ", regex=False)
            # -----------------------------------------------------------------------------
            # remove 'AND', 'AN', 'A' ... terms at the beginning of the string
            .str.split("; ")
            .map(
                lambda x: [re.sub("^AND ", "", z) for z in x],
                na_action="ignore",
            )
            .map(
                lambda x: [re.sub("^AN ", "", z) for z in x],
                na_action="ignore",
            )
            .map(
                lambda x: [re.sub("^A ", "", z) for z in x],
                na_action="ignore",
            )
            .map(
                lambda x: [re.sub("^THE ", "", z) for z in x],
                na_action="ignore",
            )
            .str.join("; ")
            # -----------------------------------------------------------------------------
            # remove multiple spaces
            .str.replace(r"\s+", " ", regex=True)
            # -----------------------------------------------------------------------------
            .str.replace('"', "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.replace(":", "", regex=False)
            # -----------------------------------------------------------------------------
            .str.replace("-", "_", regex=False).str.replace(" ", "_", regex=False)
            # -----------------------------------------------------------------------------
            # Separators
            .str.replace(";_", "; ", regex=False)
            .str.replace("_+", "_", regex=True)
            .str.replace("_(", " (", regex=False)
            .str.replace(")_", ") ", regex=False)
            .str.replace("_[", " [", regex=False)
            .str.replace("]_", "] ", regex=False),
            # -----------------------------------------------------------------------------
            root_dir=root_dir,
        )

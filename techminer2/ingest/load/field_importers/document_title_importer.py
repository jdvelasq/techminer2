# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

from ....prepare.fields.process_field import _process_field


def run_document_title_importer(root_dir):
    """Run importer."""

    _process_field(
        source="raw_document_title",
        dest="document_title",
        func=lambda x: x.str.replace(r"\[.*", "", regex=True)
        # -----------------------------------------------------------------------------
        # remove all html tags
        .str.replace("<.*?>", "", regex=True)
        # -----------------------------------------------------------------------------
        .str.replace("’", "'", regex=False).str.replace(";", ".", regex=False)
        #
        .str.replace(r"(", r" ( ", regex=False)  # (
        .str.replace(r")", r" ) ", regex=False)  # )
        .str.replace(r"$", r" $ ", regex=False)  # $
        .str.replace(r"/", r" / ", regex=False)  # /
        .str.replace(r"?", r" ? ", regex=False)  # ?
        .str.replace(r"¿", r" ¿ ", regex=False)  # ?
        .str.replace(r"!", r" ! ", regex=False)  # !
        .str.replace(r"¡", r" ¡ ", regex=False)  # ¡
        .str.replace(r"=", r" = ", regex=False)  # =
        .str.replace(r'"', r' " ', regex=False)  # "
        .str.replace(r":", r" : ", regex=False)  # :
        .str.replace(r"%", r" % ", regex=False)  # %
        #
        .str.replace(r"(\w+)(,\s)", r"\1 \2", regex=True)  # ,
        .str.replace(r"(\')(,\s)", r"\1 \2", regex=True)  # ,
        .str.replace(r"(\w+)(\.\s)", r"\1 \2", regex=True)  # .
        .str.replace(r"(\w+)\.$", r"\1 .", regex=True)  # .
        #
        .str.replace(r"(\w+)'s(\b)", r"\1\2", regex=True).str.replace(
            r"(\w+)'(\s)", r"\1\2", regex=True
        )  # 's  # s
        #
        .str.replace("—", "-", regex=False).str.replace("-", " ", regex=False)
        #
        # remove all non-ascii characters
        .str.normalize("NFKD").str.encode("ascii", errors="ignore").str.decode("utf-8")
        # -----------------------------------------------------------------------------
        .str.replace(r"\s+", r" ", regex=True).str.strip(),  # multiple spaces
        root_dir=root_dir,
    )

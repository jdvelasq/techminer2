# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import contractions
import pandas as pd  # type: ignore

from .....prepare.operations.process_database_field import fields__process


def preprocessing__abstract(root_dir):
    """Run authors importer."""

    fields__process(
        source="raw_abstract",
        dest="abstract",
        func=lambda x: x.map(
            lambda w: pd.NA if w[0] == "[" and w[-1] == "]" else w, na_action="ignore"
        )
        # -----------------------------------------------------------------------------
        #
        .str.lower().map(contractions.fix, na_action="ignore")
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
        # -----------------------------------------------------------------------------
        root_dir=root_dir,
    )

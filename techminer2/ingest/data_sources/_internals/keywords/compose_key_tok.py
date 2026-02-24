from techminer2 import CorpusField

from ..operations import merge_columns


def compose_key_tok(root_directory: str) -> int:

    return merge_columns(
        sources=(
            CorpusField.AUTH_KEY_TOK,
            CorpusField.IDX_KEY_TOK,
        ),
        target=CorpusField.KEY_TOK,
        root_directory=root_directory,
    )

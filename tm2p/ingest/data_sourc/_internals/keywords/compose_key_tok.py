from tm2p import CorpusField

from ..operations import merge_columns


def compose_key_tok(root_directory: str) -> int:

    return merge_columns(
        sources=(
            CorpusField.AUTHKW_TOK,
            CorpusField.IDXKW_TOK,
        ),
        target=CorpusField.KW_TOK,
        root_directory=root_directory,
    )

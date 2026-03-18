# CODE_REVIEW: 2026-01-26

from tm2p._intern import Params

from ...step import Step


def p11_kw_prepar(params: Params) -> list[Step]:

    from .s01_authkw_idxkw import s01_authkw_idxkw
    from .s02_authkw_idxkw_tok import s02_authkw_idxkw_tok
    from .s03_correct_hyphen_word import s03_correct_hyphen_word
    from .s04_auth_idx_kw_norm import s04_auth_idx_kw_norm
    from .s05_kw_tok import s05_kw_tok
    from .s06_kw_norm import s06_kw_norm

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Normalizing AUTHKW_RAW and IDXKW_RAW",
            function=s01_authkw_idxkw,
            kwargs=common_kwargs,
        ),
        Step(
            name="Tokenizing keywords",
            function=s02_authkw_idxkw_tok,
            kwargs=common_kwargs,
        ),
        Step(
            name="Correcting hyphenated words",
            function=s03_correct_hyphen_word,
            kwargs=common_kwargs,
        ),
        Step(
            name="Normalizing AUTHKW_TOK and IDXKW_TOK",
            function=s04_auth_idx_kw_norm,
            kwargs=common_kwargs,
            count_message="{count} records normalized",
        ),
        Step(
            name="Composing KW_TOK",
            function=s05_kw_tok,
            kwargs=common_kwargs,
            count_message="{count} records composed",
        ),
        Step(
            name="Composing KW_NORM",
            function=s06_kw_norm,
            kwargs=common_kwargs,
            count_message="{count} records composed",
        ),
    ]

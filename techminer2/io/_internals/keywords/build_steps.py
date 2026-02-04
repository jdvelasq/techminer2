# CODE_REVIEW: 2026-01-26


from ...._internals import Params
from ..step import Step


def build_keyword_steps(params: Params) -> list[Step]:

    from .compose_all_key_norm import compose_all_key_norm
    from .compose_all_key_raw import compose_all_key_raw
    from .normalize_auth_key_raw import normalize_auth_key_raw
    from .normalize_idx_key_raw import normalize_idx_key_raw

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Composing 'all_key_raw'",
            function=compose_all_key_raw,
            kwargs=common_kwargs,
            count_message="{count} records composed",
        ),
        Step(
            name="Normalizing 'auth_key_raw'",
            function=normalize_auth_key_raw,
            kwargs=common_kwargs,
            count_message="{count} records normalized",
        ),
        Step(
            name="Normalizing 'idx_key_raw'",
            function=normalize_idx_key_raw,
            kwargs=common_kwargs,
            count_message="{count} records normalized",
        ),
        Step(
            name="Composing 'all_key_norm'",
            function=compose_all_key_norm,
            kwargs=common_kwargs,
            count_message="{count} records composed",
        ),
    ]

# CODE_REVIEW: 2026-01-26

from techminer2 import Field

from ...._internals import Params
from ..step import Step


def build_keyword_steps(params: Params) -> list[Step]:

    from .compose_allkey_norm import compose_allkey_norm
    from .compose_allkey_raw import compose_allkey_raw
    from .normalize_authkey_raw import normalize_authkey_raw
    from .normalize_idxkey_raw import normalize_idxkey_raw

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Composing 'allkey_raw'",
            function=compose_allkey_raw,
            kwargs=common_kwargs,
            count_message="{count} records composed",
        ),
        Step(
            name="Normalizing 'authkey_raw'",
            function=normalize_authkey_raw,
            kwargs=common_kwargs,
            count_message="{count} records normalized",
        ),
        Step(
            name="Normalizing 'idxkey_raw'",
            function=normalize_idxkey_raw,
            kwargs=common_kwargs,
            count_message="{count} records normalized",
        ),
        Step(
            name="Composing 'allkey_norm'",
            function=compose_allkey_norm,
            kwargs=common_kwargs,
            count_message="{count} records composed",
        ),
    ]

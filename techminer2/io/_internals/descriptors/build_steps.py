# CODE_REVIEW: 2026-01-26

from ...._internals import Params
from ..step import Step


def build_descriptors_steps(params: Params) -> list[Step]:

    from .compose_descriptors_raw import compose_descriptors_raw
    from .compose_noun_phrases_raw import compose_noun_phrases_raw
    from .extract_abstract_noun_phrases import extract_abstract_noun_phrases_raw
    from .extract_document_title_noun_phrases_raw import (
        extract_document_title_noun_phrases_raw,
    )
    from .update_builtin_noun_phrases import update_builtin_noun_phrases
    from .uppercase_abstract import uppercase_abstract
    from .uppercase_document_title import uppercase_document_title

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Uppercasing abstract",
            function=uppercase_abstract,
            kwargs=dict(common_kwargs),
            count_message="\n    {count} abstracts uppercased",
        ),
        Step(
            name="Uppercasing document title",
            function=uppercase_document_title,
            kwargs=dict(common_kwargs),
            count_message="\n    {count} document titles uppercased",
        ),
        Step(
            name="Extracting noun phrases raw from abstracts",
            function=extract_abstract_noun_phrases_raw,
            kwargs=dict(common_kwargs),
            count_message="{count} abstract raw noun phrases created",
        ),
        Step(
            name="Extracting raw noun phrases from document titles",
            function=extract_document_title_noun_phrases_raw,
            kwargs=dict(common_kwargs),
            count_message="{count} document title raw noun phrases created",
        ),
        Step(
            name="Composing noun phrases raw",
            function=compose_noun_phrases_raw,
            kwargs=dict(common_kwargs),
            count_message="{count} noun phrases raw composed",
        ),
        Step(
            name="Composing descriptors raw",
            function=compose_descriptors_raw,
            kwargs=dict(common_kwargs),
            count_message="{count} descriptors raw composed",
        ),
        Step(
            name="Updating builtin noun phrases",
            function=update_builtin_noun_phrases,
            kwargs=dict(common_kwargs),
            count_message="{count} new builtin noun phrases found",
        ),
    ]

# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p13_concept(params: Params) -> list[Step]:

    from .s01_concept_raw_norm import s01_concept_raw_norm

    # from .s02_word_raw_norm import s02_word_raw_norm
    from .s03_descriptor_thesaurus import s03_descriptor_thesaurus
    from .s04_builtin_noun_phrases import s04_builtin_noun_phrases

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Merging KW and NP into CONCEPT",
            function=s01_concept_raw_norm,
            kwargs=common_kwargs,
        ),
        # Step(
        #     name="Creating WORD column",
        #     function=s02_word_raw_norm,
        #     kwargs=common_kwargs,
        # ),
        Step(
            name="Creating concept thesaurus",
            function=s03_descriptor_thesaurus,
            kwargs=common_kwargs,
        ),
        Step(
            name="Updating built-in NP with concepts",
            function=s04_builtin_noun_phrases,
            kwargs=common_kwargs,
            count_message="{count} records updated",
        ),
    ]

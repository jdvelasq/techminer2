# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p12_nlp_prepar(params: Params) -> list[Step]:

    from .s01_abstr_tok import s01_abstr_tok
    from .s02_title_tok import s02_title_tok
    from .s03_np_textblob import s03_np_textblob
    from .s04_np_spacy import s04_np_spacy
    from .s05_abstract_acronyms import s05_abstract_acronyms
    from .s06_abstr_upper import s06_abstr_upper
    from .s07_title_upper import s07_title_upper
    from .s08_np_abstr_raw import s08_np_abstr_raw
    from .s09_np_title_raw import s09_np_title_raw
    from .s10_np_raw import s10_np_raw

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Tokenizing ABTR",
            function=s01_abstr_tok,
            kwargs=common_kwargs,
        ),
        Step(
            name="Tokenizing TITLE",
            function=s02_title_tok,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting TextBlob phrases",
            function=s03_np_textblob,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting spaCy phrases",
            function=s04_np_spacy,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting abstract acronyms",
            function=s05_abstract_acronyms,
            kwargs=common_kwargs,
        ),
        Step(
            name="Uppercasing ABSTR",
            function=s06_abstr_upper,
            kwargs=common_kwargs,
        ),
        Step(
            name="Uppercasing TITLE",
            function=s07_title_upper,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting ABSTR phrases",
            function=s08_np_abstr_raw,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting TITLE phrases",
            function=s09_np_title_raw,
            kwargs=common_kwargs,
        ),
        Step(
            name="Merging TITLE and ABSTR phrases",
            function=s10_np_raw,
            kwargs=common_kwargs,
        ),
    ]

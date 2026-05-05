# CODE_REVIEW: 2026-01-26


from tm2p._intern import Params

from ...step import Step


def p12_nlp_prepar(params: Params) -> list[Step]:

    from .s01_abstr_tok import s01_abstr_tok
    from .s02_title_tok import s02_title_tok
    from .s03_np_textblob import s03_np_textblob
    from .s04_np_spacy import s04_np_spacy
    from .s05_np_gensim import s05_np_gensim
    from .s06_np_yake import s06_np_yake
    from .s07_np_known import s07_np_known
    from .s08_abstract_acronyms import s08_abstract_acronyms
    from .s09_abstr_upper import s09_abstr_upper
    from .s10_title_upper import s10_title_upper
    from .s11_np_abstr_raw import s11_np_abstr_raw
    from .s12_np_title_raw import s12_np_title_raw
    from .s13_np_raw import s13_np_raw

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
            name="Extracting Gensim phrases",
            function=s05_np_gensim,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting Yake phrases",
            function=s06_np_yake,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting known phrases",
            function=s07_np_known,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting abstract acronyms",
            function=s08_abstract_acronyms,
            kwargs=common_kwargs,
        ),
        Step(
            name="Uppercasing ABSTR",
            function=s09_abstr_upper,
            kwargs=common_kwargs,
        ),
        Step(
            name="Uppercasing TITLE",
            function=s10_title_upper,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting ABSTR phrases",
            function=s11_np_abstr_raw,
            kwargs=common_kwargs,
        ),
        Step(
            name="Extracting TITLE phrases",
            function=s12_np_title_raw,
            kwargs=common_kwargs,
        ),
        Step(
            name="Merging TITLE and ABSTR phrases",
            function=s13_np_raw,
            kwargs=common_kwargs,
        ),
    ]

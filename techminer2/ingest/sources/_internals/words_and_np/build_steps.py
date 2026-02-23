# CODE_REVIEW: 2026-01-26


from techminer2._internals import Params

from ..step import Step


def build_words_and_np_steps(params: Params) -> list[Step]:

    from .create_term_thesaurus import create_term_thesaurus
    from .extract_abstract_acronyms import extract_abstract_acronyms
    from .extract_abstract_phrases import extract_abstract_phrases
    from .extract_abstract_words import extract_abstract_words
    from .extract_spacy_phrases import extract_spacy_phrases
    from .extract_textblob_phrases import extract_textblob_phrases
    from .extract_title_phrases import extract_title_phrases
    from .extract_title_words import extract_title_words
    from .merge_keywords_and_phrases import merge_keywords_and_phrases
    from .merge_keywords_and_phrases_and_words import (
        merge_keywords_and_phrases_and_words,
    )
    from .merge_keywords_and_words import merge_keywords_and_words
    from .merge_title_and_abstract_phrases import merge_title_and_abstract_phrases
    from .merge_title_and_abstract_words import merge_title_and_abstract_words
    from .tokenize_raw_abstract import tokenize_raw_abstract
    from .tokenize_raw_title import tokenize_raw_title
    from .update_builtin_noun_phrases import update_builtin_noun_phrases
    from .uppercase_abstract_phrases import uppercase_abstract_phrases
    from .uppercase_abstract_words import uppercase_abstract_words
    from .uppercase_title_phrases import uppercase_title_phrases
    from .uppercase_title_words import uppercase_title_words

    common_kwargs = {"root_directory": params.root_directory}

    return [
        Step(
            name="Tokenizing raw abstracts",
            function=tokenize_raw_abstract,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Tokenizing document titles",
            function=tokenize_raw_title,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Extracting TextBlob NP",
            function=extract_textblob_phrases,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Extracting spaCy NP",
            function=extract_spacy_phrases,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Extracting abstract acronyms",
            function=extract_abstract_acronyms,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Uppercasing abstract NP",
            function=uppercase_abstract_phrases,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Uppercasing title NP",
            function=uppercase_title_phrases,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Uppercasing abstract words",
            function=uppercase_abstract_words,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Uppercasing title words",
            function=uppercase_title_words,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Extracting abstract words",
            function=extract_abstract_words,
            kwargs=common_kwargs,
            count_message="{count} abstract words created",
        ),
        Step(
            name="Extracting title words",
            function=extract_title_words,
            kwargs=common_kwargs,
            count_message="{count} title words created",
        ),
        Step(
            name="Merging title and abstract words",
            function=merge_title_and_abstract_words,
            kwargs=common_kwargs,
            count_message="{count} title and abstract words merged",
        ),
        Step(
            name="Extracting abstract phrases",
            function=extract_abstract_phrases,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Extracting title phrases",
            function=extract_title_phrases,
            kwargs=common_kwargs,
            count_message="{count}  records processed",
        ),
        Step(
            name="Merging title and abstract phrases",
            function=merge_title_and_abstract_phrases,
            kwargs=common_kwargs,
            count_message="{count}  records processed",
        ),
        Step(
            name="Merging keywords and NP",
            function=merge_keywords_and_phrases,
            kwargs=common_kwargs,
            count_message="{count} keywords and NP merged",
        ),
        Step(
            name="Merging keywords and words",
            function=merge_keywords_and_words,
            kwargs=common_kwargs,
            count_message="{count} keywords and words merged",
        ),
        Step(
            name="Merging keywords, NP, and words",
            function=merge_keywords_and_phrases_and_words,
            kwargs=common_kwargs,
            count_message="{count} records processed",
        ),
        Step(
            name="Creating descriptor thesaurus",
            function=create_term_thesaurus,
            kwargs=common_kwargs,
            count_message="{count} descriptors added to thesaurus",
        ),
        Step(
            name="Updating builtin noun phrases",
            function=update_builtin_noun_phrases,
            kwargs=common_kwargs,
            count_message="{count} new builtin noun phrases found",
        ),
    ]

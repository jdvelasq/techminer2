# pylint: disable=import-outside-toplevel


from ..step import Step


def build_title_abstract_keywords_steps(params) -> list[Step]:

    from .normalize_abstract import normalize_abstract
    from .normalize_acronyms import normalize_acronyms
    from .normalize_document_title import normalize_document_title
    from .normalize_raw_abstract_nouns_and_phrases import (
        normalize_raw_abstract_nouns_and_phrases,
    )
    from .normalize_raw_author_keywords import normalize_raw_author_keywords
    from .normalize_raw_document_title_nouns_and_phrases import (
        normalize_raw_document_title_nouns_and_phrases,
    )
    from .normalize_raw_index_keywords import normalize_raw_index_keywords
    from .normalize_raw_spacy_phrases import normalize_raw_spacy_phrases
    from .normalize_raw_textblob_phrases import normalize_raw_textblob_phrases
    from .tokenize_abstract import tokenize_abstract
    from .tokenize_document_title import tokenize_document_title

    return [
        Step(
            name="Normalizing acronyms",
            function=normalize_acronyms,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} acronyms extracted",
        ),
        Step(
            name="Normalizing raw author keywords",
            function=normalize_raw_author_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw author keywords extracted",
        ),
        Step(
            name="Normalizing raw index keywords",
            function=normalize_raw_index_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw index keywords extracted",
        ),
        Step(
            name="Normalizing raw TextBlob phrases",
            function=normalize_raw_textblob_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} TextBlob noun phrases extracted",
        ),
        Step(
            name="Normalizing raw spaCy phrases",
            function=normalize_raw_spacy_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} SpaCy noun phrases extracted",
        ),
        Step(
            name="Tokenizing abstract",
            function=tokenize_abstract,
            kwargs={
                "source": "raw_abstract",
                "target": "tokenized_abstract",
                "root_directory": params.root_directory,
            },
            count_message="{count} abstracts tokenized",
        ),
        Step(
            name="Tokenizing document title",
            function=tokenize_document_title,
            kwargs={
                "source": "raw_document_title",
                "target": "tokenized_document_title",
                "root_directory": params.root_directory,
            },
            count_message="{count} document titles tokenized",
        ),
        Step(
            name="Normalizing abstract",
            function=normalize_abstract,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} abstracts normalized",
        ),
        Step(
            name="Normalizing document title",
            function=normalize_document_title,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} document titles normalized",
        ),
        Step(
            name="Normalizing raw abstract nouns and phrases",
            function=normalize_raw_abstract_nouns_and_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw abstract nouns and phrases normalized",
        ),
        Step(
            name="Normalizing raw document title nouns and phrases",
            function=normalize_raw_document_title_nouns_and_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw document title nouns and phrases normalized",
        ),
        # -----
        # -----
        # Author & index keywords
        # _preprocess_index_keywords(root_directory)
        # _preprocess_author_keywords(root_directory)
        # _preprocess_raw_keywords(root_directory)
        # _preprocess_raw_descriptors(root_directory)
    ]

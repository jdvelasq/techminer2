# pylint: disable=import-outside-toplevel


from ..step import Step


def build_title_abstract_keywords_steps(params) -> list[Step]:

    from .compose_keywords_norm import compose_keywords_norm
    from .compose_keywords_raw import compose_keywords_raw
    from .extract_abstract_acronyms import extract_abstract_acronyms
    from .extract_noun_phrases_spacy import extract_noun_phrases_spacy
    from .extract_noun_phrases_textblob import extract_raw_textblob_phrases
    from .normalize_author_keywords import normalize_author_keywords
    from .normalize_index_keywords import normalize_index_keywords
    from .tokenize_abstract import tokenize_abstract
    from .tokenize_document_title import tokenize_document_title

    return [
        Step(
            name="Compose keywords raw",
            function=compose_keywords_raw,
            kwargs={"root_directory": params.root_directory},
            count_message="Keywords raw composed",
        ),
        Step(
            name="Normalizing author keywords",
            function=normalize_author_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} author keywords normalized",
        ),
        Step(
            name="Normalizing index keywords",
            function=normalize_index_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} index keywords normalized",
        ),
        Step(
            name="Compose Keywords",
            function=compose_keywords_norm,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} keywords composed",
        ),
        Step(
            name="Tokenizing abstract",
            function=tokenize_abstract,
            kwargs={
                "source": "abstract_raw",
                "target": "abstract_tokenized",
                "root_directory": params.root_directory,
            },
            count_message="{count} abstracts tokenized",
        ),
        Step(
            name="Tokenizing document title",
            function=tokenize_document_title,
            kwargs={
                "source": "document_title_raw",
                "target": "document_title_tokenized",
                "root_directory": params.root_directory,
            },
            count_message="{count} document titles tokenized",
        ),
        Step(
            name="Extracting TextBlob noun phrases",
            function=extract_raw_textblob_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} TextBlob noun phrases extracted",
        ),
        Step(
            name="Extracting spaCy noun phrases",
            function=extract_noun_phrases_spacy,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} spaCy noun phrases extracted",
        ),
        #
        Step(
            name="Extracting abstract acronyms",
            function=extract_abstract_acronyms,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} abstract acronyms extracted",
        ),
    ]

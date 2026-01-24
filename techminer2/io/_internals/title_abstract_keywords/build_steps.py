# pylint: disable=import-outside-toplevel


from ..step import Step


def build_title_abstract_keywords_steps(params) -> list[Step]:

    from .clean_raw_author_keywords import clean_raw_author_keywords
    from .clean_raw_index_keywords import clean_raw_index_keywords
    from .create_author_keywords import create_author_keywords
    from .create_descriptors import create_descriptors
    from .create_index_keywords import create_index_keywords
    from .create_keywords import create_keywords
    from .create_raw_abstract_noun_phrases import create_raw_abstract_noun_phrases
    from .create_raw_descriptors import create_raw_descriptors
    from .create_raw_document_title_noun_phrases import (
        create_raw_document_title_noun_phrases,
    )
    from .create_raw_keywords import create_raw_keywords
    from .create_raw_noun_phrases import create_raw_noun_phrases
    from .normalize_acronyms import normalize_acronyms
    from .normalize_raw_spacy_phrases import normalize_raw_spacy_phrases
    from .normalize_raw_textblob_phrases import normalize_raw_textblob_phrases
    from .tokenize_abstract import tokenize_abstract
    from .tokenize_document_title import tokenize_document_title
    from .uppercase_abstract import uppercase_abstract
    from .uppercase_document_title import uppercase_document_title

    return [
        Step(
            name="Normalizing acronyms",
            function=normalize_acronyms,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} acronyms extracted",
        ),
        Step(
            name="Cleaning raw author keywords",
            function=clean_raw_author_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw author keywords cleaned",
        ),
        Step(
            name="Cleaning raw index keywords",
            function=clean_raw_index_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw index keywords cleaned",
        ),
        Step(
            name="Creating Raw Keywords",
            function=create_raw_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="Raw keywords created",
        ),
        Step(
            name="Creating Author Keywords",
            function=create_author_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="Author keywords created",
        ),
        Step(
            name="Creating Index Keywords",
            function=create_index_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="Index keywords created",
        ),
        Step(
            name="Creating Keywords",
            function=create_keywords,
            kwargs={"root_directory": params.root_directory},
            count_message="Keywords created",
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
            name="Uppercase abstract",
            function=uppercase_abstract,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} abstracts uppercased",
        ),
        Step(
            name="Uppercase document title",
            function=uppercase_document_title,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} document titles uppercased",
        ),
        Step(
            name="Creating raw abstract noun phrases",
            function=create_raw_abstract_noun_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw abstract noun phrases created",
        ),
        Step(
            name="Creating raw document title noun phrases",
            function=create_raw_document_title_noun_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw document title noun phrases created",
        ),
        Step(
            name="Creating raw noun phrases",
            function=create_raw_noun_phrases,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw noun phrases created",
        ),
        Step(
            name="Creating raw descriptors",
            function=create_raw_descriptors,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} raw descriptors created",
        ),
        Step(
            name="Creating descriptors",
            function=create_descriptors,
            kwargs={"root_directory": params.root_directory},
            count_message="{count} descriptors created",
        ),
        # -----
        # -----
        # Author & index keywords
        # _preprocess_raw_descriptors(root_directory)
    ]

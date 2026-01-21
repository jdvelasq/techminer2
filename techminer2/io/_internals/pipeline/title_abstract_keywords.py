# pylint: disable=import-outside-toplevel


from ..title_abstract_keywords import (
    normalize_acronyms,
    normalize_raw_author_keywords,
    normalize_raw_index_keywords,
    normalize_raw_spacy_phrases,
)
from .step import Step


def build_title_abstract_keywords_steps(params) -> list[Step]:

    from ..title_abstract_keywords import normalize_raw_textblob_phrases

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
        # -----
        # -----
        # Author & index keywords
        # _preprocess_index_keywords(root_directory)
        # _preprocess_author_keywords(root_directory)
        # _preprocess_raw_keywords(root_directory)
        # _preprocess_raw_descriptors(root_directory)
    ]

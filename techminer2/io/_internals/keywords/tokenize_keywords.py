from techminer2 import CorpusField
from techminer2._internals.data_access import load_main_data, save_main_data

from ..operations import copy_column
from .helpers import (
    add_padding,
    fix_parenthesis_spacing,
    invert_acronym_definition,
    normalize_empty_strings,
    normalize_quotes,
    remove_accents,
    remove_empty_terms,
    remove_html_tags,
    remove_leading_articles,
    remove_padding,
    remove_possessives_ampersands_and_punctuation,
    strip_surrounding_chars,
    transform_keywords_to_lower_case,
    translate,
)


def tokenize_keywords(root_directory: str) -> int:

    copy_column(
        source=CorpusField.IDX_KEY_RAW,
        target=CorpusField.IDX_KEY_TOK,
        root_directory=root_directory,
    )

    copy_column(
        source=CorpusField.AUTH_KEY_RAW,
        target=CorpusField.AUTH_KEY_TOK,
        root_directory=root_directory,
    )

    dataframe = load_main_data(root_directory)
    dataframe = normalize_empty_strings(dataframe)
    dataframe = add_padding(dataframe)
    dataframe = remove_accents(dataframe)
    dataframe = transform_keywords_to_lower_case(dataframe)
    dataframe = remove_html_tags(dataframe)
    dataframe = fix_parenthesis_spacing(dataframe)
    dataframe = invert_acronym_definition(dataframe)
    dataframe = translate(dataframe)
    dataframe = remove_leading_articles(dataframe)
    dataframe = normalize_quotes(dataframe)
    dataframe = strip_surrounding_chars(dataframe)
    dataframe = remove_possessives_ampersands_and_punctuation(dataframe)
    dataframe = remove_empty_terms(dataframe)
    dataframe = remove_padding(dataframe)

    save_main_data(dataframe, root_directory)

    return max(
        int(dataframe[CorpusField.AUTH_KEY_TOK.value].notna().sum()),
        int(dataframe[CorpusField.IDX_KEY_TOK.value].notna().sum()),
    )

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Replace descriptors in abstracts and titles"""

import pathlib
import re
import sys

import pandas as pd  # type: ignore
from tqdm import tqdm  # type: ignore

from ....._internals import Params
from .....package_data.text_processing import internal__load_text_processing_terms
from ...._internals.io import (
    internal__load_all_records_from_database,
    internal__write_records_to_database,
)


# ------------------------------------------------------------------------------
def notify_process_start(source):
    sys.stderr.write(f"Highlighting tokens in '{source}' field\n")
    sys.stderr.flush()


# ------------------------------------------------------------------------------
def load_all_records_from_database(root_directory):
    params = Params(root_directory=root_directory)
    records = internal__load_all_records_from_database(params)
    return records


# ------------------------------------------------------------------------------
def write_records_to_database(dataframe, root_directory):
    params = Params(root_directory=root_directory)
    internal__write_records_to_database(params=params, records=dataframe)


# ------------------------------------------------------------------------------
def prepare_dest_field(dataframe, source, dest):

    dataframe = dataframe.copy()
    dataframe[dest] = (
        dataframe[source].str.lower().str.replace("_", " ").str.replace(" / ", " ")
    )
    return dataframe


# ------------------------------------------------------------------------------
def collect_all_keywords(dataframe):

    terms = []
    for column in [
        "raw_author_keywords",
        "raw_index_keywords",
    ]:
        if column in dataframe.columns:
            terms.append(dataframe[column].dropna().copy())

    terms = pd.concat(terms)
    terms = terms.reset_index(drop=True)

    return terms


# ------------------------------------------------------------------------------
def collect_all_noun_phrases(dataframe, dest):

    terms = []
    for column in [
        "raw_textblob_phrases",
        "raw_spacy_phrases",
    ]:
        if column in dataframe.columns:
            terms.append(dataframe[column].dropna().copy())

    terms = pd.concat(terms)
    terms = terms.str.split("; ")
    terms = terms.explode()
    terms = terms.to_list()

    return terms


# ------------------------------------------------------------------------------
def clean_all_keywords(terms):

    terms = terms.str.translate(str.maketrans("", "", "\"'#!"))
    terms = terms.str.replace(re.compile(r"\(.*\)"), "", regex=True)
    terms = terms.str.replace(re.compile(r"\[.*\]"), "", regex=True)
    terms = terms.str.translate(str.maketrans("_", " "))
    terms = terms.str.lower()
    terms = terms.str.split("; ")
    terms = terms.explode()
    terms = terms.str.strip()
    terms = terms[terms.str.len() > 2]
    terms = terms[~terms.str.contains(r"\d", regex=True)]
    #
    frequent_terms = terms.value_counts()
    frequent_terms = frequent_terms[frequent_terms > 2]
    frequent_terms = frequent_terms.index.to_list()
    #
    terms = terms.drop_duplicates()
    terms = terms.to_list()
    terms = sorted(terms, key=lambda x: (len(x.split(" ")), x), reverse=True)

    return frequent_terms, terms


# ------------------------------------------------------------------------------
def load_known_noun_phrases(root_directory):
    phrases = internal__load_text_processing_terms("known_noun_phrases.txt")
    phrases = [phrase.lower().replace("_", " ") for phrase in phrases]
    return phrases


# ------------------------------------------------------------------------------
def extract_abbreviations_from_text(text):
    #
    # Extract all texts between parentheses and then, add them to the key_terms
    #
    abbreviations = re.findall(r"\((.*?)\)", text)
    abbreviations = [t.strip() for t in abbreviations]
    abbreviations = [t for t in abbreviations if all(c.isalnum() for c in t)]
    abbreviations = list(set(abbreviations))
    return abbreviations


# ------------------------------------------------------------------------------
def clean_key_terms(stopwords, key_terms):
    key_terms = list(set(key_terms))
    key_terms = [term for term in key_terms if term not in stopwords]
    key_terms = [term for term in key_terms if "(" not in term]
    key_terms = [term for term in key_terms if "," not in term]
    key_terms = [term for term in key_terms if not any(char.isdigit() for char in term)]
    return key_terms


# ------------------------------------------------------------------------------
def mark_copyright_text(copyright_regex, text):
    for regex in copyright_regex:
        regex = r"(" + regex + r")"
        regex = re.compile(regex)
        text = re.sub(regex, lambda z: z.group().replace(" ", "_"), text)
    return text


# ------------------------------------------------------------------------------
def mark_template_abstract_compound_markers(text):
    for regex in [
        "? academic practical relevance :",
        "? data visualization tools :",
        "? design methodology approach :",
        "? design/methodology/approach :",
        "? findings and value added :",
        "? implications of the_study :",
        "? managerial implications :",
        "? methodological quality assessment tools include :",
        "? methodology results :",
        "? methods :",
        "? originality value :",
        "? originality/value :",
        "? practical implications :",
        "? problem definition :",
        "? purpose of the article :",
        "? research limitations :",
        "? research limitations implications :",
        "? research limitations/implications :",
        "? research methodology :",
        "? research background :",
        ". academic practical relevance :",
        ". data visualization tools :",
        ". design methodology approach :",
        ". design/methodology/approach :",
        ". implications of the study :",
        ". findings and value added :",
        ". managerial implications :",
        ". methodological quality assessment tools include :",
        ". methodology results :",
        ". methods :",
        ". originality value :",
        ". originality/value :",
        ". practical implications :",
        ". problem definition :",
        ". purpose of the article :",
        ". reporting quality assessment tool :",
        ". research limitations :",
        ". research limitations implications :",
        ". research limitations/implications :",
        ". research methodology :",
        ". research background :",
        ". INTERESTS_DESIGN/METHODOLOGY/APPROACH :",
        "? INTERESTS_DESIGN/METHODOLOGY/APPROACH :",
    ]:
        regex = re.escape(regex)
        regex = r"(" + regex + r")"
        regex = re.compile(regex)
        text = re.sub(regex, lambda z: z.group().replace(" ", "_"), text)
    return text


# ------------------------------------------------------------------------------
def mark_discursive_patterns(discursive_patterns, text):
    pattern = [t for t in discursive_patterns if t in text]
    if len(pattern) > 0:
        regex = "|".join([re.escape(phrase) for phrase in pattern])
        regex = re.compile(r"\b(" + regex + r")\b")
        text = re.sub(regex, lambda z: z.group().lower().replace(" ", "_"), text)
    return text


# ------------------------------------------------------------------------------
def mark_connectors(connectors, text):
    current_connectors = [t for t in connectors if t in text]
    if len(current_connectors) > 0:
        regex = "|".join([re.escape(phrase) for phrase in current_connectors])
        regex = re.compile(r"\b(" + regex + r")\b")
        text = re.sub(regex, lambda z: z.group().lower().replace(" ", "_"), text)
    return text


# ------------------------------------------------------------------------------
def join_consequtive_separate_terms_in_uppercase(text):
    for _ in range(5, 1, -1):
        pattern = "[A-Z][A-Z_]+" + " [A-Z][A-Z_]+"
        matches = re.findall(pattern, text)

        if len(matches) > 0:
            for match in matches:
                regex = re.compile(r"\b" + re.escape(match) + r"\b")
                text = re.sub(
                    regex, lambda z: z.group().upper().replace(" ", "_"), text
                )

    pattern = r"\b([A-Z][A-Z_]+) \( ([A-Z][A-Z_]+) \) ([A-Z][A-Z_]+)\b"
    matches = re.findall(pattern, text)
    if len(matches) > 0:
        for match in matches:
            full_match = f"{match[0]} ( {match[1]} ) {match[2]}"
            replacement = f"{match[0]}_{match[2]}"
            regex = re.compile(r"\b" + re.escape(full_match) + r"\b")
            text = re.sub(regex, replacement, text)

    return text


# ------------------------------------------------------------------------------
def highlight_key_terms(key_terms, text):
    key_terms = sorted(
        key_terms,
        key=lambda x: (len(x.split(" ")), x),
        reverse=True,
    )
    if len(key_terms) > 0:
        for term in key_terms:
            regex = re.compile(r"\b" + re.escape(term) + r"\b")
            text = re.sub(regex, lambda z: z.group().upper().replace(" ", "_"), text)

    return text


# ------------------------------------------------------------------------------
def unmark_lowercase_text(text):
    regex = re.compile(r"\b([a-z_\(\)\d])+\b")
    text = re.sub(regex, lambda z: z.group().replace("_", " "), text)
    regex = re.compile(r"\b\._([a-z_\(\)\d])+_:\b")
    text = re.sub(regex, lambda z: z.group().replace("_", " "), text)
    return text


# ------------------------------------------------------------------------------
def remove_roman_numbers(text):
    roman_numbers = [
        "i",
        "ii",
        "iii",
        "iv",
        "v",
        "vi",
        "vii",
        "viii",
        "ix",
        "x",
    ]
    for roman_number in roman_numbers:
        regex = r"(\( {roman_number.upper()} )\)"
        regex = re.compile(regex, re.IGNORECASE)
        text = re.sub(regex, lambda z: z.group().lower(), text)
    return text


# ------------------------------------------------------------------------------
def remove_marker_words(text):
    for regex in [
        "? AIMS :",
        "? APPROACH :",
        "? BACKGROUND :",
        "? CONCLUSION , SIGNIFICANCE and IMPACT_STUDY :",
        "? CONCLUSION :",
        "? CONCLUSIONS :",
        "? design/METHODOLOGY/approach :",
        "? DISCUSSION :",
        "? FINDINGS :",
        "? FINDINGS and VALUE added :",
        "? GRAPHICAL_ABSTRACT :",
        "? HIGHLIGHTS :",
        "? IMPACT_STATEMENT :",
        "? INTERESTS_DESIGN/METHODOLOGY/APPROACH :",
        "? LIMITATIONS :",
        "? LIMITATIONS and IMPLICATIONS :",
        "? METHOD :",
        "? METHODOLOGY :",
        "? METHODOLOGY and RESULTS :",
        "? METHODS , PROCEDURES , PROCESS :",
        "? METHODS :",
        "? NOVEL/ADDITIVE_INFORMATION :",
        "? OBJECTIVE :",
        "? OBJECTIVES :",
        "? ORIGINALITY :",
        "? ORIGINALITY/VALUE :",
        "? PURPOSE of THE_ARTICLE :",
        "? RECOMMENDATIONS :",
        "? RESEARCH_BACKGROUND :",
        "? RESULT :",
        "? RESULTS , OBSERVATIONS , CONCLUSIONS :",
        "? RESULTS :",
        "? RESULTS and DISCUSSION :",
        "? UNIQUENESS :",
        ". AIMS :",
        ". APPROACH :",
        ". BACKGROUND :",
        ". CONCLUSION , SIGNIFICANCE and IMPACT_STUDY :",
        ". CONCLUSION :",
        ". CONCLUSIONS :",
        ". design/METHODOLOGY/approach :",
        ". DISCUSSION :",
        ". FINDINGS :",
        ". FINDINGS and VALUE added :",
        ". GRAPHICAL_ABSTRACT :",
        ". HIGHLIGHTS :",
        ". IMPACT_STATEMENT :",
        ". INTERESTS_DESIGN/METHODOLOGY/APPROACH :",
        ". LIMITATIONS :",
        ". LIMITATIONS and IMPLICATIONS :",
        ". METHOD :",
        ". METHODOLOGY :",
        ". METHODOLOGY and RESULTS :",
        ". METHODS , PROCEDURES , PROCESS :",
        ". METHODS :",
        ". NOVEL/ADDITIVE_INFORMATION :",
        ". OBJECTIVE :",
        ". OBJECTIVES :",
        ". ORIGINALITY :",
        ". ORIGINALITY/VALUE :",
        ". PURPOSE of THE_ARTICLE :",
        ". RECOMMENDATIONS :",
        ". RESEARCH_BACKGROUND :",
        ". RESULT :",
        ". RESULTS , OBSERVATIONS , CONCLUSIONS :",
        ". RESULTS :",
        ". RESULTS and DISCUSSION :",
        ". UNIQUENESS :",
    ]:
        text = text.replace(regex, regex.lower())

    if text.startswith("AIMS :"):
        text = text.replace("AIMS :", "aims :")
    if text.startswith("AIM :"):
        text = text.replace("AIM :", "aim :")
    if text.startswith("PURPOSE :"):
        text = text.replace("PURPOSE :", "purpose :")
    if text.startswith("PROBLEM_DEFINITION :"):
        text = text.replace("PROBLEM_DEFINITION :", "problem definition :")
    if text.startswith("GRAPHICAL_ABSTRACT :"):
        text = text.replace("GRAPHICAL_ABSTRACT :", "graphical abstract :")
    if text.startswith("SUMMARY :"):
        text = text.replace("SUMMARY :", "summary :")
    if text.startswith("BACKGROUND :"):
        text = text.replace("BACKGROUND :", "background :")

    if text.startswith("OBJECTIVES/SCOPE :"):
        text = text.replace("OBJECTIVES/SCOPE :", "objectives/scope :")
    if text.startswith("OBJECTIVE :"):
        text = text.replace("OBJECTIVE :", "objective :")
    if text.startswith("INTRODUCTION :"):
        text = text.replace("INTRODUCTION :", "introduction :")
    if text.startswith("HIGHLIGHTS :"):
        text = text.replace("HIGHLIGHTS :", "highlights :")

    return text


# ------------------------------------------------------------------------------
def make_final_corrections(text):

    text = text.replace("_,_", "_")
    text = text.replace("_._", "_")
    text = text.replace(" :_", " : ")
    text = text.replace("_:_", " : ")
    text = text.replace("_S_", "_")
    text = text.replace("_http", " http")
    text = text.replace(" i . E . ", " i . e . ")
    text = text.replace(" ( III ) ", " ( iii ) ")
    text = text.replace(" ( IV ) ", " ( iv ) ")
    text = text.replace(" ( V ) ", " ( v ) ")
    text = text.replace(" ( VI ) ", " ( vi ) ")
    text = text.replace(" ( VII ) ", " ( vii ) ")
    text = text.replace(" ( VIII ) ", " ( viii ) ")
    text = text.replace(" ( IX ) ", " ( ix ) ")
    text = text.replace(" ( X ) ", " ( x ) ")
    text = text.replace(" ( AND_III ) ", " ( and iii ) ")
    text = text.replace(" ( AND_IV ) ", " ( and iv ) ")
    text = text.replace(" ( AND_V ) ", " ( and v ) ")
    text = text.replace(" ( AND_VI ) ", " ( and vi ) ")
    text = text.replace(" ( AND_VII ) ", " ( and vii ) ")
    text = text.replace(" ( AND_VIII ) ", " ( and viii ) ")
    text = text.replace(" ( AND_IX ) ", " ( and ix ) ")
    text = text.replace(" ( AND_X ) ", " ( and x ) ")
    text = text.replace(" . S . ", " . s . ")

    text = text.replace(" /MONTH ", " /month ")
    text = text.replace(" EQ./mwh ", " eq./mwh ")
    text = text.replace(" EQ/kw ", " eq/kw ")
    text = text.replace(" EQ/mwh ", " eq/mwh ")
    text = text.replace(" gj/YEAR ", " gj/year ")
    text = text.replace(" gwh/YEAR ", " gwh/year ")
    text = text.replace(" h/DAY ", " h/day ")
    text = text.replace(" HK_$ /KWH ", " hk $ /kwh ")
    text = text.replace(" innwind.EU ", " innwind . eu ")
    text = text.replace(" IRR/kwh ", " irr/kwh ")
    text = text.replace(" kg/YEAR ", " kg/year ")
    text = text.replace(" kwh/DAY ", " kwh/day ")
    text = text.replace(" l/YEAR ", " l/year ")
    text = text.replace(" TONS/YEAR ", " tons/year ")
    text = text.replace(" TON/YEAR ", " ton/year ")
    text = text.replace(" twh/YEAR ", " twh/year ")
    text = text.replace(" US_CENTS/kwh ", " us cents/kwh ")
    text = text.replace(" USD/KW_HR ", " usd/kw_hr ")
    text = text.replace(" USD/kwh ", " usd/kwh ")
    text = text.replace(" USD/mwh ", " usd/mwh ")
    text = text.replace(" you.s ", " you . s ")
    text = text.replace("POLENERGIA/EQUINOR", "polenergia/equinor")
    text = text.replace(" USD/barrel ", " usd/barrel ")
    text = text.replace(" yuan/TON ", " yuan/ton ")
    text = text.replace(" EUR/mwh ", " eur/mwh ")
    text = text.replace(" kwh/MONTH ", " kwh/month ")
    text = text.replace(" EURO/mwh ", " euro/mwh ")
    text = text.replace("/KW_H ", "/kw_h ")
    text = text.replace(" mwh/YEAR ", " mwh/year ")
    text = text.replace(" THE_F . E . c .", " the f . e . c .")
    text = text.replace(" i.E. ", " i.e. ")
    text = text.replace(
        " . THE_CONTRIBUTIONS of THIS_PAPER are : ",
        " . the contributions of this paper are : ",
    )
    text = text.replace(
        ". THE_CONCLUSIONS can be summarized as follows :",
        ". the conclusions can be summarized as follows :",
    )
    text = text.replace("", "")
    text = text.replace("", "")
    text = text.replace("", "")

    return text


# ------------------------------------------------------------------------------
def report_undetected_keywords(frequent_keywords, all_phrases, root_directory):

    undetected_keywords = [
        word for word in frequent_keywords if word not in all_phrases
    ]
    undetected_keywords = sorted(set(undetected_keywords))
    undetected_keywords = [
        word for word in undetected_keywords if len(word.split()) > 1
    ]
    undetected_keywords = [
        word.replace(" ", "_").upper() for word in undetected_keywords
    ]

    undetected_keywords = [word for word in undetected_keywords if len(word) < 100]

    file_path = (
        pathlib.Path(root_directory) / "data/my_keywords/undetected_keywords.txt"
    )

    # if file exists, open and load the content as a list
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            existing_keywords = file.read().splitlines()
        undetected_keywords = list(set(existing_keywords) | set(undetected_keywords))

    with open(file_path, "w", encoding="utf-8") as file:
        for keyword in sorted(undetected_keywords):
            file.write(f"{keyword}\n")


# ------------------------------------------------------------------------------
def collect_urls(text):
    url_pattern = r"(http[s]?://[^\s]+)"
    urls = re.findall(url_pattern, text)
    return urls


# ------------------------------------------------------------------------------
def replace_urls(text, matches):
    if len(matches) == 0:
        return text
    for match in matches:
        regex = re.compile(re.escape(match), re.IGNORECASE)
        text = regex.sub(lambda z: z.group().lower(), text)
    return text


# ------------------------------------------------------------------------------
EMAIL_REGEX = r"[a-za-z0-9. %+-]+@[a-za-z0-9.-]+\.[a-za-z]{2,}"


def transform_email_addresses_to_lower_case(text):

    email_pattern = re.compile(r"\b" + EMAIL_REGEX + r"\b", re.IGNORECASE)
    return email_pattern.sub(lambda z: z.group().lower(), text)


# ------------------------------------------------------------------------------
def internal__highlight_nouns_and_phrases(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_directory,
):
    """:meta private:"""

    notify_process_start(source)
    dataframe = load_all_records_from_database(root_directory)

    if source not in dataframe.columns:
        return

    dataframe = prepare_dest_field(dataframe, source, dest)

    all_keywords = collect_all_keywords(dataframe)
    frequent_keywords, all_keywords = clean_all_keywords(all_keywords)

    all_noun_phrases = collect_all_noun_phrases(dataframe, dest)
    known_noun_phrases = load_known_noun_phrases("known_noun_phrases.txt")
    ## all_noun_phrases += known_noun_phrases

    connectors = internal__load_text_processing_terms("connectors.txt")
    copyright_regex = internal__load_text_processing_terms("copyright_regex.txt")
    stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
    discursive_patterns = internal__load_text_processing_terms(
        "discursive_patterns.txt"
    )

    determiners = internal__load_text_processing_terms("determiners.txt")
    determiners = (
        "(" + "|".join(["^" + determiner + r"\s" for determiner in determiners]) + ")"
    )
    determiners = re.compile(determiners)

    text_noun_phrases = []

    for index, row in tqdm(
        dataframe.iterrows(),
        total=len(dataframe),
        desc=f"  Progress",
        ncols=80,
    ):

        if pd.isna(row[dest]):
            continue

        text = row[dest]

        key_terms = []

        #
        # Algorithm:
        #
        key_terms += [k for k in all_noun_phrases if k in row[dest]]
        text_noun_phrases += key_terms
        key_terms += extract_abbreviations_from_text(text)
        key_terms = clean_key_terms(stopwords, key_terms)
        key_terms += [k for k in all_keywords if k in row[dest]]
        key_terms += [k for k in known_noun_phrases if k in row[dest]]

        url_matches = collect_urls(text)

        text = mark_copyright_text(copyright_regex, text)
        text = mark_template_abstract_compound_markers(text)
        text = mark_discursive_patterns(discursive_patterns, text)
        text = mark_connectors(connectors, text)
        text = highlight_key_terms(key_terms, text)

        text = join_consequtive_separate_terms_in_uppercase(text)

        text = replace_urls(text, url_matches)

        text = unmark_lowercase_text(text)
        text = mark_connectors(connectors, text)
        text = remove_roman_numbers(text)
        text = remove_marker_words(text)

        text = transform_email_addresses_to_lower_case(text)

        #
        # Step 14: make_final_corrections
        #
        text = make_final_corrections(text)

        dataframe.loc[index, dest] = text

    write_records_to_database(dataframe, root_directory)

    report_undetected_keywords(
        frequent_keywords,
        text_noun_phrases + known_noun_phrases,
        root_directory,
    )

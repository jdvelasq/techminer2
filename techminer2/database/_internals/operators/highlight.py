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
from pandarallel import pandarallel
from tqdm import tqdm

from techminer2._internals import Params, stdout_to_stderr
from techminer2._internals.package_data.text_processing import (
    internal__load_text_processing_terms,
)
from techminer2._internals.user_data import (
    internal__load_all_records_from_database,
    internal__write_records_to_database,
)

with stdout_to_stderr():
    pandarallel.initialize(progress_bar=True)

tqdm.pandas(desc="✓ Processing", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}")


SINGLE_STRUCTURED_ABSTRACT_MARKERS = [
    "abstract",
    "abbreviations",
    "aim",
    "aims",
    "analysis",
    "applications",
    "approach",
    "background",
    "conclusion",
    "conclusions",
    "context",
    "contribution",
    "design",
    "discussion",
    "evaluation",
    "evidence",
    "features",
    "findings",
    "funding",
    "goal",
    "highlights",
    "impact",
    "implementation",
    "implications",
    "interpretation",
    "intervention",
    "interventions",
    "introduction",
    "keywords",
    "limitations",
    "method",
    "methodology",
    "methods",
    "objective",
    "objectives",
    "originality",
    "outcomes",
    "participants",
    "patients",
    "place",
    "program",
    "purpose",
    "recommendations",
    "result",
    "results",
    "setting",
    "settings",
    "significance",
    "subjects",
    "suggestions",
    "summary",
    "uniqueness",
    "value",
]

COMPOUND_STRUCTURED_ABSTRACT_MARKERS = [
    "actionable insights",
    "aim and background",
    "aim and methods",
    "aims / objectives",
    "application design",
    "applications of this study",
    "authors ' conclusions",
    "background / objectives",
    "background and aims",
    "background and objective",
    "background and purpose",
    "clinical impact",
    "clinical relevance",
    "clinical significance",
    "clinical registration",
    "clinical trial registration",
    "conclusion , significance and impact study",
    "conclusion and relevance",
    "contribution of the paper",
    "data collection and analysis",
    "data sources",
    "data visualization tools",
    "design / methodology / approach",
    "design / methods",
    "design / settings",
    "design methodology approach",
    "discussion and conclusions",
    "diverse perspectives",
    "ethical considerations",
    "ethics and dissemination",
    "findings and originality",
    "findings and value added",
    "graphical abstract",
    "impact and implications",
    "impact statement",
    "implications for practice and policy",
    "implications for practice",
    "implications for theory and practice",
    "improvements / applications",
    "intended outcomes",
    "interests design / methodology / approach",
    "key findings",
    "key messages",
    "key results",
    "limitations and implications",
    "main findings",
    "main measures",
    "main outcome ( s )",
    "main outcome measure",
    "main outcome measures",
    "main outcomes and measures",
    "main results",
    "managerial implications",
    "material / methods",
    "material and methods",
    "materials and methods",
    "methodological quality assessment tools include",
    "methodology / results",
    "methodology and results",
    "methods , procedures , process",
    "methods / statistical analysis",
    "methods and analysis",
    "methods and findings",
    "methods and results",
    "novel / additive information",
    "novelty / originality of this study",
    "novelty / originality",
    "objectives / scope",
    "originality / value",
    "originality and value",
    "outcome measures",
    "paper aims",
    "patient or public contribution",
    "place and duration of study",
    "practical examples",
    "practical implications",
    "practical relevance",
    "practice implications",
    "problem definition",
    "public interest summary",
    "purpose of review",
    "purpose of the article",
    "purpose of the study",
    "recent findings",
    "reporting quality assessment tool",
    "research background",
    "research design",
    "research limitations / implications",
    "research method",
    "research question",
    "results , observations , conclusions",
    "results and discussion",
    "results show",
    "review methods",
    "scholarly critique",
    "scientific discussion",
    "search methods",
    "selection criteria",
    "setting / participants / intervention",
    "settings and participants",
    "social implications",
    "some key results",
    "study design",
    "subjects and methods",
    "subjects and methods",
    "teaching implications",
    "the topics include",
    "theoretical framework",
]


# ------------------------------------------------------------------------------
def notify_process_start(source):
    sys.stderr.write(f"INFO: Highlighting tokens in '{source}' field\n")
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
    terms = terms.str.translate(str.maketrans("-", " "))  # added
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
def extract_acronyms_from_text(text):
    #
    # Extract all texts between parentheses and then, add them to the key_terms
    #
    acronyms = re.findall(r"\((.*?)\)", text)
    acronyms = [t.strip() for t in acronyms]
    acronyms = [t for t in acronyms if all(c.isalnum() for c in t)]
    acronyms = list(set(acronyms))
    return acronyms


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
def join_consequtive_separate_terms_in_uppercase(text, stopwords):

    for _ in range(5, 1, -1):
        pattern = "[A-Z][A-Z_]+ [A-Z][A-Z_]+"
        matches = re.findall(pattern, text)

        if len(matches) > 0:
            for match in matches:
                word = match.split(" ")[1]
                word = word.split("_")[0]
                if word.lower() in stopwords:
                    continue
                regex = re.compile(r"\b" + re.escape(match) + r"\b")
                text = re.sub(
                    regex, lambda z: z.group().upper().replace(" ", "_"), text
                )

    ##
    pattern = r"' ([A-Z][A-Z_]+) ' ([A-Z][A-Z_]+)\b"
    matches = re.findall(pattern, text)
    if len(matches) > 0:
        for match in matches:

            full_match = f"' {match[0]} ' {match[1]}"
            replacement = f"{match[0]}_{match[1]}"
            regex = re.compile(re.escape(full_match))
            text = re.sub(regex, replacement, text)

    ##
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
    text = text.replace(" ( AND_II ) ", " ( and ii ) ")
    text = text.replace(" ( AND_III ) ", " ( and iii ) ")
    text = text.replace(" ( AND_IV ) ", " ( and iv ) ")
    text = text.replace(" ( AND_V ) ", " ( and v ) ")
    text = text.replace(" ( AND_VI ) ", " ( and vi ) ")
    text = text.replace(" ( AND_VII ) ", " ( and vii ) ")
    text = text.replace(" ( AND_VIII ) ", " ( and viii ) ")
    text = text.replace(" ( AND_IX ) ", " ( and ix ) ")
    text = text.replace(" ( AND_X ) ", " ( and x ) ")
    text = text.replace(" . S . ", " . s . ")

    text = text.replace(" i.E. ", " i.e. ")
    text = text.replace(" E.g. ", " e.g. ")
    text = text.replace(" innwind.EU ", " innwind . eu ")
    text = text.replace(" you.s ", " you . s ")
    text = text.replace(" THE_F . E . c .", " the f . e . c .")

    text = text.replace(
        " . THE_CONTRIBUTIONS of THIS_PAPER are : ",
        " . the contributions of this paper are : ",
    )
    text = text.replace(
        ". THE_CONCLUSIONS can be summarized as follows :",
        ". the conclusions can be summarized as follows :",
    )

    text = text.replace(" ISSN ", " issn ")
    text = text.replace(" EISSN ", " eissn ")
    text = text.replace(" ISBN ", " isbn ")

    return text


# ------------------------------------------------------------------------------
def fix_units(text):

    # Introduces errors in URLs
    # text = re.sub(r"(\d)/([a-zA-Z_0-9]+)", r"\1 /\2", text)

    # Units
    for unit in [
        "cad",
        "capex",
        "cent usd",
        "cent",
        "cents",
        "cny",
        "ct",
        "day",
        "dkk",
        "dollars",
        "e",
        "eq.",
        "eq",
        "eur",
        "euro",
        "gwh",
        "h",
        "hr",
        "irr",
        "kg",
        "kw h",
        "kw_hr",
        "kw",
        "kwel",
        "kwh",
        "kwh",
        "kwhr",
        "l",
        "level",
        "m",
        "month",
        "mw",
        "mwh",
        "mwwp",
        "nt",
        "omr",
        "omr",
        "rmb",
        "s",
        "t",
        "ton",
        "tons",
        "twh",
        "unit",
        "us_cents",
        "uscents",
        "usd",
        "year",
        "yr",
        "yuan",
    ]:
        text = text.replace(
            f" {unit.upper().replace(' ', '_')}/",
            f" {unit.lower().replace(' ', '_')}/",
        )
        text = text.replace(
            f" {unit.upper().replace(' ', '_')}_/",
            f" {unit.lower().replace(' ', '_')}/",
        )
        text = text.replace(
            f"/{unit.upper().replace(' ', '_')} ",
            f"/{unit.lower().replace(' ', '_')} ",
        )
        text = text.replace(
            f"/_{unit.upper().replace(' ', '_')} ",
            f"/{unit.lower().replace(' ', '_')} ",
        )

    text = text.replace("POLENERGIA/EQUINOR", "polenergia/equinor")

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
    undetected_keywords = [term for term in undetected_keywords if "__" not in term]

    for symbol in "!\"#$%&'()*+,-./:;<=>?@[\]^`{|}~":
        undetected_keywords = [
            term for term in undetected_keywords if symbol not in term
        ]

    file_path = (
        pathlib.Path(root_directory) / "data/my_keywords/undetected_keywords.txt"
    )

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
def mark_template_abstract_separators(text):

    for marker in COMPOUND_STRUCTURED_ABSTRACT_MARKERS:

        regex = re.compile(r"^" + marker + " :", re.IGNORECASE)
        text = re.sub(regex, marker.lower().replace(" ", "_") + " :", text)

        pattern_1 = ". " + marker + " :"
        pattern_2 = ". " + marker.replace(" ", "_") + " :"
        text = text.replace(pattern_1, pattern_2)

        pattern_1 = "? " + marker + " :"
        pattern_2 = "? " + marker.replace(" ", "_") + " :"
        text = text.replace(pattern_1, pattern_2)

        pattern_1 = ") " + marker + " :"
        pattern_2 = ") " + marker.replace(" ", "_") + " :"
        text = text.replace(pattern_1, pattern_2)

    return text


# ------------------------------------------------------------------------------
def unmark_template_abstract_markers(text):

    # Corrects structured abstract markers at the beginning of the paragraph:
    # Converts uppercase markers (e.g., "AIM :") to lowercase (e.g., "aim :").

    for term in (
        COMPOUND_STRUCTURED_ABSTRACT_MARKERS + SINGLE_STRUCTURED_ABSTRACT_MARKERS
    ):

        # Corrects structured abstract markers at the beginning of the paragraph:
        regex = re.compile(r"^" + term.replace(" ", "_") + " :", re.IGNORECASE)
        text = re.sub(regex, term.lower() + " :", text)

        # Corrects structured abstract markers inside the paragraph:
        regex = re.compile("\. " + term.replace(" ", "_") + " :", re.IGNORECASE)
        text = re.sub(regex, ". " + term.lower() + " :", text)

        regex = re.compile("\) " + term.replace(" ", "_") + " :", re.IGNORECASE)
        text = re.sub(regex, ") " + term.lower() + " :", text)

        regex = re.compile("\? " + term.replace(" ", "_") + " :", re.IGNORECASE)
        text = re.sub(regex, "? " + term.lower() + " :", text)

        regex = re.compile("' " + term.replace(" ", "_") + " :", re.IGNORECASE)
        text = re.sub(regex, "' " + term.lower() + " :", text)

        ## ending with [
        regex = re.compile("\. " + term.replace(" ", "_") + " \[", re.IGNORECASE)
        text = re.sub(regex, ". " + term.lower() + " [", text)

        regex = re.compile("\) " + term.replace(" ", "_") + " \[", re.IGNORECASE)
        text = re.sub(regex, ") " + term.lower() + " [", text)

        regex = re.compile("\? " + term.replace(" ", "_") + " \[", re.IGNORECASE)
        text = re.sub(regex, "? " + term.lower() + " [", text)

        regex = re.compile("' " + term.replace(" ", "_") + " \[", re.IGNORECASE)
        text = re.sub(regex, "' " + term.lower() + " [", text)

    return text


# ------------------------------------------------------------------------------
def unmark_et_al(text):

    # search uppercase strings where spaces are replaced by "_" and finish in "_et_al"
    regex = re.compile(r"\b[A-Z][A-Z_]+_ET_AL\b")
    text = re.sub(regex, lambda z: z.group().replace("_", " ").lower(), text)

    return text


# ------------------------------------------------------------------------------
def repair_appostrophes(text):

    # Case 1: lowercase letter followed by space and an appostrophe followed by an "S_"
    # for example:
    # in WAYS that address THE_NEEDS of today ' S_STUDENTS and THE_COMPLEXITY of
    text = re.sub(r"([a-z]) ' S_([A-Z])", r"\1 ' s \2", text)

    # Case 1: upper letter followed by space and an appostrophe followed by an "S_"
    # for example:
    # THE_FLIPPED_CLASSROOM_INTERVENTION ' S_EFFECTIVENESS for
    text = re.sub(r"([A-Z]) ' S_([A-Z])", r"\1_\2", text)

    return text


# ------------------------------------------------------------------------------
global all_noun_phrases
global stopwords
global all_keywords
global connectors
global copyright_regex
global known_noun_phrases
global discursive_patterns
global text_noun_phrases


# ------------------------------------------------------------------------------
def process_column(text):

    global all_noun_phrases
    global stopwords
    global all_keywords
    global connectors
    global copyright_regex
    global known_noun_phrases
    global discursive_patterns
    global text_noun_phrases

    if pd.isna(text):
        return pd.NA

    key_terms = []

    #
    # Algorithm:
    #
    key_terms += [k for k in all_noun_phrases if k in text]
    text_noun_phrases += key_terms
    key_terms += extract_acronyms_from_text(text)
    key_terms = clean_key_terms(stopwords, key_terms)
    key_terms += [k for k in all_keywords if k in text]
    key_terms += [k for k in known_noun_phrases if k in text]

    url_matches = collect_urls(text)

    text = mark_copyright_text(copyright_regex, text)
    text = mark_template_abstract_separators(text)
    text = mark_discursive_patterns(discursive_patterns, text)
    text = mark_connectors(connectors, text)

    #
    #
    text = highlight_key_terms(key_terms, text)
    #
    #

    text = repair_appostrophes(text)

    text = join_consequtive_separate_terms_in_uppercase(text, stopwords)

    text = fix_units(text)

    text = replace_urls(text, url_matches)

    text = unmark_lowercase_text(text)
    text = unmark_template_abstract_markers(text)
    text = unmark_et_al(text)
    text = mark_connectors(connectors, text)
    text = remove_roman_numbers(text)

    text = transform_email_addresses_to_lower_case(text)

    text = make_final_corrections(text)

    return text


# ------------------------------------------------------------------------------
def internal__highlight(
    source,
    dest,
    #
    # DATABASE PARAMS:
    root_directory,
):
    """:meta private:"""

    global all_noun_phrases
    global stopwords
    global all_keywords
    global connectors
    global copyright_regex
    global known_noun_phrases
    global discursive_patterns
    global text_noun_phrases

    notify_process_start(dest)

    dataframe = load_all_records_from_database(root_directory)

    if source not in dataframe.columns:
        return

    dataframe[dest] = dataframe[source].copy()

    all_keywords = collect_all_keywords(dataframe)
    frequent_keywords, all_keywords = clean_all_keywords(all_keywords)

    all_noun_phrases = collect_all_noun_phrases(dataframe, dest)
    known_noun_phrases = load_known_noun_phrases("known_noun_phrases.txt")

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

    with stdout_to_stderr():
        dataframe[dest] = dataframe[dest].parallel_apply(process_column)

    sys.stderr.write("\n")
    sys.stderr.flush()

    write_records_to_database(dataframe, root_directory)

    report_undetected_keywords(
        frequent_keywords,
        text_noun_phrases + known_noun_phrases,
        root_directory,
    )


# ------------------------------------------------------------------------------

## def internal__highlight(
##     source,
##     dest,
##     #
##     # DATABASE PARAMS:
##     root_directory,
## ):
##     """:meta private:"""
##
##     notify_process_start(dest)
##
##     dataframe = load_all_records_from_database(root_directory)
##
##     if source not in dataframe.columns:
##         return
##
##     dataframe[dest] = dataframe[source].copy()
##
##     all_keywords = collect_all_keywords(dataframe)
##     frequent_keywords, all_keywords = clean_all_keywords(all_keywords)
##
##     all_noun_phrases = collect_all_noun_phrases(dataframe, dest)
##     known_noun_phrases = load_known_noun_phrases("known_noun_phrases.txt")
##
##     connectors = internal__load_text_processing_terms("connectors.txt")
##     copyright_regex = internal__load_text_processing_terms("copyright_regex.txt")
##     stopwords = internal__load_text_processing_terms("technical_stopwords.txt")
##     discursive_patterns = internal__load_text_processing_terms(
##         "discursive_patterns.txt"
##     )
##
##     determiners = internal__load_text_processing_terms("determiners.txt")
##     determiners = (
##         "(" + "|".join(["^" + determiner + r"\s" for determiner in determiners]) + ")"
##     )
##     determiners = re.compile(determiners)
##
##     text_noun_phrases = []
##
##     for index, row in tqdm(
##         dataframe.iterrows(),
##         total=len(dataframe),
##         desc=f"  Progress",
##         ncols=80,
##     ):
##
##         if pd.isna(row[dest]):
##             continue
##
##         text = row[dest]
##
##         key_terms = []
##
##         #
##         # Algorithm:
##         #
##         key_terms += [k for k in all_noun_phrases if k in row[dest]]
##         text_noun_phrases += key_terms
##         key_terms += extract_acronyms_from_text(text)
##         key_terms = clean_key_terms(stopwords, key_terms)
##         key_terms += [k for k in all_keywords if k in row[dest]]
##         key_terms += [k for k in known_noun_phrases if k in row[dest]]
##
##         url_matches = collect_urls(text)
##
##         text = mark_copyright_text(copyright_regex, text)
##         text = mark_template_abstract_separators(text)
##         text = mark_discursive_patterns(discursive_patterns, text)
##         text = mark_connectors(connectors, text)
##
##         #
##         #
##         text = highlight_key_terms(key_terms, text)
##         #
##         #
##
##         text = repair_appostrophes(text)
##
##         text = join_consequtive_separate_terms_in_uppercase(text, stopwords)
##
##         text = fix_units(text)
##
##         text = replace_urls(text, url_matches)
##
##         text = unmark_lowercase_text(text)
##         text = unmark_template_abstract_markers(text)
##         text = unmark_et_al(text)
##         text = mark_connectors(connectors, text)
##         text = remove_roman_numbers(text)
##
##         text = transform_email_addresses_to_lower_case(text)
##
##         text = make_final_corrections(text)
##
##         dataframe.loc[index, dest] = text
##
##     write_records_to_database(dataframe, root_directory)
##
##     report_undetected_keywords(
##         frequent_keywords,
##         text_noun_phrases + known_noun_phrases,
##         root_directory,
##     )

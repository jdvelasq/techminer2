# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Lemma Associations
=========================================================================================


## >>> from techminer2.search import lemma_associations
## >>> lemmas = lemma_associations(
## ...     #
## ...     # FUNCTION PARAMS:
## ...     lemma_a='INNOVATION',
## ...     lemma_b='FINTECH',
## ...     top_n=10,
## ...     #
## ...     # DATABASE PARAMS:
## ...     root_dir="example/", 
## ...     database="main",
## ...     year_filter=(None, None),
## ...     cited_by_filter=(None, None),
## ... )
## >>> print(lemmas.contexts_) # doctest: +ELLIPSIS 
---...


## >>> print(lemmas.prompt_)  # doctest: +ELLIPSIS
Your task is ...



"""
import os.path
import textwrap
from dataclasses import dataclass

from textblob import TextBlob  # type: ignore

# from ..database.load.load__database import load__filtered_database
from .._internals.utils.utils_format_prompt_for_paragraphs import (
    _utils_format_prompt_for_paragraphs,
)
from ..thesaurus._internals.load_thesaurus_as_mapping import (
    internal__load_thesaurus_as_mapping,
)


def lemma_associations(
    #
    # FUNCTION PARAMS:
    lemma_a,
    lemma_b,
    top_n=10,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """:meta private:"""

    word_groups = __load_word_groups(root_dir)
    lemma_a_word_group = __pick_word_group(lemma_a, word_groups)
    lemma_b_word_group = __pick_word_group(lemma_b, word_groups)

    sentences = __get_abstract_sentences(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    sentences = __select_sentences(
        sentences=sentences,
        lemma_a_word_group=lemma_a_word_group,
        lemma_b_word_group=lemma_b_word_group,
    )

    sentences = sentences.head(top_n)
    prompt = __generate_prompt(sentences, lemma_a, lemma_b)
    contexts = __generate_contexts(sentences)

    @dataclass
    class Results:
        contexts_ = contexts
        frame_ = sentences
        prompt_ = prompt

    return Results()


def __load_word_groups(root_dir):
    #
    # Returns a list of lists with the raw words in each group
    thesaurus_file = os.path.join(root_dir, "thesaurus/descriptors.the.txt")
    thesaurus = internal__load_thesaurus_as_mapping(thesaurus_file)
    return list(thesaurus.values())


def __pick_word_group(word, word_groups):
    #
    # Returns the group of the word
    for group in word_groups:
        if word in group:
            return group
    return None


def __get_abstract_sentences(
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    records = load__filtered_database(
        root_dir=root_dir,
        database=database,
        record_years_range=year_filter,
        record_citations_range=cited_by_filter,
        records_order_by=None,
        **filters,
    )

    records = records.sort_values(
        ["global_citations", "local_citations", "year", "authors"],
        ascending=[False, False, True, True],
    )

    records = records[["record_id", "abstract"]].copy()
    records = records.dropna()
    records["abstract"] = records["abstract"].map(
        lambda x: [str(sentence) for sentence in TextBlob(x).sentences],
        na_action="ignore",
    )
    records = records.explode("abstract")
    records["abstract"] = records["abstract"].str.strip()
    records = records[records["abstract"] != ""]

    return records


def __select_sentences(
    sentences,
    lemma_a_word_group,
    lemma_b_word_group,
):
    sentences["selected"] = False

    for word in lemma_a_word_group:
        sentences.loc[sentences["abstract"].str.contains(word), "selected"] = True
    sentences = sentences[sentences["selected"]]

    sentences.loc[:, "selected"] = False
    for word in lemma_b_word_group:
        sentences.loc[sentences["abstract"].str.contains(word), "selected"] = True
    sentences = sentences[sentences["selected"]]

    sentences = sentences.drop(columns=["selected"])

    sentences = sentences.groupby("record_id").agg({"abstract": list})
    sentences["abstract"] = sentences["abstract"].str.join(". ")
    sentences = sentences.rename(columns={"abstract": "sentence"})

    return sentences


def __generate_prompt(sentences, lemma_a, lemma_b):
    main_text = (
        "Your task is to generate a short summary for a research paper. "
        "Summarize the paragraphs below, delimited by triple backticks, in "
        "one unique paragraph, in at most 30 words, focusing on the any "
        "aspect contributing to explain the relationship between the lemmas "
        f"'{lemma_a}' and '{lemma_b}'. "
    )

    paragraphs = sentences.sentence.copy()

    return _utils_format_prompt_for_paragraphs(main_text, main_text, paragraphs)


def __generate_contexts(sentences):
    sentences = sentences.copy()
    sentences["sentence"] = (
        sentences["sentence"].map(lambda w: textwrap.wrap(w, width=80)).str.join("\n")
    )

    text = ""
    for index, row in sentences.iterrows():
        text += "-" * 90 + "\n"
        text += index + "\n"
        text += row.sentence + "\n\n"

    return text

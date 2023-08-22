# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _tm2.search.lemma_associations:

Lemma Associations
=========================================================================================


>>> from techminer2.search import lemma_associations
>>> lemmas = lemma_associations(
...     #
...     # FUNCTION PARAMS:
...     lemma_a='REGTECH',
...     lemma_b='FINTECH',
...     top_n=10,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(lemmas.contexts_)
------------------------------------------------------------------------------------------
Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN, V2020-September, P112
due to the scarcity of papers about CASE_STUDY in REGTECH_FIELD, we adopt an
approach already used for well-studied cases widespread in the FINTECH_AREA and
an EXPLORATORY_INVESTIGATION through in DEEP_INTERVIEWS following models used in
FINTECH_AREA and in ERM_FIELD.. results/findings: in this ARTICLE, we will,
therefore, propose CASE_STUDIES in the FINTECH_SECTOR applied to
REGULATORY_TECHNOLOGY in italy and we expect to answer the following
RESEARCH_QUESTIONS: we present three REGTECH's cases in italy's FINANCIAL_SYSTEM
exposing the fields of collaboration with FINANCIAL_INSTITUTIONS in
REGTECH_FIELD between incumbents and REGTECH_INDUSTRIES.
<BLANKLINE>
------------------------------------------------------------------------------------------
Boitan IA, 2020, FOSTER INNOVCOMPET WITH FINTE, P1
fostering INNOVATION and COMPETITIVENESS with FINTECH, REGTECH, and SUPTECH
provides emerging research exploring the theoretical and PRACTICAL_ASPECTS of
technologically INNOVATIVE_MECHANISMS and applications within the financial,
economic, and LEGAL_MARKETS.
<BLANKLINE>
------------------------------------------------------------------------------------------
Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19
IT also examines the POTENTIAL_IMPACT_FINTECH has on the riskiness of BANKS and
proposes REGTECH as the solution.
<BLANKLINE>
------------------------------------------------------------------------------------------
Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85
this CHAPTER_EXPLORES the promise and potential of REGULATORY_TECHNOLOGIES
(REGTECH), a new and VITAL_DIMENSION to FINTECH.
<BLANKLINE>
------------------------------------------------------------------------------------------
Chirulli P, 2021, ROUTLEDGE HANDBFINANCIAL TECH, P447
after focusing on the MAIN_CURRENT_TRENDS in FINTECH_REGULATION within the eu,
and on the related phenomenon of REGTECH, this CHAPTER_AIMS to explore the
RECENT_DEVELOPMENTS in SUPTECH and to assess how the employment of TECHNOLOGY
enabled solutions is changing the WAY_AUTHORITIES perform their functions.
<BLANKLINE>
------------------------------------------------------------------------------------------
Cruz Rambaud S, 2022, EUR J RISK REGUL, V13, P333
justification: however, until now, the SPECIFIC_LEGAL_REGIMES (REGTECH) that
have been established for FINTECH have, in addition to the GENERAL_LACK of
confidence in NEW_TECHNOLOGIES, made its implementation more difficult..
objective: therefore, in order to promote an APPROPRIATE_REGTECH that allows for
the progress of FINTECH, IT is necessary to analyse the LEGAL_PROBLEMS that
restrict their expansion by using an ANALYTICAL_METHODOLOGY and a
BIBLIOGRAPHIC_COMPILATION of LEGAL_RESOLUTIONS.
<BLANKLINE>
------------------------------------------------------------------------------------------
Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219
as FINANCIAL_TECHNOLOGIES (FINTECH) pioneers seek to disintermediate the world's
traditional BANKING_SECTOR's intermediary role, NEW_REGULATORY_TECHNOLOGIES
(REGTECH) will be required to guarantee markets can be trusted, CONTRACT_LAWS
are adhered to and COMPLIANCE can be verified through TRANSPARENT_PROCESSES..
services computing researchers will play an IMPORTANT_ROLE in advancing REGTECH,
but they must add to their repertoire ADDITIONAL_KNOWLEDGE of
FINANCIAL_PRINCIPLES, an understanding of COMMON_FINTECH_PATHOLOGIES that may be
exploited by BAD_ACTORS, and new thinking in regard to protecting CUSTOMER_DATA
across MULTIPLE_LEGAL_JURISDICTIONS and the related COMPLIANCE of
BOUNDARY_CROSSING BANKING RELATED_ALGORITHMS.
<BLANKLINE>
------------------------------------------------------------------------------------------
Muganyi T, 2022, FINANCIAL INNOV, V8
we also show that the emergence of FINTECH in the area of FINANCIAL_REGULATION
(REGULATORY_TECHNOLOGY: REGTECH) can significantly improve
FINANCIAL_DEVELOPMENT_OUTCOMES.
<BLANKLINE>
------------------------------------------------------------------------------------------
Nasir F, 2019, J ADV RES DYN CONTROL SYST, V11, P912
these COMPLIANCE CHALLENGES created the market for REGTECH, which is a part of
FINTECH_INDUSTRY, where the REGTECH_INDUSTRY promise to act as a solution to
reduce COMPLIANCE_COST and burden for FINANCIAL_INSTITUTIONS as well as
regulators.
<BLANKLINE>
------------------------------------------------------------------------------------------
Pantielieieva N, 2020, LECTURE NOTES DATA ENG COMMUN, V42, P1
the PAPER_DEALS with the issues of MAIN_DIRECTIONS, CHALLENGES and threats of
DEVELOPMENT of the newest FINANCIAL_TECHNOLOGIESFINTECH, REGTECH and
TRADITIONAL_FINANCIAL_INTERMEDIATION.
<BLANKLINE>
<BLANKLINE>


>>> print(lemmas.prompt_)                        
Your task is to generate a short summary for a research paper. Summarize \\
the paragraphs below, delimited by triple backticks, in one unique \\
paragraph, in at most 30 words, focusing on the any aspect contributing to \\
explain the relationship between the lemmas 'REGTECH' and 'FINTECH'.
<BLANKLINE>
Paragraph 1:
```
due to the scarcity of papers about CASE_STUDY in REGTECH_FIELD, we adopt \\
an approach already used for well-studied cases widespread in the \\
FINTECH_AREA and an EXPLORATORY_INVESTIGATION through in DEEP_INTERVIEWS \\
following models used in FINTECH_AREA and in ERM_FIELD.. results/findings: \\
in this ARTICLE, we will, therefore, propose CASE_STUDIES in the \\
FINTECH_SECTOR applied to REGULATORY_TECHNOLOGY in italy and we expect to \\
answer the following RESEARCH_QUESTIONS: we present three REGTECH's cases \\
in italy's FINANCIAL_SYSTEM exposing the fields of collaboration with \\
FINANCIAL_INSTITUTIONS in REGTECH_FIELD between incumbents and \\
REGTECH_INDUSTRIES.
```
<BLANKLINE>
Paragraph 2:
```
fostering INNOVATION and COMPETITIVENESS with FINTECH, REGTECH, and SUPTECH \\
provides emerging research exploring the theoretical and PRACTICAL_ASPECTS \\
of technologically INNOVATIVE_MECHANISMS and applications within the \\
financial, economic, and LEGAL_MARKETS.
```
<BLANKLINE>
Paragraph 3:
```
IT also examines the POTENTIAL_IMPACT_FINTECH has on the riskiness of BANKS \\
and proposes REGTECH as the solution.
```
<BLANKLINE>
Paragraph 4:
```
this CHAPTER_EXPLORES the promise and potential of REGULATORY_TECHNOLOGIES \\
(REGTECH), a new and VITAL_DIMENSION to FINTECH.
```
<BLANKLINE>
Paragraph 5:
```
after focusing on the MAIN_CURRENT_TRENDS in FINTECH_REGULATION within the \\
eu, and on the related phenomenon of REGTECH, this CHAPTER_AIMS to explore \\
the RECENT_DEVELOPMENTS in SUPTECH and to assess how the employment of \\
TECHNOLOGY enabled solutions is changing the WAY_AUTHORITIES perform their \\
functions.
```
<BLANKLINE>
Paragraph 6:
```
justification: however, until now, the SPECIFIC_LEGAL_REGIMES (REGTECH) \\
that have been established for FINTECH have, in addition to the \\
GENERAL_LACK of confidence in NEW_TECHNOLOGIES, made its implementation \\
more difficult.. objective: therefore, in order to promote an \\
APPROPRIATE_REGTECH that allows for the progress of FINTECH, IT is \\
necessary to analyse the LEGAL_PROBLEMS that restrict their expansion by \\
using an ANALYTICAL_METHODOLOGY and a BIBLIOGRAPHIC_COMPILATION of \\
LEGAL_RESOLUTIONS.
```
<BLANKLINE>
Paragraph 7:
```
as FINANCIAL_TECHNOLOGIES (FINTECH) pioneers seek to disintermediate the \\
world's traditional BANKING_SECTOR's intermediary role, \\
NEW_REGULATORY_TECHNOLOGIES (REGTECH) will be required to guarantee markets \\
can be trusted, CONTRACT_LAWS are adhered to and COMPLIANCE can be verified \\
through TRANSPARENT_PROCESSES.. services computing researchers will play an \\
IMPORTANT_ROLE in advancing REGTECH, but they must add to their repertoire \\
ADDITIONAL_KNOWLEDGE of FINANCIAL_PRINCIPLES, an understanding of \\
COMMON_FINTECH_PATHOLOGIES that may be exploited by BAD_ACTORS, and new \\
thinking in regard to protecting CUSTOMER_DATA across \\
MULTIPLE_LEGAL_JURISDICTIONS and the related COMPLIANCE of \\
BOUNDARY_CROSSING BANKING RELATED_ALGORITHMS.
```
<BLANKLINE>
Paragraph 8:
```
we also show that the emergence of FINTECH in the area of \\
FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH) can significantly \\
improve FINANCIAL_DEVELOPMENT_OUTCOMES.
```
<BLANKLINE>
Paragraph 9:
```
these COMPLIANCE CHALLENGES created the market for REGTECH, which is a part \\
of FINTECH_INDUSTRY, where the REGTECH_INDUSTRY promise to act as a \\
solution to reduce COMPLIANCE_COST and burden for FINANCIAL_INSTITUTIONS as \\
well as regulators.
```
<BLANKLINE>
Paragraph 10:
```
the PAPER_DEALS with the issues of MAIN_DIRECTIONS, CHALLENGES and threats \\
of DEVELOPMENT of the newest FINANCIAL_TECHNOLOGIESFINTECH, REGTECH and \\
TRADITIONAL_FINANCIAL_INTERMEDIATION.
```
<BLANKLINE>
<BLANKLINE>


"""
import os.path
import textwrap
from dataclasses import dataclass

from textblob import TextBlob

from .._read_records import read_records
from ..format_prompt_for_paragraphs import format_prompt_for_paragraphs
from ..thesaurus_lib import load_system_thesaurus_as_dict


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
    """Checks the occurrence contexts of a given text in the abstract's phrases.

    :meta private:
    """

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
    thesaurus_file = os.path.join(root_dir, "words.txt")
    thesaurus = load_system_thesaurus_as_dict(thesaurus_file)
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
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    records = records.sort_values(
        ["global_citations", "local_citations", "year", "authors"],
        ascending=[False, False, True, True],
    )

    records = records[["article", "abstract"]].copy()
    records = records.dropna()
    records["abstract"] = records["abstract"].map(
        lambda x: [str(sentence) for sentence in TextBlob(x).sentences], na_action="ignore"
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

    sentences["selected"] = False
    for word in lemma_b_word_group:
        sentences.loc[sentences["abstract"].str.contains(word), "selected"] = True
    sentences = sentences[sentences["selected"]]

    sentences = sentences.drop(columns=["selected"])

    sentences = sentences.groupby("article").agg({"abstract": list})
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

    paragraphs = sentences.sentence.to_list()

    return format_prompt_for_paragraphs(main_text, paragraphs)


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

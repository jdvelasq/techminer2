# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _search.concordances:

Concordances
=========================================================================================

Abstract concordances exploration tool.


>>> from techminer2.search import concordances
>>> results = concordances(
...     #
...     # FUNCTION PARAMS:
...     search_for='REGTECH',
...     top_n=10,
...     report_file="concordances_report.txt",
...     prompt_file="concordances_prompt.txt",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(results.contexts_)
                                                             REGTECH can provide an INVALUABLE_TOOL, in a BUSINESS_AS_USUAL_E >>>
                                                             REGTECH to date has focused on the DIGITIZATION of manual REPORT >>>
                                                             REGTECH to date has focused on the DIGITIZATION of manual REPORT >>>
                                                             REGTECH will not eliminate POLICY_CONSIDERATIONS, nor will IT re >>>
           although also not a panacea, the DEVELOPMENT of " REGTECH " solutions will help clear away volumes of work that un >>>
                                  REGULATORY_TECHNOLOGY or ' REGTECH ' is the use of TECHNOLOGY, particularly INFORMATION_TEC >>>
<<< S the promise and potential of REGULATORY_TECHNOLOGIES ( REGTECH ), a new and VITAL_DIMENSION to FINTECH
<<< paper, the authors propose a novel, REGULAR_TECHNOLOGY ( REGTECH ) cum automated LEGAL_TEXT_APPROACH for FINANCIAL_TRANSA >>>
                                     REGULATORY_TECHNOLOGY ( REGTECH ) is an emerging TECHNOLOGY_TREND leveraging INFORMATION >>>
<<< rpose of this paper is to explore the solutions that AI, REGTECH and CHARITYTECH provide to charities in navigating the V >>>
                                                in contrast, REGTECH has recently brought GREAT_SUCCESS to FINANCIAL_COMPLIAN >>>
<<< the area of FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH ) can significantly improve FINANCIAL_DEVELOPMENT_OUTCOMES
<<< egulator based SELF_ASSESSMENT_CHECKLIST to establish if REGTECH best practice could improve the demonstration of GDPR_CO >>>
<<< LD, sets the foundation for a PRACTICAL_UNDERSTANDING of REGTECH , and proposes sequenced reforms that could BENEFIT regu >>>
                 the chapter notes that the FULL_BENEFITS of REGTECH will only materialise if the pitfalls of a fragmented to >>>
                 nevertheless, a SOPHISTICATED_DEPLOYMENT of REGTECH should help FOCUS_REGULATORY_DISCRETION and PUBLIC_POLIC >>>
                                   however, the potential of REGTECH is far greater   IT could enable close to REAL_TIME_MONI >>>
                                   however, the potential of REGTECH is far greater  IT has the potential to enable a nearly  >>>
                        this PAPER_EXPLORES the potential of REGTECH and the merit of incorporating IT into a SMART_TREASURY_ >>>
<<< and regulators, and provided an ENVIRONMENT within which REGTECH can flourish
<<< L_SYSTEMS requires increasing the use of and reliance on REGTECH 
                                             EUROPES_ROAD to REGTECH has rested upon four apparently unrelated pillars: (1) e >>>
<<< otwithstanding the RISK_REDUCTIONS and COST_SAVINGS that REGTECH can deliver
<<<  FIVE_YEAR_RESEARCH_PROGRAMME to highlight the role that REGTECH can play in making REGULATORY_COMPLIANCE more efficient  >>>
<<< emantically enabled applications can be made possible by REGTECH 


print(results.prompt_)                        
Your task is to generate a short summary of a term for a research paper. \
Summarize the paragraphs below, delimited by triple backticks, in one \
unique paragraph, in at most 30 words, focusing on the any aspect \
contributing to the definition and characteristics of the term 'REGTECH'.
<BLANKLINE>
Paragraph 1:
```
REGULATORY_TECHNOLOGY or ' REGTECH ' is the use of TECHNOLOGY, particularly \
INFORMATION_TECHNOLOGY, in the context of REGULATORY_MONITORING, REPORTING \
and COMPLIANCE.   REGTECH to date has focused on the DIGITIZATION of manual \
REPORTING and COMPLIANCE_PROCESSES, for example in the context of \
KNOW_YOUR_CUSTOMER_REQUIREMENTS.  however, the potential of REGTECH is far \
greater   IT could enable close to REAL_TIME_MONITORING and a \
PROPORTIONATE_REGULATORY_REGIME that ADDRESSES_RISK and facilitates more \
EFFICIENT_REGULATORY_COMPLIANCE
```
<BLANKLINE>
Paragraph 2:
```
regulating rapidly transforming FINANCIAL_SYSTEMS requires increasing the \
use of and reliance on REGTECH .   REGTECH to date has focused on the \
DIGITIZATION of manual REPORTING and COMPLIANCE_PROCESSES.  however, the \
potential of REGTECH is far greater  IT has the potential to enable a \
nearly real-time and PROPORTIONATE_REGULATORY_REGIME that identifies and \
ADDRESSES_RISK while facilitating more EFFICIENT_REGULATORY_COMPLIANCE. \
this paper seeks to expose the inadequacy of digitizing ANALOGUE_PROCESSES \
in a digital FINANCIAL_WORLD, sets the foundation for a \
PRACTICAL_UNDERSTANDING of REGTECH , and proposes sequenced reforms that \
could BENEFIT regulators, industry, and entrepreneurs in the \
FINANCIAL_SECTOR and other industries
```
<BLANKLINE>
Paragraph 3:
```
although also not a panacea, the DEVELOPMENT of " REGTECH " solutions will \
help clear away volumes of work that understaffed and underfunded \
regulators cannot keep up with.   REGTECH will not eliminate \
POLICY_CONSIDERATIONS, nor will IT render \
REGULATORY_DECISIONS_NONCONTROVERSIAL.  nevertheless, a \
SOPHISTICATED_DEPLOYMENT of REGTECH should help FOCUS_REGULATORY_DISCRETION \
and PUBLIC_POLICY_DEBATE on the elements of REGULATION where choices really \
matter
```
<BLANKLINE>
Paragraph 4:
```
EUROPES_ROAD to REGTECH has rested upon four apparently unrelated pillars: \
(1) extensive REPORTING requirements imposed after the \
GLOBAL_FINANCIAL_CRISIS to control SYSTEMIC_RISK and change in \
FINANCIAL_SECTOR_BEHAVIOUR.  we argue that the EUROPEAN_UNIONS \
FINANCIAL_SERVICES and DATA_PROTECTION_REGULATORY_REFORMS have \
unintentionally driven the use of REGULATORY_TECHNOLOGIES (REGTECH) by \
intermediaries, supervisors and regulators, and provided an ENVIRONMENT \
within which REGTECH can flourish
```
<BLANKLINE>
Paragraph 5:
```
this CHAPTER_EXPLORES the promise and potential of REGULATORY_TECHNOLOGIES \
( REGTECH ), a new and VITAL_DIMENSION to FINTECH.  IT draws on the \
findings and outcomes of a FIVE_YEAR_RESEARCH_PROGRAMME to highlight the \
role that REGTECH can play in making REGULATORY_COMPLIANCE more efficient \
and effective.  the chapter presents research on the BANK of \
england/FINANCIAL_CONDUCT_AUTHORITY (fca) REGTECH_SPRINT_INITIATIVE, whose \
objective was to demonstrate how STRAIGHT_THROUGH_PROCESSING of REGULATIONS \
and REGULATORY_COMPLIANCE REPORTING using semantically enabled applications \
can be made possible by REGTECH .  the chapter notes that the FULL_BENEFITS \
of REGTECH will only materialise if the pitfalls of a fragmented tower of \
BABEL_APPROACH are avoided
```
<BLANKLINE>
Paragraph 6:
```
design/methodology/approach: in this paper, the authors propose a novel, \
REGULAR_TECHNOLOGY ( REGTECH ) cum automated LEGAL_TEXT_APPROACH for \
FINANCIAL_TRANSACTION as well as FINANCIAL_RISK REPORTING that is based on \
cutting-edge distributed computing and decentralised \
DATA_MANAGEMENT_TECHNOLOGIES such as DISTRIBUTED_LEDGER (swanson, 2015), \
distributed storage (arner et al
```
<BLANKLINE>
Paragraph 7:
```
we also show that the emergence of FINTECH in the area of \
FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH ) can significantly \
improve FINANCIAL_DEVELOPMENT_OUTCOMES
```
<BLANKLINE>
Paragraph 8:
```
in contrast, REGTECH has recently brought GREAT_SUCCESS to \
FINANCIAL_COMPLIANCE, resulting in reduced RISK, COST_SAVING and enhanced \
FINANCIAL_REGULATORY_COMPLIANCE.  a PROOF_OF_CONCEPT_PROTOTYPE was explored \
using a regulator based SELF_ASSESSMENT_CHECKLIST to establish if REGTECH \
best practice could improve the demonstration of GDPR_COMPLIANCE.  the \
application of a REGTECH_APPROACH provides OPPORTUNITIES for demonstrable \
and validated GDPR_COMPLIANCE, notwithstanding the RISK_REDUCTIONS and \
COST_SAVINGS that REGTECH can deliver
```
<BLANKLINE>
Paragraph 9:
```
the purpose of this paper is to explore the solutions that AI, REGTECH and \
CHARITYTECH provide to charities in navigating the VAST_AMOUNT of \
ANTI_MONEY_LAUNDERING and COUNTER_TERROR_FINANCE_LEGISLATION in the uk
```
<BLANKLINE>
Paragraph 10:
```
REGULATORY_TECHNOLOGY ( REGTECH ) is an emerging TECHNOLOGY_TREND \
leveraging INFORMATION_TECHNOLOGY and DIGITAL_INNOVATIONS that can greatly \
assist with a BANKS_REGULATORY_MANAGEMENT_PROCESS.   REGTECH can provide an \
INVALUABLE_TOOL, in a BUSINESS_AS_USUAL_ENVIRONMENT, as well as in \
REAL_LIFE_STRESS_EVENTS, such as the RECENT_CORONAVIRUS_OUTBREAK.  this \
PAPER_EXPLORES the potential of REGTECH and the merit of incorporating IT \
into a SMART_TREASURY_DEPARTMENT
```
<BLANKLINE>
<BLANKLINE>


"""
import os.path
import textwrap
from dataclasses import dataclass

import pandas as pd

from .._read_records import read_records
from ..format_prompt_for_paragraphs import format_prompt_for_paragraphs


def concordances(
    #
    # FUNCTION PARAMS:
    search_for,
    top_n,
    report_file="concordances_report.txt",
    prompt_file="concordances_prompt.txt",
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

    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    contexts, frame, prompt = concordances_from_records(
        search_for=search_for,
        top_n=top_n,
        report_file=report_file,
        prompt_file=prompt_file,
        root_dir=root_dir,
        records=records,
    )

    @dataclass
    class Results:
        contexts_ = contexts
        frame_ = frame
        prompt_ = prompt

    return Results()


def concordances_from_records(
    search_for,
    top_n,
    report_file,
    prompt_file,
    root_dir,
    records,
):
    """
    :meta private:
    """

    def get_phrases(records):
        """Gets the phrases with the searched text."""

        records = records.set_index(pd.Index(records.article + " / " + records.title))

        records = records.sort_values(
            ["global_citations", "local_citations", "year"],
            ascending=[False, False, True],
        )

        records["_found_"] = (
            records["abstract"].astype(str).str.contains(r"\b" + search_for + r"\b", regex=True)
        )
        records = records[records["_found_"]].head(top_n)

        abstracts = records["abstract"]
        abstracts = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        abstracts = abstracts[abstracts.map(lambda x: search_for in x)]

        return abstracts

    def create_contexts_table(phrases):
        """Extracts the contexts table."""

        regex = r"\b" + search_for + r"\b"
        contexts = phrases.str.extract(
            r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)"
        )

        contexts["left_context"] = contexts["left_context"].fillna("")
        contexts["left_context"] = contexts["left_context"].str.strip()

        contexts["right_context"] = contexts["right_context"].fillna("")
        contexts["right_context"] = contexts["right_context"].str.strip()

        contexts = contexts[
            contexts["left_context"].map(lambda x: x != "")
            | contexts["right_context"].map(lambda x: x != "")
        ]

        return contexts

    def transform_context_to_text(contexts):
        """Transforms the contexts table to a text."""

        contexts = contexts.copy()

        contexts["left_r"] = contexts["left_context"].str[::-1]

        contexts = contexts.sort_values(["left_r", "right_context"])

        contexts["left_context"] = contexts["left_context"].map(
            lambda x: "<<< " + x[-56:] if len(x) > 60 else x
        )
        contexts["right_context"] = contexts["right_context"].map(
            lambda x: x[:56] + " >>>" if len(x) > 60 else x
        )

        texts = []
        for _, row in contexts.iterrows():
            text = f"{row['left_context']:>60} {search_for.upper()} {row['right_context']}"
            texts.append(text)

        return "\n".join(texts)

    def generate_prompt(phrases):
        """Generates the chatgpt prompt."""

        phrases = phrases.copy()
        phrases["text"] = (
            phrases["left_context"] + f" {search_for.upper()} " + phrases["right_context"]
        )
        phrases["article"] = phrases.index.to_list()
        phrases = phrases[["text", "article"]]
        phrases = phrases.groupby("article").agg({"text": list})
        phrases = phrases.text.str.join(".  ")

        main_text = (
            "Your task is to generate a short summary of a term for a research "
            "paper. Summarize the paragraphs below, delimited by triple backticks, "
            "in one unique paragraph, in at most 30 words, focusing on the any aspect contributing "
            f"to the definition and characteristics of the term '{search_for.upper()}'."
        )

        paragraphs = phrases.to_list()

        return format_prompt_for_paragraphs(main_text, paragraphs)

    def fill(text):
        if isinstance(text, str):
            return textwrap.fill(
                text,
                width=87,
                initial_indent=" " * 0,
                subsequent_indent=" " * 0,
                fix_sentence_endings=True,
            )
        return ""

    def write_report(phrases, report_file):
        """Writes the report."""

        phrases = phrases.copy()
        phrases = phrases.to_frame()
        phrases["doc"] = phrases.index
        phrases = phrases.groupby("doc")["abstract"].apply(list)
        # phrases = phrases.map(lambda x: ".  ".join(x))
        phrases = phrases.str.join(".  ")

        file_path = os.path.join(root_dir, "reports", report_file)
        with open(file_path, "w", encoding="utf-8") as file:
            counter = 0
            for title, phrase in zip(phrases.index, phrases):
                print(f"-- {counter:03d} " + "-" * 83, file=file)
                print("AR: ", end="", file=file)
                print(fill(title), file=file)
                print("", file=file)
                print(fill(phrase), file=file)
                print("\n", file=file)
                counter += 1

    def write_prompt_file():
        file_path = os.path.join(root_dir, "reports", prompt_file)
        with open(file_path, "w", encoding="utf-8") as file:
            print(prompt_, file=file)

    #
    # Main code:
    #
    phrases = get_phrases(records)
    frame_ = create_contexts_table(phrases)
    contexts_ = transform_context_to_text(frame_)
    prompt_ = generate_prompt(frame_)

    write_report(phrases, report_file)
    write_prompt_file()

    return contexts_, frame_, prompt_

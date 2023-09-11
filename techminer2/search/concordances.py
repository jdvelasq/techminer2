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
                                                             REGTECH to date has focused on the digitization of manual report >>>
                                  REGULATORY_TECHNOLOGY or ' REGTECH ' is the use of technology, particularly INFORMATION_TEC >>>
<<< S the promise and potential of REGULATORY_TECHNOLOGIES ( REGTECH ), a new and VITAL_DIMENSION to FINTECH
<<< paper, the authors propose a novel, REGULAR_TECHNOLOGY ( REGTECH ) cum automated LEGAL_TEXT_APPROACH for FINANCIAL_TRANSA >>>
<<< development of the newest FINANCIAL_TECHNOLOGIESFINTECH, REGTECH and TRADITIONAL_FINANCIAL_INTERMEDIATION
<<< rpose of this paper is to explore the solutions that ai, REGTECH and CHARITYTECH provide to charities in navigating the V >>>
                                                in contrast, REGTECH has recently brought GREAT_SUCCESS to FINANCIAL_COMPLIAN >>>
<<< the area of FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH ) can significantly improve FINANCIAL_DEVELOPMENT_OUTCOMES
<<< s and specialists of anti FINANCIAL_CRIME COMPLIANCE and REGTECH , five MAIN_PREDICTIONS have been developed
<<< egulator based SELF_ASSESSMENT checklist to establish if REGTECH best practice could improve the demonstration of GDPR_CO >>>
                 the chapter notes that the FULL_BENEFITS of REGTECH will only materialise if the pitfalls of a fragmented to >>>
                                   however, the potential of REGTECH is far greater   it could enable close to REAL_TIME_MONI >>>
<<< and regulators, and provided an environment within which REGTECH can flourish
     the PAPER_ARGUES that these provide a platform on which REGTECH can perform EFFECTIVE_RISK_MANAGEMENT and COMPLIANCE_REP >>>
<<< ide insights for other societies in developing their own REGTECH ecosystems in order to support more efficient, stable, i >>>
                                             EUROPES_ROAD to REGTECH has rested upon four apparently unrelated pillars: (1) e >>>
<<< MPACT_FINTECH has on the riskiness of banks and proposes REGTECH as the solution
<<< otwithstanding the RISK_REDUCTIONS and COST_SAVINGS that REGTECH can deliver
<<<  five year research programme to highlight the role that REGTECH can play in making REGULATORY_COMPLIANCE more efficient  >>>
<<< emantically enabled applications can be made possible by REGTECH 




>>> print(results.prompt_)                        
You are an automated scientific writer assistant. Use only the \
information provided in the following records to write one paragraph \
focusing on the any aspect contributing to the definition and \
characteristics of the term 'REGTECH'. Use the Record-No value between \
brackets to indicate the reference to the record. For example, [1] means \
that the information is in the Record-No 1. Use notes below of the \
generated text to justify the affirmation. Use only phrases appearing in \
the provided text. Here are the records:   ---  Improve and make more \
clear the explanation of definition and characterisitcs of the term: \
'REGTECH' in the next paragraphs delimited by '<<<' and '>>>', using only \
the information provided in the records presented below. Add cites to the \
added text using the corresponding Record-No value between brackets. \
Here are text to improve and make more clear:  <<<   >>>   Here are the \
records:
<BLANKLINE>
Record-No: 1
Artile: Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359 / REGTECH: building a better FINANCIAL_SYSTEM
Text:```
REGULATORY_TECHNOLOGY or 'REGTECH' is the use of technology, particularly \
INFORMATION_TECHNOLOGY, in the context of regulatory monitoring, \
reporting and compliance.  REGTECH to date has focused on the \
digitization of manual reporting and COMPLIANCE_PROCESSES, for example in \
the context of know your CUSTOMER_REQUIREMENTS.  however, the potential \
of REGTECH is far greater   it could enable close to REAL_TIME_MONITORING \
and a PROPORTIONATE_REGULATORY_REGIME that ADDRESSES_RISK and facilitates \
more EFFICIENT_REGULATORY_COMPLIANCE
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 2
Artile: Buckley RP, 2020, J BANK REGUL, V21, P26 / the road to REGTECH: the (astonishing) example of the EUROPEAN_UNION
Text:```
EUROPES_ROAD to REGTECH has rested upon four apparently unrelated \
pillars: (1) extensive reporting requirements imposed after the global \
financial crisis to control SYSTEMIC_RISK and change in \
FINANCIAL_SECTOR_BEHAVIOUR.  the paper analyses these four pillars and \
suggests that together they are underpinning the development of a \
REGTECH_ECOSYSTEM in europe and will continue to do so.  we argue that \
the EUROPEAN_UNIONS FINANCIAL_SERVICES and \
DATA_PROTECTION_REGULATORY_REFORMS have unintentionally driven the use of \
REGULATORY_TECHNOLOGIES (REGTECH) by intermediaries, supervisors and \
regulators, and provided an environment within which REGTECH can \
flourish.  the experiences of europe in this process will provide \
insights for other societies in developing their own REGTECH ecosystems \
in order to support more efficient, stable, inclusive financial systems
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 3
Artile: Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19 / on the role of ontology based REGTECH for managing risk and COMPLIANCE_REPORTING in the age of REGULATION
Text:```
this PAPER_ADDRESSES IMPORTANT_QUESTIONS such as: what challenges are \
presented by NEW_REGULATION to BANKS_INFRASTRUCTURE, RISK_MANAGEMENT and \
profitability, and how can these challenges be best addressed? it also \
examines the POTENTIAL_IMPACT_FINTECH has on the riskiness of banks and \
proposes REGTECH as the solution.  following a BRIEF_OVERVIEW of the \
impact and costs of REGULATION since the FINANCIAL_CRISIS, the \
PAPER_INTRODUCES_REGTECH in the context of challenges facing \
FINANCIAL_INSTITUTIONS and the limitations of governance, risk and \
compliance (grc) systems.  the PAPER_ARGUES that these provide a platform \
on which REGTECH can perform EFFECTIVE_RISK_MANAGEMENT and \
COMPLIANCE_REPORTING in a global post crisis regulatory environment
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 4
Artile: Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85 / UNDERSTANDING_REGTECH for DIGITAL_REGULATORY_COMPLIANCE
Text:```
this CHAPTER_EXPLORES the promise and potential of \
REGULATORY_TECHNOLOGIES (REGTECH), a new and VITAL_DIMENSION to FINTECH. \
it draws on the findings and outcomes of a five year research programme \
to highlight the role that REGTECH can play in making \
REGULATORY_COMPLIANCE more efficient and effective.  the chapter presents \
research on the bank of england/financial conduct authority (fca) \
REGTECH_SPRINT_INITIATIVE, whose objective was to demonstrate how \
straight through processing of regulations and REGULATORY_COMPLIANCE \
reporting using semantically enabled applications can be made possible by \
REGTECH.  the chapter notes that the FULL_BENEFITS of REGTECH will only \
materialise if the pitfalls of a fragmented tower of BABEL_APPROACH are \
avoided
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 5
Artile: Kavassalis P, 2018, J RISK FINANC, V19, P39 / an INNOVATIVE_REGTECH_APPROACH to FINANCIAL_RISK monitoring and supervisory reporting
Text:```
design/methodology/approach: in this paper, the authors propose a novel, \
REGULAR_TECHNOLOGY (REGTECH) cum automated LEGAL_TEXT_APPROACH for \
FINANCIAL_TRANSACTION as well as FINANCIAL_RISK reporting that is based \
on cutting edge distributed computing and decentralised \
DATA_MANAGEMENT_TECHNOLOGIES such as distributed ledger (swanson, 2015), \
distributed storage (arner et al.  PRACTICAL_IMPLICATIONS: the \
REGTECH_APPROACH has the potential to contain OPERATIONAL_RISK linked to \
inadequate handling of RISK_DATA and to rein in COMPLIANCE_COST of \
supervisory reporting.  ORIGINALITY_VALUE: the PRESENT_REGTECH_APPROACH \
to FINANCIAL_RISK monitoring and supervisory reporting is the first \
integration of algorithmic FINANCIAL_DATA_STANDARDS with \
BLOCKCHAIN_FUNCTIONALITY
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 6
Artile: Kurum E, 2020, J FINANC CRIME / REGTECH_SOLUTIONS and AML_COMPLIANCE: what future for FINANCIAL_CRIME?
Text:```
purpose: this STUDY_AIMS to discuss the growing use of REGTECH_SOLUTIONS \
by FINANCIAL_INSTITUTIONS to comply more efficiently with regulation in \
terms of anti MONEY_LAUNDERING COMPLIANCE and more specifically its \
influence on the evolution of FINANCIAL_CRIME in the next ten years. \
design/methodology/approach: based on two ONLINE_DELPHI_SURVEYS sent to a \
panel of INTERNATIONAL_EXPERTS composed of eight specially recruited \
professionals and specialists of anti FINANCIAL_CRIME COMPLIANCE and \
REGTECH, five MAIN_PREDICTIONS have been developed.  furthermore, the \
panel designated REGULATORS_RECOMMENDATIONS as likely to be less \
influential than REGTECH_SOLUTIONS, and the time required to integrate \
REGTECH_SOLUTIONS for AML_COMPLIANCE as the MAIN_FUTURE_CHALLENGE.  while \
the reviewed literature focused on the role of regulations on the \
evolution of MONEY_LAUNDERING, this study puts stress on \
REGTECH_SOLUTIONS and their impact on both COMPLIANCE and FINANCIAL_CRIME
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 7
Artile: Muganyi T, 2022, FINANCIAL INNOV, V8 / FINTECH, REGTECH, and FINANCIAL_DEVELOPMENT: evidence from CHINA
Text:```
we also show that the emergence of FINTECH in the area of \
FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH) can significantly \
improve FINANCIAL_DEVELOPMENT_OUTCOMES
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 8
Artile: Pantielieieva N, 2020, LECTURE NOTES DATA ENG COMMUN, V42, P1 / FINTECH, REGTECH and TRADITIONAL_FINANCIAL_INTERMEDIATION: trends and threats for FINANCIAL_STABILITY
Text:```
the PAPER_DEALS with the issues of MAIN_DIRECTIONS, challenges and \
threats of development of the newest FINANCIAL_TECHNOLOGIESFINTECH, \
REGTECH and TRADITIONAL_FINANCIAL_INTERMEDIATION.  the AUTHORS_DESCRIBE \
features of REGTECH_APPLICATION for improvement \
FINANCIAL_INTERMEDIARIES_RISK_MANAGEMENT_SYSTEMS, usage of \
INNOVATIVE_REGULATORY_TECHNOLOGY_TOOLS that can enhance the quality and \
efficiency of FINANCIAL_INSTITUTIONS_COMPLIANCE_SYSTEMS as a prerequisite \
for increasing the protection of depositors, creditors and \
INVESTORS_INTERESTS.  NEW_OPPORTUNITIES for cooperation between \
TRADITIONAL_FINANCIAL_INTERMEDIARIES and REGTECH_COMPANIES are examined
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 9
Artile: Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787 / DESIGN_CHALLENGES for GDPR_REGTECH
Text:```
in contrast, REGTECH has recently brought GREAT_SUCCESS to \
FINANCIAL_COMPLIANCE, resulting in reduced risk, COST_SAVING and enhanced \
FINANCIAL_REGULATORY_COMPLIANCE.  a PROOF_OF_CONCEPT prototype was \
explored using a regulator based SELF_ASSESSMENT checklist to establish \
if REGTECH best practice could improve the demonstration of \
GDPR_COMPLIANCE.  the application of a REGTECH_APPROACH provides \
opportunities for demonstrable and validated GDPR_COMPLIANCE, \
notwithstanding the RISK_REDUCTIONS and COST_SAVINGS that REGTECH can \
deliver.  this PAPER_DEMONSTRATES a REGTECH_APPROACH to GDPR_COMPLIANCE \
can facilitate an ORGANISATION_MEETING its ACCOUNTABILITY_OBLIGATIONS
```
<BLANKLINE>
--
<BLANKLINE>
Record-No: 10
Artile: Singh C, 2020, J MONEY LAUND CONTROL, V24, P464 / can ARTIFICIAL_INTELLIGENCE, REGTECH and CHARITYTECH provide EFFECTIVE_SOLUTIONS for ANTI_MONEY_LAUNDERING and counter terror financing initiatives in charitable fundraising
Text:```
the purpose of this paper is to explore the solutions that ai, REGTECH \
and CHARITYTECH provide to charities in navigating the VAST_AMOUNT of \
ANTI_MONEY_LAUNDERING and COUNTER_TERROR_FINANCE legislation in the uk
```
<BLANKLINE>
--
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
        phrases = pd.DataFrame(
            {
                "text": phrases.values,
                "article": phrases.index.to_list(),
            }
        )
        # phrases["text"] = (
        #     phrases["left_context"] + f" {search_for.upper()} " + phrases["right_context"]
        # )
        # phrases["article"] = phrases.index.to_list()
        # phrases = phrases[["text", "article"]]
        phrases = phrases.groupby("article").agg({"text": list})
        phrases = phrases.text.str.join(".  ")

        main_text = (
            "You are an automated scientific writer assistant. Use only the information "
            "provided in the following records to write one paragraph focusing on the "
            "any aspect contributing to the definition and characteristics of the term "
            f"'{search_for.upper()}'. Use the Record-No value between brackets "
            "to indicate the reference to the record. For example, [1] means that the "
            "information is in the Record-No 1. Use notes below of the generated text "
            "to justify the affirmation. Use only phrases appearing in the provided "
            "text. Here are the records: "
            "\n\n---\n\n"
            "Improve and make more clear the explanation of definition and "
            f"characterisitcs of the term: '{search_for.upper()}' in the next "
            "paragraphs delimited by '<<<' and '>>>', using only the information "
            "provided in the records presented below. Add cites to the added text using the "
            "corresponding Record-No value between brackets. "
            "\n\n"
            "Here are text to improve and make more clear: "
            "\n"
            "<<<\n\n\n>>>"
            "\n\n\n"
            "Here are the records: "
        )

        # paragraphs = phrases.to_list()

        return format_prompt_for_paragraphs(main_text, phrases)

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
                # print(f"-- {counter:03d} " + "-" * 83, file=file)
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
    # prompt_ = generate_prompt(frame_)
    prompt_ = generate_prompt(phrases)

    write_report(phrases, report_file)
    write_prompt_file()

    return contexts_, frame_, prompt_

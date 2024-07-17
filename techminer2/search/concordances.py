# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Concordances
=========================================================================================

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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(results.contexts_)
                                                             REGTECH to DATE has focused on the DIGITIZATION of manual REPORT >>>
<<< LD, SETS the FOUNDATION for a PRACTICAL_UNDERSTANDING of REGTECH , and proposes sequenced REFORMS that could BENEFIT REGU >>>
                                   however, the POTENTIAL of REGTECH is far greater  IT has the POTENTIAL to enable a nearly  >>>
<<< L_SYSTEMS requires increasing the USE of and RELIANCE on REGTECH 


>>> print(results.prompt_)                        
You are an automated scientific writer assistant. Use only the
information provided in the following records to write one paragraph
focusing on the any aspect contributing to the definition and
characteristics of the term:
<BLANKLINE>
'REGTECH'
<BLANKLINE>
Use the Record-No value between brackets to indicate the reference to the
record. For example, [1] means that the information is in the Record-No
1. Use notes below of the generated text to justify the affirmation. Use
only phrases appearing in the provided text.
<BLANKLINE>
Here are the records: 
<BLANKLINE>
--
<BLANKLINE>
Record-No: 1
Artile: Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373 / FINTECH, REGTECH, and the RECONCEPTUALIZATION of FINANCIAL_REGULATION
Text:```
at the JUNCTURE of these PHENOMENA lies REGULATORY_TECHNOLOGY or
REGTECHTHE_USE of TECHNOLOGY, particularly INFORMATION_TECHNOLOGY, in the
CONTEXT of regulatory MONITORING, REPORTING, and COMPLIANCE.  regulating
rapidly TRANSFORMING FINANCIAL_SYSTEMS requires increasing the USE of and
RELIANCE on REGTECH.  REGTECH_DEVELOPMENTS are leading TOWARDS a PARADIGM
SHIFT necessitating the RECONCEPTUALIZATION of FINANCIAL_REGULATION.
REGTECH to DATE has focused on the DIGITIZATION of manual REPORTING and
COMPLIANCE_PROCESSES.  however, the POTENTIAL of REGTECH is far greater
IT has the POTENTIAL to enable a nearly real_time and
PROPORTIONATE_REGULATORY_REGIME that IDENTIFIES and ADDRESSES_RISK while
facilitating more EFFICIENT_REGULATORY_COMPLIANCE.  this PAPER seeks to
expose the INADEQUACY of digitizing ANALOGUE_PROCESSES in a digital
FINANCIAL_WORLD, SETS the FOUNDATION for a PRACTICAL_UNDERSTANDING of
REGTECH, and proposes sequenced REFORMS that could BENEFIT REGULATORS,
INDUSTRY, and ENTREPRENEURS in the FINANCIAL_SECTOR and other INDUSTRIES
```
<BLANKLINE>
<BLANKLINE>


"""
import os.path
import textwrap
from dataclasses import dataclass

import pandas as pd

from ..core.read_filtered_database import read_filtered_database
from ..helpers.helper_format_prompt_for_paragraphs import helper_format_prompt_for_paragraphs

TEXTWRAP_WIDTH = 73


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
    """:meta private:"""

    records = read_filtered_database(
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
    """:meta private:"""

    def get_phrases(records):
        """Gets the phrases with the searched text."""

        records = records.set_index(pd.Index(records.article + " / " + records.document_title))

        records = records.sort_values(
            ["global_citations", "local_citations", "year"],
            ascending=[False, False, True],
        )

        records["_found_"] = records["abstract"].astype(str).str.contains(r"\b" + search_for + r"\b", regex=True)
        records = records[records["_found_"]].head(top_n)

        abstracts = records["abstract"]
        abstracts = abstracts.str.replace(";", ".").str.split(".").explode().str.strip()
        abstracts = abstracts[abstracts.map(lambda x: search_for in x)]

        return abstracts

    def create_contexts_table(phrases):
        """Extracts the contexts table."""

        regex = r"\b" + search_for + r"\b"
        contexts = phrases.str.extract(r"(?P<left_context>[\s \S]*)" + regex + r"(?P<right_context>[\s \S]*)")

        contexts["left_context"] = contexts["left_context"].fillna("")
        contexts["left_context"] = contexts["left_context"].str.strip()

        contexts["right_context"] = contexts["right_context"].fillna("")
        contexts["right_context"] = contexts["right_context"].str.strip()

        contexts = contexts[contexts["left_context"].map(lambda x: x != "") | contexts["right_context"].map(lambda x: x != "")]

        return contexts

    def transform_context_to_text(contexts):
        """Transforms the contexts table to a text."""

        contexts = contexts.copy()

        contexts["left_r"] = contexts["left_context"].str[::-1]

        contexts = contexts.sort_values(["left_r", "right_context"])

        contexts["left_context"] = contexts["left_context"].map(lambda x: "<<< " + x[-56:] if len(x) > 60 else x)
        contexts["right_context"] = contexts["right_context"].map(lambda x: x[:56] + " >>>" if len(x) > 60 else x)

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

        phrases = phrases.groupby("article").agg({"text": list})
        phrases = phrases.text.str.join(".  ")

        if phrases.shape[0] == 0:
            return None

        #
        # Main text:
        text = (
            "You are an automated scientific writer assistant. Use only the "
            "information provided in the following records to write one paragraph "
            "focusing on the any aspect contributing to the definition "
            "and characteristics of the term:"
        )
        main_text = textwrap.fill(text, width=TEXTWRAP_WIDTH)

        #
        # Term:
        main_text += f"\n\n'{search_for.upper()}'\n\n"

        #
        # Continuation main text:
        text = (
            "Use the Record-No value between brackets to indicate the reference to "
            "the record. For example, [1] means that the information is in the "
            "Record-No 1. Use notes below of the generated text to justify the "
            "affirmation. Use only phrases appearing in the provided text."
        )
        main_text += textwrap.fill(text, width=TEXTWRAP_WIDTH)
        main_text += "\n\nHere are the records: \n\n"

        #
        # Secondary text:
        text = "Improve and make more clear the explanation of definition and " "characterisitcs of the term: "
        secondary_text = textwrap.fill(text, width=TEXTWRAP_WIDTH)

        #
        # Term:
        secondary_text += f"\n\n'{search_for.upper()}'\n\n"

        text = (
            "in the next paragraphs delimited by '<<<' and '>>>', using only the "
            "information provided in the records presented below. Add cites to the "
            "added text using the corresponding Record-No value between brackets. "
        )
        secondary_text += textwrap.fill(text, width=TEXTWRAP_WIDTH)

        secondary_text += "\n\nHere are text to improve and make more clear: " "\n\n<<<\n\n>>>\n\n\n" "Here are the records:\n\n"

        return helper_format_prompt_for_paragraphs(main_text=main_text, secondary_text=secondary_text, paragraphs=phrases)

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
        phrases = phrases.str.join(".  ")

        if phrases.shape[0] == 0:
            return

        file_path = os.path.join(root_dir, "reports", report_file)
        with open(file_path, "w", encoding="utf-8") as file:
            counter = 0
            for title, phrase in zip(phrases.index, phrases):
                print("AR: ", end="", file=file)
                print(fill(title), file=file)
                print("", file=file)
                print(fill(phrase), file=file)
                print("\n", file=file)
                counter += 1

    def write_prompt_file():
        if prompt_ is None:
            return
        file_path = os.path.join(root_dir, "reports", prompt_file)
        with open(file_path, "w", encoding="utf-8") as file:
            print(prompt_, file=file)

    #
    # Main code:
    #
    phrases = get_phrases(records)
    frame_ = create_contexts_table(phrases)
    contexts_ = transform_context_to_text(frame_)
    prompt_ = generate_prompt(phrases)

    write_report(phrases, report_file)
    write_prompt_file()

    return contexts_, frame_, prompt_

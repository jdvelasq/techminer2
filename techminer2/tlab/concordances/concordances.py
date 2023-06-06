# flake8: noqa
"""
Concordances
=========================================================================================

Abstract concordances exploration tool.


>>> root_dir = "data/regtech/"

>>> from techminer2 import tlab
>>> concordances = tlab.concordances.concordances(
...     'REGTECH',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> print(concordances.contexts_)
<<< L_SYSTEMS requires increasing the use of and reliance on REGTECH 
                                                             REGTECH developments are leading towards a paradigm shift necess >>>
                                                             REGTECH to date has focused on the DIGITIZATION of manual report >>>
                                   however, the potential of REGTECH is far greater  IT has the potential to enable a nearly  >>>
<<< LD, sets the foundation for a practical understanding of REGTECH , and proposes sequenced reforms that could BENEFIT regu >>>
<<< s the promise and potential of regulatory TECHNOLOGIES ( REGTECH ), a new and vital dimension to FINTECH
<<<  five-year research programme to highlight the role that REGTECH can play in making REGULATORY_COMPLIANCE more efficient  >>>
<<< emantically enabled applications can be made possible by REGTECH 
                 the chapter notes that the full BENEFITS of REGTECH will only materialise if the pitfalls of a fragmented to >>>
           although also not a panacea, the development of " REGTECH " solutions will help clear away volumes of work that un >>>
                                                             REGTECH will not eliminate policy considerations, nor will IT re >>>
                 nevertheless, a sophisticated deployment of REGTECH should help focus regulatory discretion and public-polic >>>
                                             europes road to REGTECH has rested upon four apparently unrelated pillars: (1) e >>>
<<< that together they are underpinning the development of a REGTECH ecosystem in EUROPE and will continue to do so
<<< and regulators, and provided an environment within which REGTECH can flourish
<<< ide insights for other societies in developing their own REGTECH ECOSYSTEMS in order to support more efficient, stable, i >>>
<<< paper, the authors propose a novel, regular TECHNOLOGY ( REGTECH ) cum automated legal text approach for financial TRANSA >>>
<<< rpose of this paper is to explore the solutions that ai, REGTECH and charitytech provide to charities in navigating the v >>>
<<< the area of FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH ) can significantly improve FINANCIAL_DEVELOPMENT outcomes
                                                in contrast, REGTECH has recently brought GREAT_SUCCESS to FINANCIAL_COMPLIAN >>>
<<< egulator based SELF-ASSESSMENT_CHECKLIST to establish if REGTECH best practice could improve the demonstration of GDPR_CO >>>
<<< otwithstanding the RISK_REDUCTIONS and COST_SAVINGS that REGTECH can deliver
<<< llustrate the impact of adopting REGULATORY_TECHNOLOGY ( REGTECH ) INNOVATIONS in BANKS on MONEY_LAUNDERING prevention ef >>>
<<< ING through REGTECH and cost- and time-saving aspects of REGTECH , drive MONEY_LAUNDERING prevention effectiveness to a h >>>
<<< ral awareness concerning the adoption and integration of REGTECH platforms for fighting MONEY_LAUNDERING
                     2020 the authorsregulatory TECHNOLOGY ( REGTECH )
                                     REGULATORY_TECHNOLOGY ( REGTECH ) is an emerging TECHNOLOGY trend leveraging INFORMATION >>>
                                 an option is to incorporate REGTECH into the DIGITAL_TRANSFORMATION STRATEGY of a management >>>
                                                             REGTECH can provide an invaluable tool, in a BUSINESS-as-usual e >>>
                        this paper explores the potential of REGTECH and the merit of incorporating IT into a smart treasury  >>>

                        

>>> print(concordances.prompt_)                        
Write a clear and concise paragraph of 30 words about 'REGTECH' using the following bullets:
<BLANKLINE>
* regulating rapidly transforming FINANCIAL_SYSTEMS requires increasing the use of and reliance on REGTECH 
<BLANKLINE>
*  REGTECH developments are leading towards a paradigm shift necessitating the reconceptualization of FINANCIAL_REGULATION
<BLANKLINE>
*  REGTECH to date has focused on the DIGITIZATION of manual reporting and COMPLIANCE_PROCESSES
<BLANKLINE>
* however, the potential of REGTECH is far greater  IT has the potential to enable a nearly real-time and PROPORTIONATE_REGULATORY_REGIME that identifies and ADDRESSES_RISK while facilitating more EFFICIENT_REGULATORY_COMPLIANCE
<BLANKLINE>
* this paper seeks to expose the inadequacy of digitizing ANALOGUE_PROCESSES in a digital FINANCIAL_WORLD, sets the foundation for a practical understanding of REGTECH , and proposes sequenced reforms that could BENEFIT regulators, industry, and entrepreneurs in the FINANCIAL_SECTOR and other industries
<BLANKLINE>
* this chapter explores the promise and potential of regulatory TECHNOLOGIES ( REGTECH ), a new and vital dimension to FINTECH
<BLANKLINE>
* IT draws on the findings and outcomes of a five-year research programme to highlight the role that REGTECH can play in making REGULATORY_COMPLIANCE more efficient and effective
<BLANKLINE>
* the chapter presents research on the bank of england/financial conduct authority (fca) REGTECH sprint initiative, whose objective was to demonstrate how straight-through processing of REGULATIONS and REGULATORY_COMPLIANCE reporting using semantically enabled applications can be made possible by REGTECH 
<BLANKLINE>
* the chapter notes that the full BENEFITS of REGTECH will only materialise if the pitfalls of a fragmented tower of babel approach are avoided
<BLANKLINE>
* although also not a panacea, the development of " REGTECH " solutions will help clear away volumes of work that understaffed and underfunded regulators cannot keep up with
<BLANKLINE>
*  REGTECH will not eliminate policy considerations, nor will IT render regulatory decisions noncontroversial
<BLANKLINE>
* nevertheless, a sophisticated deployment of REGTECH should help focus regulatory discretion and public-policy debate on the elements of REGULATION where choices really matter
<BLANKLINE>
* europes road to REGTECH has rested upon four apparently unrelated pillars: (1) extensive reporting requirements imposed after the GLOBAL_FINANCIAL_CRISIS to control SYSTEMIC_RISK and change in FINANCIAL_SECTOR behaviour
<BLANKLINE>
* the PAPER_ANALYSES these four pillars and suggests that together they are underpinning the development of a REGTECH ecosystem in EUROPE and will continue to do so
<BLANKLINE>
* we argue that the european unions FINANCIAL_SERVICES and DATA_PROTECTION regulatory reforms have unintentionally driven the use of regulatory TECHNOLOGIES (REGTECH) by intermediaries, supervisors and regulators, and provided an environment within which REGTECH can flourish
<BLANKLINE>
* the experiences of EUROPE in this process will provide insights for other societies in developing their own REGTECH ECOSYSTEMS in order to support more efficient, stable, inclusive FINANCIAL_SYSTEMS
<BLANKLINE>
* DESIGN/METHODOLOGY/APPROACH: in this paper, the authors propose a novel, regular TECHNOLOGY ( REGTECH ) cum automated legal text approach for financial TRANSACTION as well as FINANCIAL_RISK reporting that is based on cutting-edge distributed computing and decentralised data management TECHNOLOGIES such as DISTRIBUTED_LEDGER (swanson, 2015), distributed storage (arner et al
<BLANKLINE>
* the purpose of this paper is to explore the solutions that ai, REGTECH and charitytech provide to charities in navigating the vast amount of ANTI-MONEY_LAUNDERING and counter-terror FINANCE legislation in the uk
<BLANKLINE>
* we also show that the emergence of FINTECH in the area of FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH ) can significantly improve FINANCIAL_DEVELOPMENT outcomes
<BLANKLINE>
* in contrast, REGTECH has recently brought GREAT_SUCCESS to FINANCIAL_COMPLIANCE, resulting in reduced RISK, COST_SAVING and enhanced FINANCIAL_REGULATORY_COMPLIANCE
<BLANKLINE>
* a PROOF_OF_CONCEPT prototype was explored using a regulator based SELF-ASSESSMENT_CHECKLIST to establish if REGTECH best practice could improve the demonstration of GDPR_COMPLIANCE
<BLANKLINE>
* the application of a REGTECH_APPROACH provides OPPORTUNITIES for demonstrable and validated GDPR_COMPLIANCE, notwithstanding the RISK_REDUCTIONS and COST_SAVINGS that REGTECH can deliver
<BLANKLINE>
* this STUDY_AIMS to illustrate the impact of adopting REGULATORY_TECHNOLOGY ( REGTECH ) INNOVATIONS in BANKS on MONEY_LAUNDERING prevention effectiveness using BAHRAIN as a CASE_STUDY
<BLANKLINE>
* the results of MULTIVARIATE_ANALYSIS indicate that transactions MONITORING through REGTECH and cost- and time-saving aspects of REGTECH , drive MONEY_LAUNDERING prevention effectiveness to a highly statistically significant extent
<BLANKLINE>
* this research not only sheds light on the efficacy of REGTECH but also raises general awareness concerning the adoption and integration of REGTECH platforms for fighting MONEY_LAUNDERING
<BLANKLINE>
* 2020 the authorsregulatory TECHNOLOGY ( REGTECH )
<BLANKLINE>
* REGULATORY_TECHNOLOGY ( REGTECH ) is an emerging TECHNOLOGY trend leveraging INFORMATION_TECHNOLOGY and DIGITAL_INNOVATIONS that can greatly assist with a BANKS regulatory management process
<BLANKLINE>
* an option is to incorporate REGTECH into the DIGITAL_TRANSFORMATION STRATEGY of a management function such as treasury
<BLANKLINE>
*  REGTECH can provide an invaluable tool, in a BUSINESS-as-usual environment, as well as in real-life stress events, such as the recent coronavirus outbreak
<BLANKLINE>
* this paper explores the potential of REGTECH and the merit of incorporating IT into a smart treasury department
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
# import os.path
# import textwrap

from ...classes import Concordances
from ...record_utils import read_records


# pylint: disable=too-many-arguments
def concordances(
    search_for,
    top_n=50,
    root_dir="./",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    def get_phrases():
        """Gets the phrases with the searched text."""

        records = read_records(
            root_dir=root_dir,
            database="documents",
            year_filter=year_filter,
            cited_by_filter=cited_by_filter,
            **filters,
        )

        records = records.sort_values(
            ["global_citations", "local_citations", "year"],
            ascending=[False, False, True],
        )

        records["_found_"] = (
            records["abstract"]
            .astype(str)
            .str.contains(r"\b" + search_for + r"\b", regex=True)
        )
        records = records[records["_found_"]].head(top_n)

        abstracts = records["abstract"]
        abstracts = (
            abstracts.str.replace(";", ".")
            .str.split(".")
            .explode()
            .str.strip()
        )
        abstracts = abstracts[abstracts.map(lambda x: search_for in x)]

        return abstracts

    def create_contexts_table(phrases):
        """Extracts the contexts table."""

        regex = r"\b" + search_for + r"\b"
        contexts = phrases.str.extract(
            r"(?P<left_context>[\s \S]*)"
            + regex
            + r"(?P<right_context>[\s \S]*)"
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

    def _select_abstracts(abstracts, text):
        """Selects the abstracts."""

        regex = r"\b" + text + r"\b"
        abstracts = abstracts[abstracts.phrase.str.contains(regex, regex=True)]
        abstracts["phrase"] = abstracts["phrase"].str.capitalize()
        abstracts["phrase"] = abstracts["phrase"].str.replace(
            r"\b" + text + r"\b", text.upper(), regex=True
        )
        abstracts["phrase"] = abstracts["phrase"].str.replace(
            r"\b" + text.capitalize() + r"\b", text.upper(), regex=True
        )

        return abstracts

    # def fill(text):
    #     if isinstance(text, str):
    #         return textwrap.fill(
    #             text,
    #             width=87,
    #             initial_indent=" " * 0,
    #             subsequent_indent=" " * 3,
    #             fix_sentence_endings=True,
    #         )
    #     else:
    #         return ""

    def generate_chatgpt_prompt(contexts_table):
        """Generates the chatgpt prompt."""

        text = (
            "Write a clear and concise paragraph of 30 words about "
            f"'{search_for}' using the following bullets:\n\n"
        )

        for _, row in contexts_table.iterrows():
            text += (
                "* "
                + row["left_context"]
                + " "
                + search_for.upper()
                + " "
                + row["right_context"]
                + "\n\n"
            )

        return text

    #
    # Main code:
    #
    phrases = get_phrases()
    contexts_table = create_contexts_table(phrases)
    texts = transform_context_to_text(contexts_table)

    obj = Concordances()
    obj.contexts_ = texts
    obj.table_ = contexts_table.copy()
    obj.prompt_ = generate_chatgpt_prompt(contexts_table)

    return obj

    # file_path = os.path.join(root_dir, "reports", "concordances.txt")
    # with open(file_path, "w", encoding="utf-8") as file:
    #     counter = 0
    #     for abstract in abstracts:
    #         print("-- {:03d} ".format(counter) + "-" * 83, file=file)
    #         print("AR ", end="", file=file)
    #         print(fill(abstract), file=file)
    #         print(fill(row.phrase), file=file)
    #         print("\n", file=file)
    #         counter += 1

    # ###

    # abstracts = load_abstracts(root_dir)
    # abstracts = abstracts[abstracts.article.isin(records.article)]
    # abstracts = abstracts.sort_values(
    #     ["global_citations", "article", "line_no"],
    #     ascending=[False, True, True],
    # )
    # abstracts = _select_abstracts(abstracts, search_for)

    # _write_report(root_dir, abstracts, year_filter, cited_by_filter, **filters)

    # if not quiet:
    #     abstracts = abstracts.head(top_n)
    #     contexts = _extract_contexts(abstracts, search_for)
    #     _print_concordances(contexts, search_for)


# def _write_report(directory, abstracts, start_year, end_year, **filters):
#     abstracts = abstracts.copy()
#     abstracts = abstracts[["global_citations", "article", "phrase"]]
#     abstracts = abstracts.groupby(["article"], as_index=False).agg(list)
#     abstracts["phrase"] = abstracts["phrase"].str.join("  ")
#     abstracts["global_citations"] = abstracts["global_citations"].map(max)
#     abstracts = abstracts.sort_values("global_citations", ascending=False)

#     records = read_records(
#         root_dir=directory,
#         database="documents",
#         start_year=start_year,
#         end_year=end_year,
#         **filters,
#     )
#     records.index = records.article
#     abstracts.index = abstracts.article
#     abstracts["title"] = records.loc[abstracts.article, "title"]

#     file_name = os.path.join(directory, "reports", "concordances.txt")
#     with open(file_name, "w", encoding="utf-8") as out_file:
#         counter = 0

#         for _, row in abstracts.iterrows():
#             print("-- {:03d} ".format(counter) + "-" * 83, file=out_file)
#             print("AR ", end="", file=out_file)
#             print(_fill(row["article"]), file=out_file)
#             print("TI ", end="", file=out_file)
#             print(_fill(row["title"]), file=out_file)
#             print("TC ", end="", file=out_file)
#             print(str(row.global_citations), file=out_file)
#             print("AB ", end="", file=out_file)
#             print(_fill(row.phrase), file=out_file)
#             print("\n", file=out_file)

#             counter += 1

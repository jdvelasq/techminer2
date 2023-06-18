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
<<< l systems requires increasing the use of and reliance on REGTECH 
                                                             REGTECH developments are leading towards a paradigm shift necess >>>
                                                             REGTECH to date has focused on the DIGITIZATION of manual REPORT >>>
                                   however, the potential of REGTECH is far greater  IT has the potential to enable a nearly  >>>
<<< ld, sets the foundation for a practical understanding of REGTECH , and proposes sequenced reforms that could BENEFIT regu >>>
<<< s the promise and potential of REGULATORY_TECHNOLOGIES ( REGTECH ), a new and vital dimension to FINTECH
<<<  five-year research programme to highlight the role that REGTECH can play in making REGULATORY_COMPLIANCE more efficient  >>>
<<< emantically enabled applications can be made possible by REGTECH 
                 the chapter notes that the full BENEFITS of REGTECH will only materialise if the pitfalls of a fragmented to >>>
           although also not a panacea, the DEVELOPMENT of " REGTECH " solutions will help clear away volumes of work that un >>>
                                                             REGTECH will not eliminate policy considerations, nor will IT re >>>
                 nevertheless, a sophisticated deployment of REGTECH should help focus regulatory discretion and PUBLIC_POLIC >>>
                                             europes road to REGTECH has rested upon four apparently unrelated pillars: (1) e >>>
<<< that together they are underpinning the DEVELOPMENT of a REGTECH ECOSYSTEM in EUROPE and will continue to do so
<<< and regulators, and provided an ENVIRONMENT within which REGTECH can flourish
<<< ide insights for other societies in developing their own REGTECH ECOSYSTEMS in order to support more efficient, stable, i >>>
<<< paper, the authors propose a novel, regular TECHNOLOGY ( REGTECH ) cum automated legal text approach for financial TRANSA >>>
<<< rpose of this paper is to explore the solutions that AI, REGTECH and CHARITYTECH provide to charities in navigating the v >>>
<<< the area of FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH ) can significantly improve FINANCIAL_DEVELOPMENT outcomes
                                                in contrast, REGTECH has recently brought great SUCCESS to financial COMPLIAN >>>
<<< egulator based SELF_ASSESSMENT checklist to establish if REGTECH best practice could improve the demonstration of GDPR_CO >>>
<<< otwithstanding the RISK_REDUCTIONS and cost savings that REGTECH can deliver
<<< llustrate the impact of adopting REGULATORY_TECHNOLOGY ( REGTECH ) INNOVATIONS in BANKS on MONEY_LAUNDERING prevention ef >>>
<<< ING through REGTECH and cost  and time-saving aspects of REGTECH , drive MONEY_LAUNDERING prevention effectiveness to a h >>>
<<< ral awareness concerning the ADOPTION and integration of REGTECH PLATFORMS for fighting MONEY_LAUNDERING
<<< ndings provide specific insights about the deployment of REGTECH capabilities in BANKS in regional BANKING centers of mod >>>
                     2020 the authorsregulatory TECHNOLOGY ( REGTECH )
                                     REGULATORY_TECHNOLOGY ( REGTECH ) is an emerging TECHNOLOGY trend leveraging INFORMATION >>>
                                 an option is to incorporate REGTECH into the DIGITAL_TRANSFORMATION STRATEGY of a MANAGEMENT >>>
                                                             REGTECH can provide an invaluable tool, in a BUSINESS as usual E >>>
                        this paper explores the potential of REGTECH and the merit of incorporating IT into a SMART_TREASURY  >>>



>>> print(concordances.prompt_)                        
Your task is to generate a short summary of a term for a research \\
paper. Summarize the text below, delimited by triple backticks, \\
in at most 30 words, focusing on the any aspect contributing \\
to the definition and characteristics of the term 'REGTECH'.
<BLANKLINE>
Text: ```regulating rapidly transforming financial systems requires increasing \\
the use of and reliance on 'REGTECH' .  'REGTECH' developments are \\
leading towards a paradigm shift necessitating the reconceptualization \\
of FINANCIAL_REGULATION.  'REGTECH' to date has focused on the \\
DIGITIZATION of manual REPORTING and COMPLIANCE processes. however, \\
the potential of 'REGTECH' is far greater  IT has the potential to \\
enable a nearly real-time and proportionate REGULATORY_REGIME that \\
identifies and addresses RISK while facilitating more efficient \\
REGULATORY_COMPLIANCE. this paper seeks to expose the inadequacy of \\
digitizing analogue processes in a digital financial world, sets the \\
foundation for a practical understanding of 'REGTECH' , and proposes \\
sequenced reforms that could BENEFIT regulators, industry, and \\
entrepreneurs in the FINANCIAL_SECTOR and other industries. this \\
chapter explores the promise and potential of REGULATORY_TECHNOLOGIES \\
( 'REGTECH' ), a new and vital dimension to FINTECH. IT draws on the \\
findings and outcomes of a five-year research programme to highlight \\
the role that 'REGTECH' can play in making REGULATORY_COMPLIANCE more \\
efficient and effective. the chapter presents research on the BANK of \\
england/financial conduct authority (fca) REGTECH sprint initiative, \\
whose objective was to demonstrate how straight-through processing of \\
REGULATIONS and REGULATORY_COMPLIANCE REPORTING using semantically \\
enabled applications can be made possible by 'REGTECH' . the chapter \\
notes that the full BENEFITS of 'REGTECH' will only materialise if the \\
pitfalls of a fragmented tower of babel approach are avoided. although \\
also not a panacea, the DEVELOPMENT of " 'REGTECH' " solutions will \\
help clear away volumes of work that understaffed and underfunded \\
regulators cannot keep up with.  'REGTECH' will not eliminate policy \\
considerations, nor will IT render regulatory decisions \\
noncontroversial. nevertheless, a sophisticated deployment of \\
'REGTECH' should help focus regulatory discretion and PUBLIC_POLICY \\
debate on the elements of REGULATION where choices really matter. \\
europes road to 'REGTECH' has rested upon four apparently unrelated \\
pillars: (1) extensive REPORTING requirements imposed after the \\
GLOBAL_FINANCIAL_CRISIS to control SYSTEMIC_RISK and change in \\
FINANCIAL_SECTOR behaviour. the paper analyses these four pillars and \\
suggests that together they are underpinning the DEVELOPMENT of a \\
'REGTECH' ECOSYSTEM in EUROPE and will continue to do so. we argue \\
that the european unions FINANCIAL_SERVICES and DATA_PROTECTION \\
regulatory reforms have unintentionally driven the use of \\
REGULATORY_TECHNOLOGIES (REGTECH) by intermediaries, supervisors and \\
regulators, and provided an ENVIRONMENT within which 'REGTECH' can \\
flourish. the experiences of EUROPE in this process will provide \\
insights for other societies in developing their own 'REGTECH' \\
ECOSYSTEMS in order to support more efficient, stable, inclusive \\
financial systems. design/methodology/approach: in this paper, the \\
authors propose a novel, regular TECHNOLOGY ( 'REGTECH' ) cum \\
automated legal text approach for financial TRANSACTION as well as \\
FINANCIAL_RISK REPORTING that is based on cutting-edge distributed \\
computing and decentralised DATA_MANAGEMENT TECHNOLOGIES such as \\
DISTRIBUTED_LEDGER (swanson, 2015), distributed storage (arner et al. \\
the purpose of this paper is to explore the solutions that AI, \\
'REGTECH' and CHARITYTECH provide to charities in navigating the vast \\
amount of ANTI_MONEY_LAUNDERING and COUNTER_TERROR_FINANCE legislation \\
in the uk. we also show that the emergence of FINTECH in the area of \\
FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: 'REGTECH' ) can \\
significantly improve FINANCIAL_DEVELOPMENT outcomes. in contrast, \\
'REGTECH' has recently brought great SUCCESS to financial COMPLIANCE, \\
resulting in reduced RISK, COST_SAVING and enhanced financial \\
REGULATORY_COMPLIANCE. a PROOF_OF_CONCEPT prototype was explored using \\
a regulator based SELF_ASSESSMENT checklist to establish if 'REGTECH' \\
best practice could improve the demonstration of GDPR_COMPLIANCE. the \\
application of a REGTECH_APPROACH provides OPPORTUNITIES for \\
demonstrable and validated GDPR_COMPLIANCE, notwithstanding the \\
RISK_REDUCTIONS and cost savings that 'REGTECH' can deliver. this \\
study aims to illustrate the impact of adopting REGULATORY_TECHNOLOGY \\
( 'REGTECH' ) INNOVATIONS in BANKS on MONEY_LAUNDERING prevention \\
effectiveness using BAHRAIN as a CASE_STUDY. the results of \\
MULTIVARIATE_ANALYSIS indicate that transactions MONITORING through \\
REGTECH and cost  and time-saving aspects of 'REGTECH' , drive \\
MONEY_LAUNDERING prevention effectiveness to a highly statistically \\
significant extent. this research not only sheds light on the efficacy \\
of REGTECH but also raises general awareness concerning the ADOPTION \\
and integration of 'REGTECH' PLATFORMS for fighting MONEY_LAUNDERING. \\
in particular, the findings provide specific insights about the \\
deployment of 'REGTECH' capabilities in BANKS in regional BANKING \\
centers of modest scale. 2020 the authorsregulatory TECHNOLOGY ( \\
'REGTECH' ). REGULATORY_TECHNOLOGY ( 'REGTECH' ) is an emerging \\
TECHNOLOGY trend leveraging INFORMATION_TECHNOLOGY and \\
DIGITAL_INNOVATIONS that can greatly assist with a BANKS regulatory \\
MANAGEMENT process. an option is to incorporate 'REGTECH' into the \\
DIGITAL_TRANSFORMATION STRATEGY of a MANAGEMENT function such as \\
treasury.  'REGTECH' can provide an invaluable tool, in a BUSINESS as \\
usual ENVIRONMENT, as well as in real-life stress events, such as the \\
recent CORONAVIRUS outbreak. this paper explores the potential of \\
'REGTECH' and the merit of incorporating IT into a SMART_TREASURY \\
department.```
<BLANKLINE>

# pylint: disable=line-too-long
"""
# import os.path
# import textwrap

# from ..classes import Concordances
# from ..records import read_records


# # pylint: disable=too-many-arguments
# def concordances(
#     search_for,
#     top_n=100,
#     report_file="concordances_report.txt",
#     prompt_file="concordances_prompt.txt",
#     # Database params:
#     root_dir="./",
#     database="main",
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """Checks the occurrence contexts of a given text in the abstract's phrases."""

#     def get_phrases():
#         """Gets the phrases with the searched text."""

#         records = read_records(
#             root_dir=root_dir,
#             database=database,
#             year_filter=year_filter,
#             cited_by_filter=cited_by_filter,
#             **filters,
#         )
#         records.index = records.article + " / " + records.title

#         records = records.sort_values(
#             ["global_citations", "local_citations", "year"],
#             ascending=[False, False, True],
#         )

#         records["_found_"] = (
#             records["abstract"]
#             .astype(str)
#             .str.contains(r"\b" + search_for + r"\b", regex=True)
#         )
#         records = records[records["_found_"]].head(top_n)

#         abstracts = records["abstract"]
#         abstracts = (
#             abstracts.str.replace(";", ".")
#             .str.split(".")
#             .explode()
#             .str.strip()
#         )
#         abstracts = abstracts[abstracts.map(lambda x: search_for in x)]

#         return abstracts

#     def create_contexts_table(phrases):
#         """Extracts the contexts table."""

#         regex = r"\b" + search_for + r"\b"
#         contexts = phrases.str.extract(
#             r"(?P<left_context>[\s \S]*)"
#             + regex
#             + r"(?P<right_context>[\s \S]*)"
#         )

#         contexts["left_context"] = contexts["left_context"].fillna("")
#         contexts["left_context"] = contexts["left_context"].str.strip()

#         contexts["right_context"] = contexts["right_context"].fillna("")
#         contexts["right_context"] = contexts["right_context"].str.strip()

#         contexts = contexts[
#             contexts["left_context"].map(lambda x: x != "")
#             | contexts["right_context"].map(lambda x: x != "")
#         ]

#         return contexts

#     def transform_context_to_text(contexts):
#         """Transforms the contexts table to a text."""

#         contexts = contexts.copy()
#         contexts["left_context"] = contexts["left_context"].map(
#             lambda x: "<<< " + x[-56:] if len(x) > 60 else x
#         )
#         contexts["right_context"] = contexts["right_context"].map(
#             lambda x: x[:56] + " >>>" if len(x) > 60 else x
#         )

#         texts = []
#         for _, row in contexts.iterrows():
#             text = f"{row['left_context']:>60} {search_for.upper()} {row['right_context']}"
#             texts.append(text)

#         return "\n".join(texts)

#     def generate_chatgpt_prompt(contexts_table):
#         """Generates the chatgpt prompt."""

#         text_to_summarize = ""

#         for _, row in contexts_table.iterrows():
#             left = row["left_context"]
#             right = row["right_context"]
#             text_to_summarize += f"{left} '{search_for.upper()}' {right}. "

#         text_to_summarize = textwrap.fill(text_to_summarize, width=70).replace(
#             "\n", " \\\n"
#         )

#         text = (
#             "Your task is to generate a short summary of a term for a research \\\n"
#             "paper. Summarize the text below, delimited by triple backticks, \\\n"
#             "in at most 30 words, focusing on the any aspect contributing \\\n"
#             f"to the definition and characteristics of the term '{search_for}'.\n\n"
#             f"Text: ```{text_to_summarize}```\n"
#         )

#         return text

#     def fill(text):
#         if isinstance(text, str):
#             return textwrap.fill(
#                 text,
#                 width=87,
#                 initial_indent=" " * 0,
#                 subsequent_indent=" " * 0,
#                 fix_sentence_endings=True,
#             )
#         else:
#             return ""

#     def write_report(phrases, report_file):
#         """Writes the report."""

#         phrases = phrases.copy()
#         phrases = phrases.to_frame()
#         phrases["doc"] = phrases.index
#         phrases = phrases.groupby("doc")["abstract"].apply(list)
#         phrases = phrases.map(lambda x: ".  ".join(x))

#         file_path = os.path.join(root_dir, "reports", report_file)
#         with open(file_path, "w", encoding="utf-8") as file:
#             counter = 0
#             for title, phrase in zip(phrases.index, phrases):
#                 print("-- {:03d} ".format(counter) + "-" * 83, file=file)
#                 print("AR: ", end="", file=file)
#                 print(fill(title), file=file)
#                 print("", file=file)
#                 print(fill(phrase), file=file)
#                 print("\n", file=file)
#                 counter += 1

#     def write_prompt(text, prompt_file):
#         file_path = os.path.join(root_dir, "reports", prompt_file)
#         with open(file_path, "w", encoding="utf-8") as file:
#             print(text, file=file)

#     #
#     # Main code:
#     #
#     phrases = get_phrases()
#     contexts_table = create_contexts_table(phrases)
#     texts = transform_context_to_text(contexts_table)
#     write_report(phrases, report_file)

#     obj = Concordances()
#     obj.contexts_ = texts
#     obj.table_ = contexts_table.copy()
#     obj.prompt_ = generate_chatgpt_prompt(contexts_table)

#     write_prompt(obj.prompt_, prompt_file)

#     return obj

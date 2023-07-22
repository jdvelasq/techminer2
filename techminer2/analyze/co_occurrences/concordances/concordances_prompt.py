# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _concordances_prompt:

Concordances Prompt
=========================================================================================

Abstract concordances exploration prompt.


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> prompt = tm2p.concordances_prompt(
...     search_for='REGTECH',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> print(prompt)
Your task is to generate a short summary of a term for a research paper. \\
Summarize the paragraphs below, delimited by triple backticks, in one \\
unique paragraph, in at most 30 words, focusing on the any aspect \\
contributing to the definition and characteristics of the term 'REGTECH'.
<BLANKLINE>
Paragraph 1:
```
regulating rapidly transforming financial systems requires increasing the \\
use of and reliance on REGTECH.  REGTECH developments are leading towards a \\
paradigm shift necessitating the reconceptualization of \\
FINANCIAL_REGULATION.  REGTECH to date has focused on the DIGITIZATION of \\
manual REPORTING and COMPLIANCE processes.  however, the potential of \\
REGTECH is far greater  IT has the potential to enable a nearly real-time \\
and proportionate REGULATORY_REGIME that identifies and addresses RISK \\
while facilitating more efficient REGULATORY_COMPLIANCE.  this paper seeks \\
to expose the inadequacy of digitizing analogue processes in a digital \\
financial world, sets the foundation for a practical understanding of \\
REGTECH, and proposes sequenced reforms that could BENEFIT regulators, \\
industry, and entrepreneurs in the FINANCIAL_SECTOR and other industries
```
<BLANKLINE>
Paragraph 2:
```
although also not a panacea, the DEVELOPMENT of "REGTECH" solutions will \\
help clear away volumes of work that understaffed and underfunded \\
regulators cannot keep up with.  REGTECH will not eliminate policy \\
considerations, nor will IT render regulatory decisions noncontroversial. \\
nevertheless, a sophisticated deployment of REGTECH should help focus \\
regulatory discretion and PUBLIC_POLICY debate on the elements of \\
REGULATION where choices really matter
```
<BLANKLINE>
Paragraph 3:
```
europes road to REGTECH has rested upon four apparently unrelated pillars: \\
(1) extensive REPORTING requirements imposed after the \\
GLOBAL_FINANCIAL_CRISIS to control SYSTEMIC_RISK and change in \\
FINANCIAL_SECTOR behaviour.  the paper analyses these four pillars and \\
suggests that together they are underpinning the DEVELOPMENT of a REGTECH \\
ECOSYSTEM in EUROPE and will continue to do so.  we argue that the european \\
unions FINANCIAL_SERVICES and DATA_PROTECTION regulatory reforms have \\
unintentionally driven the use of REGULATORY_TECHNOLOGIES (REGTECH) by \\
intermediaries, supervisors and regulators, and provided an ENVIRONMENT \\
within which REGTECH can flourish.  the experiences of EUROPE in this \\
process will provide insights for other societies in developing their own \\
REGTECH ECOSYSTEMS in order to support more efficient, stable, inclusive \\
financial systems
```
<BLANKLINE>
Paragraph 4:
```
this chapter explores the promise and potential of REGULATORY_TECHNOLOGIES \\
(REGTECH), a new and vital dimension to FINTECH.  IT draws on the findings \\
and outcomes of a five-year research programme to highlight the role that \\
REGTECH can play in making REGULATORY_COMPLIANCE more efficient and \\
effective.  the chapter presents research on the BANK of england/financial \\
conduct authority (fca) REGTECH sprint initiative, whose objective was to \\
demonstrate how straight-through processing of REGULATIONS and \\
REGULATORY_COMPLIANCE REPORTING using semantically enabled applications can \\
be made possible by REGTECH.  the chapter notes that the full BENEFITS of \\
REGTECH will only materialise if the pitfalls of a fragmented tower of \\
babel approach are avoided
```
<BLANKLINE>
Paragraph 5:
```
design/methodology/approach: in this paper, the authors propose a novel, \\
regular TECHNOLOGY (REGTECH) cum automated legal text approach for \\
financial TRANSACTION as well as FINANCIAL_RISK REPORTING that is based on \\
cutting-edge distributed computing and decentralised DATA_MANAGEMENT \\
TECHNOLOGIES such as DISTRIBUTED_LEDGER (swanson, 2015), distributed \\
storage (arner et al.  practical implications: the REGTECH_APPROACH has the \\
potential to contain OPERATIONAL_RISK linked to inadequate handling of RISK \\
DATA and to rein in COMPLIANCE cost of supervisory REPORTING.  originality \\
value: the present REGTECH_APPROACH to FINANCIAL_RISK MONITORING and \\
supervisory REPORTING is the first integration of algorithmic \\
FINANCIAL_DATA STANDARDS with BLOCKCHAIN functionality
```
<BLANKLINE>
Paragraph 6:
```
we also show that the emergence of FINTECH in the area of \\
FINANCIAL_REGULATION (REGULATORY_TECHNOLOGY: REGTECH) can significantly \\
improve FINANCIAL_DEVELOPMENT outcomes
```
<BLANKLINE>
Paragraph 7:
```
in contrast, REGTECH has recently brought great SUCCESS to financial \\
COMPLIANCE, resulting in reduced RISK, COST_SAVING and enhanced financial \\
REGULATORY_COMPLIANCE.  a PROOF_OF_CONCEPT prototype was explored using a \\
regulator based SELF_ASSESSMENT checklist to establish if REGTECH best \\
practice could improve the demonstration of GDPR_COMPLIANCE.  the \\
application of a REGTECH_APPROACH provides OPPORTUNITIES for demonstrable \\
and validated GDPR_COMPLIANCE, notwithstanding the RISK_REDUCTIONS and cost \\
savings that REGTECH can deliver.  this paper demonstrates a \\
REGTECH_APPROACH to GDPR_COMPLIANCE can facilitate an organisation meeting \\
its ACCOUNTABILITY obligations
```
<BLANKLINE>
Paragraph 8:
```
the purpose of this paper is to explore the solutions that AI, REGTECH and \\
CHARITYTECH provide to charities in navigating the vast amount of \\
ANTI_MONEY_LAUNDERING and COUNTER_TERROR_FINANCE legislation in the uk
```
<BLANKLINE>
Paragraph 9:
```
this study aims to illustrate the impact of adopting REGULATORY_TECHNOLOGY \\
(REGTECH) INNOVATIONS in BANKS on MONEY_LAUNDERING prevention effectiveness \\
using BAHRAIN as a CASE_STUDY.  the results of MULTIVARIATE_ANALYSIS \\
indicate that transactions MONITORING through REGTECH and cost  and time- \\
saving aspects of REGTECH, drive MONEY_LAUNDERING prevention effectiveness \\
to a highly statistically significant extent.  this research not only sheds \\
light on the efficacy of REGTECH but also raises general awareness \\
concerning the ADOPTION and integration of REGTECH PLATFORMS for fighting \\
MONEY_LAUNDERING.  in particular, the findings provide specific insights \\
about the deployment of REGTECH capabilities in BANKS in regional BANKING \\
centers of modest scale.  2020 the authorsregulatory TECHNOLOGY (REGTECH)
```
<BLANKLINE>
Paragraph 10:
```
REGULATORY_TECHNOLOGY (REGTECH) is an emerging TECHNOLOGY trend leveraging \\
INFORMATION_TECHNOLOGY and DIGITAL_INNOVATIONS that can greatly assist with \\
a BANKS regulatory MANAGEMENT process.  an option is to incorporate REGTECH \\
into the DIGITAL_TRANSFORMATION STRATEGY of a MANAGEMENT function such as \\
treasury.  REGTECH can provide an invaluable tool, in a BUSINESS as usual \\
ENVIRONMENT, as well as in real-life stress events, such as the recent \\
CORONAVIRUS outbreak.  this paper explores the potential of REGTECH and the \\
merit of incorporating IT into a SMART_TREASURY department
```
<BLANKLINE>
<BLANKLINE>

"""
from ...._read_records import read_records
from .concordances_prompt_from_records import concordances_prompt_from_records


def concordances_prompt(
    #
    # FUNCTION PARAMS:
    search_for: str,
    top_n: int,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    #
    # MAIN CODE:
    #
    records = read_records(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return concordances_prompt_from_records(search_for=search_for, top_n=top_n, records=records)

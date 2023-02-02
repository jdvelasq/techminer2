"""
Record View
===============================================================================

VantagePoint / Record View

>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.record_view(
...     criterion='author_keywords',
...     search_for='regtech',
...     records_length=2,
...     directory=directory,
... )
AR Anagnostopoulos I, 2018, J ECON BUS, V100, P7
TI Fintech and regtech: Impact on regulators and banks
AU Anagnostopoulos I
TC 153
SO Journal of Economics and Business
PY 2018
AB the purpose of this paper is to develop an insight and review the effect of fintech
   development against the broader environment in financial technology.  we further aim
   to offer various perspectives in order to aid the understanding of the disruptive
   potential of fintech, and its implications for the wider financial ecosystem.  by
   drawing upon very recent and highly topical research on this area this study
   examines the implications for financial institutions, and regulation especially when
   technology poses a challenge to the global banking and regulatory system.  it is
   driven by a wide-ranging overview of the development, the current state, and
   possible future of fintech.  this paper attempts to connect practitioner-led and
   academic research.  while it draws on academic research, the perspective it takes is
   also practice-oriented.  it relies on the current academic literature as well as
   insights from industry sources, action research and other publicly available
   commentaries.  it also draws on professional practitioners roundtable discussions,
   and think-tanks in which the author has been an active participant.  we attempt to
   interpret banking, and regulatory issues from a behavioural perspective.  the last
   crisis exposed significant failures in regulation and supervision.  it has made the
   financial market law and compliance a key topic on the current agenda.  disruptive
   technological change also seems to be important in investigating regulatory
   compliance followed by change.  we contribute to the current literature review on
   financial and digital innovation by new entrants where this has also practical
   implications.  we also provide for an updated review of the current regulatory
   issues addressing the contextual root causes of disruption within the financial
   services domain.  the aim here is to assist market participants to improve
   effectiveness and collaboration.  the difficulties arising from extensive regulation
   may suggest a more liberal and principled approach to financial regulation.
   disruptive innovation has the potential for welfare outcomes for consumers,
   regulatory, and supervisory gains as well as reputational gains for the financial
   services industry.  it becomes even more important as the financial services
   industry evolves.  for example, the preparedness of the regulators to instil culture
   change and harmonise technological advancements with regulation could likely achieve
   many desired outcomes.  such results range from achieving an orderly market growth,
   further aiding systemic stability and restoring trust and confidence in the
   financial system.  our action-led research results have implications for both
   research and practice.  these should be of interest to regulatory standard setters,
   investors, international organisations and other academics who are researching
   regulatory and competition issues, and their manifestation within the financial and
   social contexts.  as a perspective on a social construct, this study appeals to
   regulators and law makers, entrepreneurs, and investors who participate in
   technology applied within the innovative financial services domain.  it is also of
   interest to bankers who might consider fintech and strategic partnerships as a
   prospective, future strategic direction.1  2018 elsevier inc.
DE business models; financial services; fintech; future research direction; regtech;
   regulation
ID nan
------------------------------------------------------------------------------------------
AR Butler T/1, 2019, PALGRAVE STUD DIGIT BUS ENABLING TECHNOL, P85
TI Understanding RegTech for Digital Regulatory Compliance
AU Butler T/1; OBrien L
TC 33
SO Palgrave Studies in Digital Business and Enabling Technologies
PY 2019
AB this chapter explores the promise and potential of regulatory technologies
   (regtech), a new and vital dimension to fintech.  it draws on the findings and
   outcomes of a five-year research programme to highlight the role that regtech can
   play in making regulatory compliance more efficient and effective.  the chapter
   presents research on the bank of england/financial conduct authority (fca) regtech
   sprint initiative, whose objective was to demonstrate how straight-through
   processing of regulations and regulatory compliance reporting using semantically
   enabled applications can be made possible by regtech.  the chapter notes that the
   full benefits of regtech will only materialise if the pitfalls of a fragmented tower
   of babel approach are avoided.  semantic standards, we argue, are the key to all
   this.  2019, the author(s).
DE fintech; regtech; semantic technologies; standards
ID nan

"""
import textwrap

from .._lib._read_records import read_records


def record_view(
    criterion,
    search_for,
    case=False,
    flags=0,
    regex=True,
    records_length=10,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Record View."""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    contains = records[criterion].str.contains(
        search_for, case=case, flags=flags, regex=regex
    )
    contains = contains.dropna()
    contains = contains[contains]
    records = records.loc[contains.index, :]

    column_list = []

    reported_columns = [
        "article",
        "title",
        "authors",
        "global_citations",
        "source_title",
        "year",
        "abstract",
        "raw_author_keywords",
        "raw_index_keywords",
    ]

    for criterion in reported_columns:

        if criterion in records.columns:
            column_list.append(criterion)

    records = records[column_list]
    if "global_citations" in records.columns:
        records = records.sort_values(by="global_citations", ascending=False)

    records = records.head(records_length)

    for index, row in records.iterrows():

        for criterion in reported_columns:

            if criterion not in row.index:
                continue

            if row[criterion] is None:
                continue

            if criterion == "article":
                print("AR ", end="")
            if criterion == "title":
                print("TI ", end="")
            if criterion == "authors":
                print("AU ", end="")
            if criterion == "global_citations":
                print("TC ", end="")
            if criterion == "source_title":
                print("SO ", end="")
            if criterion == "year":
                print("PY ", end="")
            if criterion == "abstract":
                print("AB ", end="")
            if criterion == "raw_author_keywords":
                print("DE ", end="")
            if criterion == "author_keywords":
                print("DE ", end="")
            if criterion == "raw_index_keywords":
                print("ID ", end="")
            if criterion == "index_keywords":
                print("ID ", end="")

            print(
                textwrap.fill(
                    str(row[criterion]),
                    width=87,
                    initial_indent=" " * 3,
                    subsequent_indent=" " * 3,
                    fix_sentence_endings=True,
                )[3:]
            )

        if index != records.index[-1]:
            print("-" * 90)

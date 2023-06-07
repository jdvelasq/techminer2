# flake8: noqa
"""
Most Local Cited Documents
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_documents.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.documents.most_local_cited_documents(
...     top_n=20,
...     root_dir=root_dir,
... )
--INFO-- The file 'data/regtech/reports/most_local_cited_documents.txt' was created

>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_documents.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head(5)
                                                    global_citations  ...                             doi
article                                                               ...                                
Anagnostopoulos I, 2018, J ECON BUS, V100, P7                    153  ...  10.1016/J.JECONBUS.2018.07.003
Butler T/1, 2019, PALGRAVE STUD DIGIT BUS ENABL...                33  ...     10.1007/978-3-030-02330-0_6
Kavassalis P, 2018, J RISK FINANC, V19, P39                       21  ...        10.1108/JRF-07-2017-0111
Buckley RP, 2020, J BANK REGUL, V21, P26                          24  ...      10.1057/S41261-019-00104-1
Butler T/1, 2018, J RISK MANG FINANCIAL INST, V...                 8  ...                             NaN
<BLANKLINE>
[5 rows x 5 columns]



>>> print(r.prompts_[0])
Summarize the following text in 30 words or less: 
<BLANKLINE>
the purpose of this paper is to develop an insight and review the effect of FINTECH_DEVELOPMENT against the broader environment in FINANCIAL_TECHNOLOGY. we further aim to offer various perspectives in order to aid the understanding of the disruptive potential of FINTECH, and its implications for the wider financial ecosystem. by drawing upon very recent and highly topical research on this area this study examines the implications for FINANCIAL_INSTITUTIONS, and REGULATION especially when TECHNOLOGY poses a CHALLENGE to the global BANKING and regulatory system. IT is driven by a wide-ranging overview of the development, the CURRENT state, and possible future of FINTECH. this paper attempts to connect practitioner-led and academic research. while IT draws on academic research, the perspective IT takes is also practice-oriented. IT relies on the CURRENT_ACADEMIC_LITERATURE as well as insights from industry sources, action research and other publicly available commentaries. IT also draws on professional practitioners roundtable discussions, and think-tanks in which the author has been an active participant. we attempt to interpret BANKING, and REGULATORY_ISSUES from a behavioural perspective. the last crisis exposed significant failures in REGULATION and supervision. IT has made the FINANCIAL_MARKET law and COMPLIANCE a key topic on the CURRENT agenda. disruptive TECHNOLOGICAL_CHANGE also seems to be important in investigating REGULATORY_COMPLIANCE followed by change. we contribute to the CURRENT LITERATURE_REVIEW on financial and DIGITAL_INNOVATION by NEW_ENTRANTS where this has also practical implications. we also provide for an updated review of the CURRENT REGULATORY_ISSUES addressing the contextual root causes of disruption within the FINANCIAL_SERVICES domain. the aim here is to assist market participants to improve effectiveness and collaboration. the difficulties arising from extensive REGULATION may suggest a more liberal and principled approach to FINANCIAL_REGULATION. DISRUPTIVE_INNOVATION has the potential for welfare outcomes for consumers, regulatory, and supervisory gains as well as reputational gains for the FINANCIAL_SERVICES_INDUSTRY. IT becomes even more important as the FINANCIAL_SERVICES_INDUSTRY evolves. for example, the preparedness of the regulators to instil CULTURE change and harmonise technological advancements with REGULATION could likely achieve many desired outcomes. such results range from achieving an orderly market growth, further aiding systemic STABILITY and restoring TRUST and confidence in the FINANCIAL_SYSTEM. our action-led research results have implications for both research and practice. these should be of interest to regulatory standard setters, INVESTORS, INTERNATIONAL_ORGANISATIONS and other academics who are researching regulatory and COMPETITION issues, and their manifestation within the financial and social contexts. as a perspective on a social construct, this study appeals to regulators and law makers, entrepreneurs, and INVESTORS who participate in TECHNOLOGY applied within the innovative FINANCIAL_SERVICES domain. IT is also of interest to bankers who might consider FINTECH and strategic partnerships as a prospective, future strategic direction.1  2018 ELSEVIER_INC.


# pylint: disable=line-too-long
"""
from ..cited_documents import bibiometrix_cited_documents


def most_local_cited_documents(
    root_dir="./",
    top_n=20,
    title="Most Local Cited Documents",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most local cited documents."""

    return bibiometrix_cited_documents(
        metric="local_citations",
        root_dir=root_dir,
        file_name="most_local_cited_documents.txt",
        database="documents",
        top_n=top_n,
        title=title,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

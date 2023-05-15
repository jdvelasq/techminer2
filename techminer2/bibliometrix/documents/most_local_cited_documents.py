"""
Most Local Cited Documents
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_documents.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.documents.most_local_cited_documents(
...     topics_length=20,
...     directory=directory,
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
the purpose of this paper is to develop an insight and review the effect of fintech development against the broader environment in financial technology. we further aim to offer various perspectives in order to aid the understanding of the disruptive potential of fintech, and its implications for the wider financial ecosystem. by drawing upon very recent and highly topical research on this area this study examines the implications for financial institutions, and regulation especially when technology poses a challenge to the global banking and regulatory system. it is driven by a wide-ranging overview of the development, the current state, and possible future of fintech. this paper attempts to connect practitioner-led and academic research. while it draws on academic research, the perspective it takes is also practice-oriented. it relies on the current academic literature as well as insights from industry sources, action research and other publicly available commentaries. it also draws on professional practitioners roundtable discussions, and think-tanks in which the author has been an active participant. we attempt to interpret banking, and regulatory issues from a behavioural perspective. the last crisis exposed significant failures in regulation and supervision. it has made the financial market law and compliance a key topic on the current agenda. disruptive technological change also seems to be important in investigating regulatory compliance followed by change. we contribute to the current literature review on financial and digital innovation by new entrants where this has also practical implications. we also provide for an updated review of the current regulatory issues addressing the contextual root causes of disruption within the financial services domain. the aim here is to assist market participants to improve effectiveness and collaboration. the difficulties arising from extensive regulation may suggest a more liberal and principled approach to financial regulation. disruptive innovation has the potential for welfare outcomes for consumers, regulatory, and supervisory gains as well as reputational gains for the financial services industry. it becomes even more important as the financial services industry evolves. for example, the preparedness of the regulators to instil culture change and harmonise technological advancements with regulation could likely achieve many desired outcomes. such results range from achieving an orderly market growth, further aiding systemic stability and restoring trust and confidence in the financial system. our action-led research results have implications for both research and practice. these should be of interest to regulatory standard setters, investors, international organisations and other academics who are researching regulatory and competition issues, and their manifestation within the financial and social contexts. as a perspective on a social construct, this study appeals to regulators and law makers, entrepreneurs, and investors who participate in technology applied within the innovative financial services domain. it is also of interest to bankers who might consider fintech and strategic partnerships as a prospective, future strategic direction.1  2018 elsevier inc.


"""
from ..cited_documents import bibiometrix_cited_documents


def most_local_cited_documents(
    directory="./",
    topics_length=20,
    title="Most Local Cited Documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most local cited documents."""

    return bibiometrix_cited_documents(
        metric="local_citations",
        directory=directory,
        file_name="most_local_cited_documents.txt",
        database="documents",
        top_n=topics_length,
        title=title,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

"""
Most Global Cited Organizations
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_global_cited_organizations(
...     directory,
...     topics_length=20,
...     plot="cleveland",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
organizations
University of Hong Kong        185
---FinTech HK                  161
---Kingston Business School    153
---Centre for Law              150
University College Cork         41
Name: global_citations, dtype: int64

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
organizations with more global_citations in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
<BLANKLINE>
| organizations                                                   |   global_citations |
|:----------------------------------------------------------------|-------------------:|
| University of Hong Kong                                         |                185 |
| ---FinTech HK                                                   |                161 |
| ---Kingston Business School                                     |                153 |
| ---Centre for Law                                               |                150 |
| University College Cork                                         |                 41 |
| Duke University School of Law                                   |                 30 |
| Heinrich Heine University                                       |                 24 |
| University of Zurich                                            |                 24 |
| University of Luxembourg                                        |                 24 |
| ---UNSW Sydney                                                  |                 24 |
| Harvard University Weatherhead Center for International Affairs |                 21 |
| ---School of Engineering                                        |                 21 |
| ---Panepistemio Aigaiou                                         |                 21 |
| ---KS Strategic                                                 |                 21 |
| European Central Bank                                           |                 21 |
| Ahlia University                                                |                 19 |
| University of Westminster                                       |                 17 |
| Coventry University                                             |                 17 |
| Dublin City University                                          |                 14 |
| Shanghai University                                             |                 13 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>


"""
from ...vantagepoint.report.chart import chart


def most_global_cited_organizations(
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most global cited organizations."""

    return chart(
        criterion="organizations",
        directory=directory,
        database=database,
        metric="global_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Global Cited Organizations",
        plot=plot,
        **filters,
    )

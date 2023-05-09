"""
Most Relevant Organizations
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_relevant_organizations.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.most_relevant_organizations(
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
...     database="documents",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_relevant_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
organizations
University of Hong Kong      3
University College Cork      3
Ahlia University             3
---FinTech HK                2
University of Westminster    2
Name: OCC, dtype: int64

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
organizations with more OCC in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
<BLANKLINE>
| organizations                                                   |   OCC |
|:----------------------------------------------------------------|------:|
| University of Hong Kong                                         |     3 |
| University College Cork                                         |     3 |
| Ahlia University                                                |     3 |
| ---FinTech HK                                                   |     2 |
| University of Westminster                                       |     2 |
| Coventry University                                             |     2 |
| Dublin City University                                          |     2 |
| Politecnico di Milano                                           |     2 |
| ---School of Electrical Engineering and Informatics             |     2 |
| ---Kingston Business School                                     |     1 |
| ---Centre for Law                                               |     1 |
| Duke University School of Law                                   |     1 |
| Heinrich Heine University                                       |     1 |
| University of Zurich                                            |     1 |
| University of Luxembourg                                        |     1 |
| ---UNSW Sydney                                                  |     1 |
| Harvard University Weatherhead Center for International Affairs |     1 |
| ---School of Engineering                                        |     1 |
| ---Panepistemio Aigaiou                                         |     1 |
| ---KS Strategic                                                 |     1 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>


"""
from ...vantagepoint.report.chart import chart


def most_relevant_organizations(
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
    """Plots the number of documents by organizations using the specified plot."""

    return chart(
        criterion="organizations",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Frequent Organizations",
        plot=plot,
        **filters,
    )

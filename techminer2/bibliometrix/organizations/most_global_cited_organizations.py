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
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 cited organizations with highest number of total citations in the dataset ('global_citations' column). Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the organization in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
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

    obj = chart(
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

    obj.prompt_ = _create_prompt(obj.table_)

    return obj


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} cited organizations with highest \
number of total citations in the dataset ('global_citations' column). Use the \
information in the table to draw conclusions about the impact and relevance of \
the reseach published by the organization in the dataset. In your analysis, be sure \
to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""

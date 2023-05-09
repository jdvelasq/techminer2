"""
Organization Impact
===============================================================================



>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__organization_impact.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.organizations.organization_impact(
...     impact_measure='h_index', 
...     topics_length=20, 
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__organization_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
             Organizations  ...  Avg Global Citations
0  University of Hong Kong  ...                 61.67
1      Coventry University  ...                  8.50
2         Ahlia University  ...                  6.33
3  University College Cork  ...                 13.67
4            ---FinTech HK  ...                 80.50
<BLANKLINE>
[5 rows x 10 columns]

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. 
<BLANKLINE>
The following table contains the top 20 Organizations 
with more H Index in the given bibliographic dataset.
<BLANKLINE>
| Organizations                            |   Occ |   Global Citations |   First Pb Year |   Age |   H Index |   G Index |   M Index |   Global Citations Per Year |   Avg Global Citations |
|:-----------------------------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| University of Hong Kong                  |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| Coventry University                      |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Ahlia University                         |     3 |                 19 |            2020 |     4 |         2 |         2 |      0.5  |                        4.75 |                   6.33 |
| University College Cork                  |     3 |                 41 |            2018 |     6 |         2 |         2 |      0.33 |                        6.83 |                  13.67 |
| ---FinTech HK                            |     2 |                161 |            2017 |     7 |         2 |         2 |      0.29 |                       23    |                  80.5  |
| Dublin City University                   |     2 |                 14 |            2020 |     4 |         2 |         1 |      0.5  |                        3.5  |                   7    |
| University of Westminster                |     2 |                 17 |            2020 |     4 |         2 |         1 |      0.5  |                        4.25 |                   8.5  |
| Finance and Banking                      |     1 |                 11 |            2020 |     4 |         1 |         1 |      0.25 |                        2.75 |                  11    |
| ---AML Forensic library KPMG...          |     1 |                 10 |            2020 |     4 |         1 |         1 |      0.25 |                        2.5  |                  10    |
| Goethe University Frankfurt              |     1 |                  1 |            2022 |     2 |         1 |         1 |      0.5  |                        0.5  |                   1    |
| Guru Gobind Singh Indraprastha...        |     1 |                  1 |            2020 |     4 |         1 |         1 |      0.25 |                        0.25 |                   1    |
| Politecnico di Milano                    |     2 |                  2 |            2020 |     4 |         1 |         1 |      0.25 |                        0.5  |                   1    |
| Harvard University Weatherhead Center... |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Hebei University of Technology           |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                  13    |
| Heinrich Heine University                |     1 |                 24 |            2020 |     4 |         1 |         1 |      0.25 |                        6    |                  24    |
| Jiangsu University                       |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                  13    |
| FOM University of Applied Sciences       |     1 |                  5 |            2020 |     4 |         1 |         1 |      0.25 |                        1.25 |                   5    |
| Macquarie University                     |     1 |                  2 |            2021 |     3 |         1 |         1 |      0.33 |                        0.67 |                   2    |
| National Chengchi University             |     1 |                  1 |            2017 |     7 |         1 |         1 |      0.14 |                        0.14 |                   1    |
| Palestine Technical University           |     1 |                  1 |            2021 |     3 |         1 |         1 |      0.33 |                        0.33 |                   1    |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice in the previous table. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.    
<BLANKLINE>
<BLANKLINE>

"""
from .._impact import _impact


def organization_impact(
    impact_measure="h_index",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the selected impact measure by organizations."""

    return _impact(
        criterion="organizations",
        impact_measure=impact_measure,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Organization Local Impact by "
        + impact_measure.replace("_", " ").title(),
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

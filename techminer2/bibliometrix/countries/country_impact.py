"""
Country Impact
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_impact.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.country_impact(
...     impact_measure='h_index',
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_impact.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| countries      |   OCC |   Global Citations |   First Pb Year |   Age |   H-Index |   G-Index |   M-Index |   Global Citations Per Year |   Avg Global Citations |
|:---------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Australia      |     7 |                199 |            2017 |     7 |         4 |         3 |      0.57 |                       28.43 |                  28.43 |
| United Kingdom |     7 |                199 |            2018 |     6 |         4 |         3 |      0.67 |                       33.17 |                  28.43 |
| Hong Kong      |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| United States  |     6 |                 59 |            2016 |     8 |         3 |         2 |      0.38 |                        7.38 |                   9.83 |
| Ireland        |     5 |                 55 |            2018 |     6 |         3 |         2 |      0.5  |                        9.17 |                  11    |

>>> print(r.prompt_)
The table below provides data on top 20 countries with the highest H-Index. 'OCC' represents the number of documents published by the country in the dataset. Use the information in the table to draw conclusions about the impact and productivity of the country. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
<BLANKLINE>
| countries            |   OCC |   Global Citations |   First Pb Year |   Age |   H-Index |   G-Index |   M-Index |   Global Citations Per Year |   Avg Global Citations |
|:---------------------|------:|-------------------:|----------------:|------:|----------:|----------:|----------:|----------------------------:|-----------------------:|
| Australia            |     7 |                199 |            2017 |     7 |         4 |         3 |      0.57 |                       28.43 |                  28.43 |
| United Kingdom       |     7 |                199 |            2018 |     6 |         4 |         3 |      0.67 |                       33.17 |                  28.43 |
| Hong Kong            |     3 |                185 |            2017 |     7 |         3 |         3 |      0.43 |                       26.43 |                  61.67 |
| United States        |     6 |                 59 |            2016 |     8 |         3 |         2 |      0.38 |                        7.38 |                   9.83 |
| Ireland              |     5 |                 55 |            2018 |     6 |         3 |         2 |      0.5  |                        9.17 |                  11    |
| Germany              |     4 |                 51 |            2018 |     6 |         3 |         2 |      0.5  |                        8.5  |                  12.75 |
| China                |     5 |                 27 |            2017 |     7 |         3 |         2 |      0.43 |                        3.86 |                   5.4  |
| Switzerland          |     4 |                 45 |            2017 |     7 |         2 |         2 |      0.29 |                        6.43 |                  11.25 |
| Luxembourg           |     2 |                 34 |            2020 |     4 |         2 |         2 |      0.5  |                        8.5  |                  17    |
| Bahrain              |     4 |                 19 |            2020 |     4 |         2 |         2 |      0.5  |                        4.75 |                   4.75 |
| United Arab Emirates |     2 |                 13 |            2020 |     4 |         2 |         1 |      0.5  |                        3.25 |                   6.5  |
| Greece               |     1 |                 21 |            2018 |     6 |         1 |         1 |      0.17 |                        3.5  |                  21    |
| Japan                |     1 |                 13 |            2022 |     2 |         1 |         1 |      0.5  |                        6.5  |                  13    |
| Jordan               |     1 |                 11 |            2020 |     4 |         1 |         1 |      0.25 |                        2.75 |                  11    |
| South Africa         |     1 |                 11 |            2021 |     3 |         1 |         1 |      0.33 |                        3.67 |                  11    |
| Italy                |     5 |                  5 |            2019 |     5 |         1 |         1 |      0.2  |                        1    |                   1    |
| Spain                |     2 |                  4 |            2021 |     3 |         1 |         1 |      0.33 |                        1.33 |                   2    |
| Ukraine              |     1 |                  4 |            2020 |     4 |         1 |         1 |      0.25 |                        1    |                   4    |
| Malaysia             |     1 |                  3 |            2019 |     5 |         1 |         1 |      0.2  |                        0.6  |                   3    |
| India                |     1 |                  1 |            2020 |     4 |         1 |         1 |      0.25 |                        0.25 |                   1    |
<BLANKLINE>


"""
# from ..criterion_impact import criterion_impact


def country_impact(
    impact_measure="h_index",
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Plots the selected impact measure by country."""

    obj = criterion_impact(
        criterion="countries",
        metric=impact_measure,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        directory=directory,
        title="Country Local Impact by "
        + impact_measure.replace("_", " ").title(),
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    obj.prompt_ = _create_prompt(obj.table_, impact_measure)

    return obj


def _create_prompt(table, impact_measure):
    return f"""\
The table below provides data on top {table.shape[0]} countries with the \
highest {impact_measure.replace("_", "-").title()}. 'OCC' represents the \
number of documents published by the country in the dataset. Use the \
information in the table to draw conclusions about the impact and \
productivity of the country. In your analysis, be sure to describe in a clear \
and concise way, any findings or any patterns you observe, and identify any \
outliers or anomalies in the data. Limit your description to one paragraph \
with no more than 250 words.

{table.to_markdown()}
"""

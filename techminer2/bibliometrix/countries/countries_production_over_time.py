"""
Countries' Production over Time
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__countries_production_over_time.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.countries_production_over_time(
...    topics_length=10,
...    directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__countries_production_over_time.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.documents_per_country_.head()
       countries  ...                            doi
0          Italy  ...  10.1016/J.TECHSOC.2022.102150
1    Switzerland  ...  10.1016/J.TECHSOC.2022.102150
2  United States  ...  10.1016/J.TECHSOC.2022.102150
3          China  ...    10.1016/J.RIBAF.2022.101868
4  United States  ...        10.1109/MC.2022.3176693
<BLANKLINE>
[5 rows x 7 columns]


>>> r.production_per_year_.head()
                OCC  ...  local_citations_per_year
countries year       ...                          
Australia 2017    2  ...                     0.429
          2020    3  ...                     2.250
          2021    2  ...                     1.000
Bahrain   2020    1  ...                     1.000
          2021    2  ...                     0.333
<BLANKLINE>
[5 rows x 7 columns]


>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top 10
countries with more documnets in a given bibliographic dataset. 
<BLANKLINE>
- Column 'OCC' is the number of documents published in a given year by the 
  current source. 
<BLANKLINE>
- Column 'Year' is the year of publication.
<BLANKLINE>
- Column 'Countries' is the name of the country.
<BLANKLINE>
- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current country during the 
  period of analysis.
<BLANKLINE>
| Countries            |   OCC |   Year |
|:---------------------|------:|-------:|
| United Kingdom 7:199 |     3 |   2018 |
| Australia 7:199      |     2 |   2017 |
| Australia 7:199      |     3 |   2020 |
| United Kingdom 7:199 |     2 |   2020 |
| Australia 7:199      |     2 |   2021 |
| United Kingdom 7:199 |     1 |   2022 |
| United Kingdom 7:199 |     1 |   2019 |
| United States 6:059  |     1 |   2016 |
| United States 6:059  |     1 |   2018 |
| United States 6:059  |     2 |   2019 |
| United States 6:059  |     1 |   2022 |
| United States 6:059  |     1 |   2023 |
| Ireland 5:055        |     1 |   2019 |
| China 5:027          |     3 |   2022 |
| Ireland 5:055        |     1 |   2020 |
| China 5:027          |     1 |   2017 |
| Ireland 5:055        |     1 |   2018 |
| Italy 5:005          |     1 |   2019 |
| Ireland 5:055        |     1 |   2021 |
| Italy 5:005          |     1 |   2020 |
| Italy 5:005          |     1 |   2022 |
| China 5:027          |     1 |   2023 |
| Ireland 5:055        |     1 |   2022 |
| Italy 5:005          |     1 |   2021 |
| Italy 5:005          |     1 |   2023 |
| Germany 4:051        |     2 |   2020 |
| Switzerland 4:045    |     1 |   2020 |
| Germany 4:051        |     1 |   2018 |
| Switzerland 4:045    |     1 |   2018 |
| Bahrain 4:019        |     1 |   2020 |
| Bahrain 4:019        |     2 |   2021 |
| Bahrain 4:019        |     1 |   2022 |
| Germany 4:051        |     1 |   2022 |
| Switzerland 4:045    |     1 |   2017 |
| Switzerland 4:045    |     1 |   2023 |
| Hong Kong 3:185      |     2 |   2017 |
| Hong Kong 3:185      |     1 |   2020 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.    
<BLANKLINE>



"""
from dataclasses import dataclass

from ...techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)
from .._documents_per import _documents_per
from .._production_over_time import _production_over_time


@dataclass(init=False)
class _Results:
    plot_ = None
    prompt_ = None
    production_per_year_ = None
    documents_per_country_ = None


def countries_production_over_time(
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Country production over time."""

    results = _production_over_time(
        criterion="countries",
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        title="Country' production over time",
        metric="OCC",
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.documents_per_country_ = _documents_per(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    results.production_per_year_ = indicators_by_topic_per_year(
        criterion="countries",
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    prompt_table = results.table_[["Countries", "OCC", "Year"]]
    prompt_table = prompt_table.set_index("Countries")

    results.prompt_ = f"""
Act as a researcher realizing a bibliometric analysis. Analyze a timeline plot
build with the following table, which provides data corresponding to the top {topics_length}
countries with more documnets in a given bibliographic dataset. 

- Column 'OCC' is the number of documents published in a given year by the 
  current source. 

- Column 'Year' is the year of publication.

- Column 'Countries' is the name of the country.

- Numbers separated by a colon (:) are the total number of documents published
  the total number of citations received by the current country during the 
  period of analysis.

{prompt_table.to_markdown()}

Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 

Limit your description to a paragraph with no more than 250 words.    
"""

    return results

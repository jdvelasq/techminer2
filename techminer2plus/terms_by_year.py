# flake8: noqa
# pylint: disable=line-too-long
"""
.. _terms_by_year:

Terms by Year 
===============================================================================


>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> terms_by_year = (
...     tm2p.Records(root_dir=root_dir)
...     .field("author_keywords", top_n=10)
...     .terms_by_year()
... )
>>> terms_by_year
TermsByYear(field='author_keywords', metric='OCC', top_n=10,
    custom_items=['REGTECH', 'FINTECH', 'REGULATORY_TECHNOLOGY', 'COMPLIANCE',
    'REGULATION', 'ANTI_MONEY_LAUNDERING', 'FINANCIAL_SERVICES',
    'FINANCIAL_REGULATION', 'ARTIFICIAL_INTELLIGENCE', 'RISK_MANAGEMENT'],
    cumulative=False)

>>> terms_by_year.frame_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     3     4     8     3     6     2
FINTECH 12:249                     0     2     4     3     1     2     0
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     3     2     0
COMPLIANCE 07:030                  0     0     1     3     1     1     1
REGULATION 05:164                  0     2     0     1     1     1     0
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     3     0     0
FINANCIAL_SERVICES 04:168          1     1     0     1     0     1     0
FINANCIAL_REGULATION 04:035        1     0     0     1     0     2     0
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     2     0     1     0
RISK_MANAGEMENT 03:014             0     1     0     1     0     1     0



>>> print(terms_by_year.prompt_)
Your task is to generate an analysis about the  occurrences by year of the \\
'author_keywords' in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, identify any notable patterns, \\
trends, or outliers in the data, and disc  uss their implications for the \\
research field. Be sure to provide a concise summary of your findings in no \\
more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      3 |      4 |      8 |      3 |      6 |      2 |
| FINTECH 12:249                 |      0 |      2 |      4 |      3 |      1 |      2 |      0 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      3 |      2 |      0 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      3 |      1 |      1 |      1 |
| REGULATION 05:164              |      0 |      2 |      0 |      1 |      1 |      1 |      0 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      3 |      0 |      0 |
| FINANCIAL_SERVICES 04:168      |      1 |      1 |      0 |      1 |      0 |      1 |      0 |
| FINANCIAL_REGULATION 04:035    |      1 |      0 |      0 |      1 |      0 |      2 |      0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      2 |      0 |      1 |      0 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      0 |      1 |      0 |      1 |      0 |
```
<BLANKLINE>




>>> terms_by_year = (
...     tm2p.Records(root_dir=root_dir)
...     .field("author_keywords", top_n=10)
...     .terms_by_year(cumulative=True)
... )
>>> terms_by_year.frame_
year                            2017  2018  2019  2020  2021  2022  2023
author_keywords                                                         
REGTECH 28:329                     2     5     9    17    20    26    28
FINTECH 12:249                     0     2     6     9    10    12    12
REGULATORY_TECHNOLOGY 07:037       0     0     0     2     5     7     7
COMPLIANCE 07:030                  0     0     1     4     5     6     7
REGULATION 05:164                  0     2     2     3     4     5     5
ANTI_MONEY_LAUNDERING 05:034       0     0     0     2     5     5     5
FINANCIAL_SERVICES 04:168          1     2     2     3     3     4     4
FINANCIAL_REGULATION 04:035        1     1     1     2     2     4     4
ARTIFICIAL_INTELLIGENCE 04:023     0     0     1     3     3     4     4
RISK_MANAGEMENT 03:014             0     1     1     2     2     3     3

>>> print(terms_by_year.prompt_)
Your task is to generate an analysis about the cumulative occurrences by \\
year of the 'author_keywords' in a scientific bibliography database. \\
Summarize the table below, delimited by triple backticks, identify any \\
notable patterns, trends, or outliers in the data, and disc  uss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                |   2017 |   2018 |   2019 |   2020 |   2021 |   2022 |   2023 |
|:-------------------------------|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
| REGTECH 28:329                 |      2 |      5 |      9 |     17 |     20 |     26 |     28 |
| FINTECH 12:249                 |      0 |      2 |      6 |      9 |     10 |     12 |     12 |
| REGULATORY_TECHNOLOGY 07:037   |      0 |      0 |      0 |      2 |      5 |      7 |      7 |
| COMPLIANCE 07:030              |      0 |      0 |      1 |      4 |      5 |      6 |      7 |
| REGULATION 05:164              |      0 |      2 |      2 |      3 |      4 |      5 |      5 |
| ANTI_MONEY_LAUNDERING 05:034   |      0 |      0 |      0 |      2 |      5 |      5 |      5 |
| FINANCIAL_SERVICES 04:168      |      1 |      2 |      2 |      3 |      3 |      4 |      4 |
| FINANCIAL_REGULATION 04:035    |      1 |      1 |      1 |      2 |      2 |      4 |      4 |
| ARTIFICIAL_INTELLIGENCE 04:023 |      0 |      0 |      1 |      3 |      3 |      4 |      4 |
| RISK_MANAGEMENT 03:014         |      0 |      1 |      1 |      2 |      2 |      3 |      3 |
```
<BLANKLINE>



"""

import textwrap

import pandas as pd

from .chatbot_prompts import format_chatbot_prompt_for_df
from .gantt_chart import gantt_chart


class TermsByYear:
    """Terms by year."""

    def __init__(self, records_instance, field_instance, cumulative=False):
        """Constructor."""

        #
        # Inputs:
        #
        self.__records_instance = records_instance
        self.__field_instance = field_instance
        self.__cumulative = cumulative

        #
        # Params:
        #
        self.__frame = pd.DataFrame()
        self.__prompt = None

        #
        # Computations:
        #
        self.__compute_terms_by_year()
        self.__generate_prompt()

    #
    #
    # PROPERTIES
    #
    #
    def __repr__(self):
        """String representation."""
        params = ", ".join(self.repr_params_)
        text = f"{self.__class__.__name__}({params})"
        text = textwrap.fill(text, width=80, subsequent_indent=" " * 4)
        return text

    @property
    def repr_params_(self):
        """Returns the parameters used for the string representation as a list."""
        return self.__field_instance.repr_params_ + [
            f"cumulative={self.__cumulative}",
        ]

    @property
    def frame_(self):
        """Returns the dataframe."""
        return self.__frame

    @property
    def prompt_(self):
        """Returns the chatbot prompt."""
        return self.__prompt

    @property
    def cumulative_(self):
        """Returns the cumulative param."""
        return self.__cumulative

    @property
    def field_(self):
        """Returns the field name."""
        return self.__field_instance.field_

    #
    #
    # PUBLIC METHODS FOR VISUALIZATION
    #
    #
    def gantt_chart(self, title=None):
        """Returns a Gantt chart."""
        return gantt_chart(self, title=title)

    #
    #
    # INTERNAL METHODS
    #
    #
    def __compute_terms_by_year(self):
        """Computes terms by year."""

        descriptors_by_year = self.__records_instance.items_occ_by_year(
            field=self.__field_instance.field_,
            cumulative=self.__cumulative,
        )

        descriptors_by_year = descriptors_by_year[
            descriptors_by_year.index.isin(self.__field_instance.custom_items_)
        ]

        descriptors_by_year = descriptors_by_year.loc[
            self.__field_instance.custom_items_, :
        ]

        self.__frame = self.__records_instance.add_counters_to_frame_axis(
            descriptors_by_year,
            axis=0,
            field=self.__field_instance.field_,
        )

    def __generate_prompt(self):
        # pylint: disable=line-too-long
        main_text = (
            "Your task is to generate an analysis about the "
            f"{'cumulative' if self.cumulative_ else ''} occurrences by year "
            f"of the '{self.field_}' in a scientific bibliography database. "
            "Summarize the table below, delimited by triple backticks, "
            "identify any notable patterns, trends, or outliers in the data, "
            "and disc  uss their implications for the research field. Be sure "
            "to provide a concise summary of your findings in no more than "
            "150 words."
        )
        self.__prompt = format_chatbot_prompt_for_df(
            main_text, self.frame_.to_markdown()
        )

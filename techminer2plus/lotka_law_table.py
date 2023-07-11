# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Lotka's Law Table
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/analyze/lotka_law.html"

>>> import techminer2plus as tm2p
>>> tm2p.lotka_law_table(root_dir=root_dir)
   Documents Written  ...  Prop Theoretical Authors
0                  1  ...                     0.735
1                  2  ...                     0.184
2                  3  ...                     0.082
<BLANKLINE>
[3 rows x 5 columns]

"""
from .global_indicators_by_field import global_indicators_by_field


def lotka_law_table(
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    #
    # Part 1: Computes the number of written documents per number of authors.
    #         Read as: "178 authors write only 1 document and 1 author writes 7 documents"
    #
    #    Documents Written  Num Authors
    # 0                  1          178
    # 1                  2            9
    # 2                  3            2
    # 3                  4            2
    # 4                  6            1
    # 5                  7            1
    #
    indicators = global_indicators_by_field(
        field="authors",
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = indicators[["OCC"]]
    indicators = indicators.groupby(["OCC"], as_index=False).size()
    indicators.columns = ["Documents Written", "Num Authors"]
    indicators = indicators.sort_values(by="Documents Written", ascending=True)
    indicators = indicators.reset_index(drop=True)
    indicators = indicators[["Documents Written", "Num Authors"]]
    indicators["Proportion of Authors"] = (
        indicators["Num Authors"]
        .map(lambda x: x / indicators["Num Authors"].sum())
        .round(3)
    )

    #
    # Part 2: Computes the theoretical number of authors
    #
    total_authors = indicators["Num Authors"].max()
    indicators["Theoretical Num Authors"] = (
        indicators["Documents Written"]
        .map(lambda x: total_authors / float(x * x))
        .round(3)
    )
    total_theoretical_num_authors = indicators["Theoretical Num Authors"].sum()
    indicators["Prop Theoretical Authors"] = (
        indicators["Theoretical Num Authors"]
        .map(lambda x: x / total_theoretical_num_authors)
        .round(3)
    )

    return indicators

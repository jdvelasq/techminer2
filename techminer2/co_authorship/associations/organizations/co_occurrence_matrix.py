# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.co_authorship.associations.organizations.co_occurrence_matrix:

Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_authorship.associations.organizations import co_occurrence_matrix
>>> matrix = co_occurrence_matrix(
...     #
...     # ITEM PARAMS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_.head()
organizations                    Univ of Hong Kong (HKG) 3:185  ...  ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150
organizations                                                   ...                                                                          
Univ of Hong Kong (HKG) 3:185                                3  ...                                                  1                       
Univ Coll Cork (IRL) 3:041                                   0  ...                                                  0                       
Ahlia Univ (BHR) 3:019                                       0  ...                                                  0                       
Coventry Univ (GBR) 2:017                                    0  ...                                                  0                       
Univ of Westminster (GBR) 2:017                              0  ...                                                  0                       
<BLANKLINE>
[5 rows x 10 columns]



>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
                             row                           column  matrix_value
0  Univ of Hong Kong (HKG) 3:185    Univ of Hong Kong (HKG) 3:185             3
1  Univ of Hong Kong (HKG) 3:185       Univ Coll Cork (IRL) 3:041             0
2  Univ of Hong Kong (HKG) 3:185           Ahlia Univ (BHR) 3:019             0
3  Univ of Hong Kong (HKG) 3:185        Coventry Univ (GBR) 2:017             0
4  Univ of Hong Kong (HKG) 3:185  Univ of Westminster (GBR) 2:017             0


>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the \\
'organizations' and 'None' fields in a bibliographic dataset. Identify any \\
notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                                            |   Univ of Hong Kong (HKG) 3:185 |   Univ Coll Cork (IRL) 3:041 |   Ahlia Univ (BHR) 3:019 |   Coventry Univ (GBR) 2:017 |   Univ of Westminster (GBR) 2:017 |   Dublin City Univ (IRL) 2:014 |   Politec di Milano (ITA) 2:002 |   Kingston Bus Sch (GBR) 1:153 |   FinTech HK, Hong Kong (HKG) 1:150 |   ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |
|:-------------------------------------------------------------------------|--------------------------------:|-----------------------------:|-------------------------:|----------------------------:|----------------------------------:|-------------------------------:|--------------------------------:|-------------------------------:|------------------------------------:|---------------------------------------------------------------------------:|
| Univ of Hong Kong (HKG) 3:185                                            |                               3 |                            0 |                        0 |                           0 |                                 0 |                              0 |                               0 |                              0 |                                   1 |                                                                          1 |
| Univ Coll Cork (IRL) 3:041                                               |                               0 |                            3 |                        0 |                           0 |                                 0 |                              0 |                               0 |                              0 |                                   0 |                                                                          0 |
| Ahlia Univ (BHR) 3:019                                                   |                               0 |                            0 |                        3 |                           0 |                                 0 |                              0 |                               0 |                              0 |                                   0 |                                                                          0 |
| Coventry Univ (GBR) 2:017                                                |                               0 |                            0 |                        0 |                           2 |                                 2 |                              0 |                               0 |                              0 |                                   0 |                                                                          0 |
| Univ of Westminster (GBR) 2:017                                          |                               0 |                            0 |                        0 |                           2 |                                 2 |                              0 |                               0 |                              0 |                                   0 |                                                                          0 |
| Dublin City Univ (IRL) 2:014                                             |                               0 |                            0 |                        0 |                           0 |                                 0 |                              2 |                               0 |                              0 |                                   0 |                                                                          0 |
| Politec di Milano (ITA) 2:002                                            |                               0 |                            0 |                        0 |                           0 |                                 0 |                              0 |                               2 |                              0 |                                   0 |                                                                          0 |
| Kingston Bus Sch (GBR) 1:153                                             |                               0 |                            0 |                        0 |                           0 |                                 0 |                              0 |                               0 |                              1 |                                   0 |                                                                          0 |
| FinTech HK, Hong Kong (HKG) 1:150                                        |                               1 |                            0 |                        0 |                           0 |                                 0 |                              0 |                               0 |                              0 |                                   1 |                                                                          1 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |                               1 |                            0 |                        0 |                           0 |                                 0 |                              0 |                               0 |                              0 |                                   1 |                                                                          1 |
```
<BLANKLINE>


"""
from ....co_occurrence.co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "organizations"


def co_occurrence_matrix(
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """
    :meta private:
    """

    return __co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=ROWS_AND_COLUMNS,
        rows=None,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # ROW PARAMS:
        row_top_n=None,
        row_occ_range=(None, None),
        row_gc_range=(None, None),
        row_custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

"""
Coverage report
===============================================================================

>>> from techminer import *
>>> coverage("/workspaces/techminer-api/data/")
                    column  number of terms coverage (%)
0                 abstract              826      100.00%
1             affiliations              795       96.25%
2          author_keywords              620       75.06%
3                  authors              807       97.70%
4               authors_id              807       97.70%
5        bradford_law_zone              826      100.00%
6                countries              792       95.88%
7       country_1st_author              792       95.88%
8              document_id              826      100.00%
9           document_title              826      100.00%
10           document_type              826      100.00%
11                     doi              666       80.63%
12      frac_num_documents              826      100.00%
13        global_citations              826      100.00%
14       global_references              766       92.74%
15          index_keywords              293       35.47%
16  institution_1st_author              747       90.44%
17            institutions              747       90.44%
18                    isbn              211       25.54%
19         iso_source_name              826      100.00%
20                    issn              665       80.51%
21         local_citations              826      100.00%
22        local_references              555       67.19%
23             num_authors              826      100.00%
24   num_global_references              826      100.00%
25              page_start              590       71.43%
26                pub_year              826      100.00%
27               pubmed_id                5        0.61%
28     raw_author_keywords              620       75.06%
29       raw_authors_names              808       97.82%
30      raw_index_keywords              293       35.47%
31            raw_keywords              251       30.39%
32               record_no              826      100.00%
33             source_name              826      100.00%
34                  volume              577       69.85%

"""

import pandas as pd

from .utils import load_filtered_documents


def coverage(directory="./"):
    """
    Returns an coverage report of the dataset.

    Parameters
    ----------
    directory: str
        path to the directory

    Returns
    -------
    pandas.DataFrame
        Coverage statistcs
    """
    documents = load_filtered_documents(directory)
    columns = sorted(documents.columns)
    n_documents = len(documents)
    report = pd.DataFrame(
        {
            "column": columns,
            "number of terms": [
                n_documents - documents[col].isnull().sum() for col in columns
            ],
            "coverage (%)": [
                "{:5.2%}".format(
                    (n_documents - documents[col].isnull().sum()) / n_documents
                )
                for col in columns
            ],
        }
    )

    return report

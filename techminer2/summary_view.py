"""
Summary View
===============================================================================

>>> from techminer2 import *
>>> summary_view("/workspaces/techminer-api/data/")
                    column  number of terms coverage (%)
0                 abstract              248      100.00%
1             affiliations              244       98.39%
2          author_keywords              202       81.45%
3                  authors              245       98.79%
4               authors_id              245       98.79%
5        bradford_law_zone              248      100.00%
6                countries              244       98.39%
7       country_1st_author              244       98.39%
8              document_id              248      100.00%
9           document_title              248      100.00%
10           document_type              248      100.00%
11                     doi              248      100.00%
12      frac_num_documents              248      100.00%
13        global_citations              248      100.00%
14       global_references              238       95.97%
15          index_keywords               88       35.48%
16  institution_1st_author              236       95.16%
17            institutions              236       95.16%
18                    isbn               13        5.24%
19         iso_source_name              248      100.00%
20                    issn              240       96.77%
21         local_citations              248      100.00%
22        local_references              118       47.58%
23             num_authors              248      100.00%
24   num_global_references              248      100.00%
25              page_start              153       61.69%
26                pub_year              248      100.00%
27               pubmed_id                4        1.61%
28     raw_author_keywords              202       81.45%
29       raw_authors_names              246       99.19%
30      raw_index_keywords               88       35.48%
31            raw_keywords               66       26.61%
32               record_no              248      100.00%
33             source_name              248      100.00%
34                  volume              217       87.50%

"""

import pandas as pd

from .utils import load_filtered_documents


def summary_view(directory="./"):
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

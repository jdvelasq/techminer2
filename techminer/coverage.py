"""
Coverage report
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> coverage(directory)
                    column  number of terms coverage (%)
0                 abstract             1301      100.00%
1             affiliations             1266       97.31%
2          author_keywords             1122       86.24%
3       author_keywords_cl             1122       86.24%
4                  authors             1283       98.62%
5               authors_id             1283       98.62%
6        bradford_law_zone             1301      100.00%
7                countries             1262       97.00%
8       country_1st_author             1262       97.00%
9              document_id             1301      100.00%
10          document_title             1301      100.00%
11           document_type             1301      100.00%
12                     doi             1094       84.09%
13      frac_num_documents             1301      100.00%
14        global_citations             1301      100.00%
15       global_references             1230       94.54%
16          index_keywords              497       38.20%
17       index_keywords_cl              497       38.20%
18  institution_1st_author             1198       92.08%
19            institutions             1198       92.08%
20                    isbn              334       25.67%
21         iso_source_name             1301      100.00%
22                    issn             1056       81.17%
23                keywords              459       35.28%
24             keywords_cl              459       35.28%
25         local_citations             1301      100.00%
26        local_references              815       62.64%
27             num_authors             1301      100.00%
28   num_global_references             1301      100.00%
29                pub_year             1301      100.00%
30               pubmed_id                7        0.54%
31       raw_authors_names             1284       98.69%
32             source_name             1301      100.00%
"""

import pandas as pd

from .lib import load_filtered_documents


def coverage(directory):
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

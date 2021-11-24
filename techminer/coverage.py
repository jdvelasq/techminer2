"""
Coverage report
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> coverage(directory)
                    column  number of terms coverage (%)
0                 abstract             1649      100.00%
1             affiliations             1605       97.33%
2          author_keywords             1411       85.57%
3                  authors             1627       98.67%
4               authors_id             1627       98.67%
5        bradford_law_zone             1649      100.00%
6                countries             1599       96.97%
7       country_1st_author             1599       96.97%
8              document_id             1649      100.00%
9           document_title             1649      100.00%
10           document_type             1649      100.00%
11                     doi             1374       83.32%
12      frac_num_documents             1649      100.00%
13        global_citations             1649      100.00%
14       global_references             1560       94.60%
15          index_keywords              646       39.18%
16  institution_1st_author             1515       91.87%
17            institutions             1515       91.87%
18                    isbn              428       25.96%
19         iso_source_name             1649      100.00%
20                    issn             1350       81.87%
21         local_citations             1649      100.00%
22        local_references             1000       60.64%
23             num_authors             1649      100.00%
24   num_global_references             1649      100.00%
25              page_start             1174       71.19%
26                pub_year             1649      100.00%
27               pubmed_id               11        0.67%
28     raw_author_keywords             1411       85.57%
29       raw_authors_names             1628       98.73%
30      raw_index_keywords              646       39.18%
31            raw_keywords              591       35.84%
32             source_name             1649      100.00%
33                  volume             1190       72.16%
34         wos_document_id             1649      100.00%

"""

import pandas as pd

from .utils import load_filtered_documents


def coverage(directory=None):
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

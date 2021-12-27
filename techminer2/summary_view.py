"""
Summary View
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> summary_view(directory)
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
23            nlp_abstract              236       95.16%
24      nlp_document_title              247       99.60%
25             nlp_phrases              248      100.00%
26             num_authors              248      100.00%
27   num_global_references              248      100.00%
28              page_start              153       61.69%
29                pub_year              248      100.00%
30               pubmed_id                4        1.61%
31     raw_author_keywords              202       81.45%
32       raw_authors_names              246       99.19%
33      raw_index_keywords               88       35.48%
34            raw_keywords              224       90.32%
35        raw_nlp_abstract              236       95.16%
36  raw_nlp_document_title              247       99.60%
37         raw_nlp_phrases              248      100.00%
38               record_no              248      100.00%
39             source_name              248      100.00%
40                  volume              217       87.50%


"""

import pandas as pd

from .documents_api.load_filtered_documents import load_filtered_documents


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

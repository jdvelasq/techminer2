"""
Summary View
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> summary_view(directory)
                       column  number of terms coverage (%)
0                    abstract              236       95.16%
1                affiliations              244       98.39%
2             author_keywords              202       81.45%
3   author_keywords_thesaurus              202       81.45%
4                     authors              245       98.79%
5                  authors_id              245       98.79%
6           bradford_law_zone              248      100.00%
7                   countries              244       98.39%
8          country_1st_author              244       98.39%
9                 document_id              248      100.00%
10             document_title              248      100.00%
11              document_type              248      100.00%
12                        doi              248      100.00%
13         frac_num_documents              248      100.00%
14           global_citations              248      100.00%
15          global_references              238       95.97%
16             index_keywords               88       35.48%
17     institution_1st_author              236       95.16%
18               institutions              236       95.16%
19                       isbn               13        5.24%
20            iso_source_name              248      100.00%
21                       issn              248      100.00%
22            local_citations              248      100.00%
23           local_references              118       47.58%
24               nlp_abstract              236       95.16%
25         nlp_document_title              247       99.60%
26                nlp_phrases              248      100.00%
27                num_authors              248      100.00%
28      num_global_references              248      100.00%
29                 page_start              153       61.69%
30                   pub_year              248      100.00%
31                  pubmed_id                4        1.61%
32        raw_author_keywords              202       81.45%
33          raw_authors_names              246       99.19%
34         raw_index_keywords               88       35.48%
35               raw_keywords              224       90.32%
36           raw_nlp_abstract              236       95.16%
37     raw_nlp_document_title              247       99.60%
38            raw_nlp_phrases              248      100.00%
39                  record_no              248      100.00%
40                source_name              248      100.00%
41                     volume              217       87.50%

"""

import pandas as pd

from ._read_records import read_filtered_records


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
    documents = read_filtered_records(directory)
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

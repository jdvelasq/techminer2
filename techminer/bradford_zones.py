"""
Bradford Law's zones
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> bradford_zones(directory).head()
                      iso_source_name  num_documents  ...  cum_num_documents    zone
0                      SUSTAINABILITY             15  ...                 15  zone 1
1                     FINANCIAL INNOV             11  ...                 26  zone 1
2  J OPEN INNOV: TECHNOL MARK COMPLEX              8  ...                 34  zone 1
3                        E3S WEB CONF              7  ...                 41  zone 1
4               FRONTIER ARTIF INTELL              5  ...                 46  zone 1
<BLANKLINE>
[5 rows x 5 columns]

>>> bradford_zones(directory).tail()
                           iso_source_name  ...    zone
140                SPRINGERBRIEFS COMP SCI  ...  zone 3
141  STUD UNIV VASILE GOLDIS ARAD ECON SER  ...  zone 3
142                               WEBOLOGY  ...  zone 3
143          WIRELESS COMMUN MOBILE COMPUT  ...  zone 3
144                WORLD ECONOMY INT RELAT  ...  zone 3
<BLANKLINE>
[5 rows x 5 columns]

"""


import numpy as np

from .utils import load_filtered_documents


def bradford_zones(directory="./"):

    documents = load_filtered_documents(directory)
    documents = documents.assign(num_documents=1)
    sources = documents.groupby("iso_source_name", as_index=False).agg(
        {
            "num_documents": np.sum,
            "global_citations": np.sum,
        }
    )
    sources["global_citations"] = sources["global_citations"].map(int)
    sources = sources.sort_values(
        by=["num_documents", "global_citations", "iso_source_name"],
        ascending=[False, False, True],
    )
    sources = sources.reset_index(drop=True)
    sources = sources.assign(cum_num_documents=sources.num_documents.cumsum())
    core_documents = int(len(documents) / 3)
    sources["zone"] = np.where(
        sources.cum_num_documents <= core_documents,
        "zone 1",
        np.where(sources.cum_num_documents <= 2 * core_documents, "zone 2", "zone 3"),
    )

    return sources

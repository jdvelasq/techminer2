"""
Top Documents
============


"""

import pandas as pd
from techminer.utils.datastore import load_datastore


class TopDocuments:
    """
    Class to manage the top documents
    """

    def __init__(
        self,
        datastorepath="./",
        global_citations=True,
        normalized_citations=False,
    ):
        self._datastorepath = datastorepath
        self._global_citations = global_citations
        self._normalized_citations = normalized_citations
        self._datastore = load_datastore(self._datastorepath)
        self._detailed = None
        self._resumed = None

    def _get_top_documents(self):
        """
        Get the top documents.

        """
        data = self._datastore.copy()

        max_year = data.pub_year.dropna().max()

        data["global_normalized_citations"] = data.global_citations.map(
            lambda w: round(w / max_year, 3), na_action="ignore"
        )
        data["local_normalized_citations"] = data.local_citations.map(
            lambda w: round(w / max_year, 3), na_action="ignore"
        )

        data["global_citations"] = data.global_citations.map(int, na_action="ignore")

        citations_column = {
            (True, True): "global_normalized_citations",
            (True, False): "global_citations",
            (False, True): "local_normalized_citations",
            (False, False): "local_citations",
        }[(self._global_citations, self._normalized_citations)]

        data = data.sort_values(citations_column, ascending=False)
        data = data.reset_index(drop=True)

        self._detailed = data[
            [
                "authors",
                "pub_year",
                "document_title",
                "publication_name",
                citations_column,
            ]
        ]

        reference = [
            str(authors) + ". " + str(pub_year) + ". " + str(document_title) + ". "
            for authors, pub_year, document_title, in zip(
                data.authors, data.pub_year, data.document_title
            )
        ]

        self._resumed = pd.DataFrame(
            {"reference": reference, citations_column: data[citations_column]}
        )

    @property
    def detailed_(self):
        """
        Get the top documents.

        """
        if self._detailed is None:
            self._get_top_documents()
        return self._detailed

    @property
    def resumed_(self):
        """
        Get the top documents.

        """
        if self._resumed is None:
            self._get_top_documents()
        return self._resumed

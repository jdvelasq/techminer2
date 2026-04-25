"""
Coverage
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field
    >>> from tm2p.ingest.rec import Coverage
    >>> df = (
    ...     Coverage()
    ...     .with_source_field(Field.AUTHKW_RAW)
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     .run()
    ... )
    >>> assert df.shape[0] > 0
    >>> df.head()  # doctest: +SKIP
       OCC  CUM_SUM_DOCS COVERAGE  CUM_SUM_ITEMS
    0  962           962  64.96 %              1
    1  209          1004  67.79 %              2
    2  169          1049  70.83 %              3
    3  167          1189  80.28 %              4
    4  122          1201  81.09 %              5


"""

from tm2p._intern import ParamsMixin
from tm2p._intern.data_access.load_filtered_main_csv_zip import (
    load_filtered_main_csv_zip,
)
from tm2p.enum import Col


class Coverage(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):

        FIELD = self.params.source_field.value

        documents = load_filtered_main_csv_zip(params=self.params)
        documents = documents.reset_index()
        documents = documents[[FIELD, Col.RID]]

        n_documents = len(documents)

        documents = documents.dropna()
        documents = documents.assign(num_documents=1)
        documents[FIELD] = documents[FIELD].str.split("; ")
        documents = documents.explode(FIELD)

        documents = documents.groupby(by=[FIELD]).agg(
            {"num_documents": "count", Col.RID: list}
        )
        documents = documents.sort_values(by=["num_documents"], ascending=False)

        documents = documents.reset_index()

        documents = documents.groupby(by="num_documents", as_index=False).agg(
            {Col.RID: list, FIELD: list}
        )

        documents = documents.sort_values(by=["num_documents"], ascending=False)
        documents[Col.RID] = documents[Col.RID].apply(
            lambda x: [term for sublist in x for term in sublist]
        )

        documents = documents.assign(cum_sum_documents=documents[Col.RID].cumsum())
        documents = documents.assign(
            cum_sum_documents=documents.cum_sum_documents.apply(set)
        )
        documents = documents.assign(
            cum_sum_documents=documents.cum_sum_documents.apply(len)
        )

        documents = documents.assign(
            coverage=documents.cum_sum_documents.map(
                lambda x: f"{100 * x / n_documents:5.2f} %"
            )
        )

        documents = documents.assign(cum_sum_items=documents[FIELD].cumsum())
        documents = documents.assign(cum_sum_items=documents.cum_sum_items.apply(set))
        documents = documents.assign(cum_sum_items=documents.cum_sum_items.apply(len))

        documents.drop(Col.RID, axis=1, inplace=True)
        documents.drop(FIELD, axis=1, inplace=True)
        documents = documents.reset_index(drop=True)

        documents = documents.rename(
            columns={
                "num_documents": Col.OCC.value,
                "cum_sum_documents": Col.CUM_SUM_DOCS.value,
                "cum_sum_items": Col.CUM_SUM_ITEMS.value,
                "coverage": Col.COVERAGE.value,
            }
        )

        return documents

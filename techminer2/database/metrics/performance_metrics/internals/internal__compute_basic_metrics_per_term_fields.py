# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__compute_basic_metrics_per_term_fields(
    records,
    field,
):
    """:meta private:"""

    records["OCC"] = 1
    grouped_records = records.groupby(field).agg(
        {
            "OCC": "sum",
            "global_citations": "sum",
            "local_citations": "sum",
            "year": "min",
        }
    )
    grouped_records = grouped_records.rename(columns={"year": "first_publication_year"})
    grouped_records["last_year"] = records.year.max()

    grouped_records["age"] = (
        grouped_records["last_year"] - grouped_records["first_publication_year"] + 1
    )
    grouped_records["global_citations_per_year"] = (
        grouped_records["global_citations"] / grouped_records["age"]
    )
    grouped_records["local_citations_per_year"] = (
        grouped_records["local_citations"] / grouped_records["age"]
    )

    grouped_records["global_citations_per_document"] = (
        grouped_records["global_citations"] / grouped_records["OCC"]
    )
    grouped_records["local_citations_per_document"] = (
        grouped_records["local_citations"] / grouped_records["OCC"]
    )

    return grouped_records

import os

import yaml

from .load_all_documents import load_all_documents


def load_filtered_documents(directory):
    """Loads documents from project directory."""
    documents = load_all_documents(directory)

    # Filter documents
    yaml_filename = os.path.join(directory, "filter.yaml")
    with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
        filter_ = yaml.load(yaml_file, Loader=yaml.FullLoader)

    year_min, year_max = filter_["first_year"], filter_["last_year"]
    documents = documents.query(f"pub_year >= {year_min}")
    documents = documents.query(f"pub_year <= {year_max}")

    min_citations, max_citations = filter_["min_citations"], filter_["max_citations"]
    documents = documents.query(f"global_citations >= {min_citations}")
    documents = documents.query(f"global_citations <= {max_citations}")

    bradford = filter_["bradford"]
    documents = documents.query(f"bradford_law_zone <= {bradford}")

    for key, value in filter_.items():
        if key in [
            "first_year",
            "last_year",
            "citations_min",
            "citations_max",
            "bradford",
        ]:
            continue

        if value is False:
            documents = documents.query(f"document_type != '{key}'")

    return documents

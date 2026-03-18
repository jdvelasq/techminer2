def scopus_to_csv(root_directory: str) -> int:
    """:meta private:"""

    from .openalex import openalex_to_csv

    return openalex_to_csv(root_directory)

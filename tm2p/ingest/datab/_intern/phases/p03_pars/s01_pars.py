from ..get_datab_marker import get_datab_marker


def s01_pars(root_directory: str) -> int:
    """:meta private:"""

    from ._intern.openalex import openalex_to_csv
    from ._intern.pubmed import pubmed_to_csv
    from ._intern.scopus import scopus_to_csv
    from ._intern.wos import wos_to_csv

    marker = get_datab_marker(root_directory)
    fn = {
        "OpenAlex": openalex_to_csv,
        "PubMed": pubmed_to_csv,
        "Scopus": scopus_to_csv,
        "WoS": wos_to_csv,
    }.get(marker)

    if fn is not None:
        return fn(root_directory)
    return 0

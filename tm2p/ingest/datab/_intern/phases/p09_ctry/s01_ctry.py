from tm2p import Field
from tm2p.ingest.datab._intern.oper.transform_col import transform_column
from tm2p.ingest.datab._intern.phases.get_datab_marker import get_datab_marker

from ._intern.extract_country_name import extract_country_name_from_string


def s01_ctry(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": None,
        "Scopus": _scopus,
        "WoS": _scopus,
    }[marker]

    if function:
        return transform_column(
            source=Field.AFFIL,
            target=Field.CTRY,
            function=function,
            root_directory=root_directory,
        )
    return 0


def _scopus(series):

    series = series.str.split("; ")
    series = series.map(
        lambda x: [extract_country_name_from_string(y) for y in x], na_action="ignore"
    )
    series = series.str.join("; ")

    return series

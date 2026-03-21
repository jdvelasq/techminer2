import sys

from pandarallel import pandarallel  # type: ignore

from tm2p import Field
from tm2p._intern import stdout_to_stderr
from tm2p.ingest.datab._intern.oper.transform_col import transform_column
from tm2p.ingest.datab._intern.phases.get_datab_marker import get_datab_marker

from ._intern.extract_org_name import extract_org_name_from_string


def s01_org(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": _scopus,
        "Scopus": _scopus,
        "WoS": _scopus,
    }[marker]

    if function:
        return transform_column(
            source=Field.AFFIL,
            target=Field.ORG,
            function=function,
            root_directory=root_directory,
        )

    return 0


def _scopus(series):

    series = series.str.split("; ")

    with stdout_to_stderr():
        progress_bar = True
        pandarallel.initialize(progress_bar=progress_bar, verbose=0)
        series = series.parallel_apply(
            lambda x: (
                [extract_org_name_from_string(y) for y in x]
                if isinstance(x, list)
                else x
            )
        )
        sys.stderr.write("\n")

    series = series.str.join("; ")

    return series

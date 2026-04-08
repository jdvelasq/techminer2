from tm2p.enum import Field
from tm2p.ingest.data_source._intern.oper.transform_col import transform_column
from tm2p.ingest.data_source._intern.phases.get_datab_marker import get_datab_marker


def s02_auth_raw(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": _openalex,
        "PubMed": None,
        "Scopus": _wos,
        "WoS": _wos,
    }[marker]

    if function:
        return function(root_directory)

    return 0


def _openalex(root_directory: str) -> int:

    def _transform(series):
        series = series.copy()
        series = series.str.split("; ")
        series = series.map(
            lambda auths: [
                au.split(" ")[-1]
                + " "
                + "".join([x[0] for x in au.split(" ")[:-1]]).upper()
                for au in auths
            ],
            na_action="ignore",
        )
        series = series.str.join("; ")
        return series

    return transform_column(
        source=Field.AUTH_FULL_NAME,
        target=Field.AUTH_RAW,
        function=_transform,
        root_directory=root_directory,
    )


def _wos(root_directory: str) -> int:

    def _transform(series):
        series = series.copy()
        series = series.str.replace(".", "", regex=False)
        series = series.str.replace(",", "", regex=False)
        return series

    return transform_column(
        source=Field.AUTH_RAW,
        target=Field.AUTH_RAW,
        function=_transform,
        root_directory=root_directory,
    )

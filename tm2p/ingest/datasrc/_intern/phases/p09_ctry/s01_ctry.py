import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.packag_data import load_builtin_mapping
from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper.transform_col import transform_column
from tm2p.ingest.datasrc._intern.phases.get_datab_marker import get_datab_marker

from ._intern.extract_country_name import extract_country_name_from_string


def s01_ctry(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": _openalex,
        "PubMed": _scopus,
        "Scopus": _scopus,
        "WoS": _scopus,
    }[marker]

    return function(root_directory)


def _openalex(root_directory: str) -> int:

    def _extract(text):
        if pd.isna(text):
            return pd.NA
        text = text.split("; ")
        text = [alpha2_to_ctry[i] for i in text if i in alpha2_to_ctry]
        if not text:
            return pd.NA
        text = "; ".join(text)
        return text

    ctry_to_alpha2 = load_builtin_mapping("country_to_alpha2.the.json")
    alpha2_to_ctry = {v: k for k, v in ctry_to_alpha2.items()}

    df = load_main_csv_zip(root_directory)
    df[Field.CTRY.value] = df[Field.CTRY_ISO2.value].map(_extract, na_action="ignore")
    save_main_csv_zip(df, root_directory)

    return 1


def _scopus(root_directory: str) -> int:

    def _process(series):

        series = series.str.split("; ")
        series = series.map(
            lambda x: [extract_country_name_from_string(y) for y in x],
            na_action="ignore",
        )
        series = series.str.join("; ")

        return series

    return transform_column(
        source=Field.AFFIL,
        target=Field.CTRY,
        function=_process,
        root_directory=root_directory,
    )

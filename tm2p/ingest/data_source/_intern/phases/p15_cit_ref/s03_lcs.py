from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.data_source._intern.phases.get_datab_marker import get_datab_marker


def s03_lcs(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)
    function = {
        "OpenAlex": None,
        "PubMed": None,
        "Scopus": _compute,
        "WoS": _compute,
    }[marker]

    if function:
        return function(root_directory=root_directory)

    return 0


def _compute(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    if Field.GCR_WOS_FORMAT.value not in df.columns:
        return 0

    lcr = df[Field.LCR_WOS_FORMAT.value].dropna()
    if not lcr.any():
        return 0
    lcr = lcr.str.split("; ")
    lcr = lcr.explode()
    lcr = lcr.str.strip()
    lcr = lcr.to_list()

    def _process(row):
        rec_id = row[Field.REC_ID.value]
        lcr_ = lcr[:]
        lcr_ = [g for g in lcr_ if rec_id in g]
        lcs = len(lcr_)
        return lcs

    df[Field.LCS.value] = df.apply(_process, axis=1)

    save_main_csv_zip(df=df, root_directory=root_directory)

    return len(df)

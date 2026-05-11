from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s04_n_gcr(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    if Field.GCR_WOS_FORMAT_NORM.value in df.columns:
        # check if all column is empty
        if df[Field.GCR_WOS_FORMAT_NORM.value].isnull().all():
            df[Field.N_GCR.value] = 0
        else:
            df[Field.N_GCR.value] = (
                df[Field.GCR_WOS_FORMAT_NORM.value].str.split("; ").str.len()
            )
    else:
        df[Field.N_GCR.value] = 0

    save_main_csv_zip(df, root_directory)

    return 1

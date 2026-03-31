from tm2p import Field
from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip


def s04_n_gcr(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    if Field.GCR_WOS_FORMAT.value in df.columns:
        # check if all column is empty
        if df[Field.GCR_WOS_FORMAT.value].isnull().all():
            df[Field.N_GCR.value] = 0
        else:
            df[Field.N_GCR.value] = (
                df[Field.GCR_WOS_FORMAT.value].str.split("; ").str.len()
            )
    else:
        df[Field.N_GCR.value] = 0

    save_main_csv_zip(df, root_directory)

    return 1

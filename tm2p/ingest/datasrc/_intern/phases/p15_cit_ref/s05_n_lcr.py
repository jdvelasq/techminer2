from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s05_n_lcr(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    if Field.LCR_WOS_FORMAT.value in df.columns:
        # check if all column is empty
        if df[Field.LCR_WOS_FORMAT.value].isnull().all():
            df[Field.N_LCR.value] = 0
        else:
            df[Field.N_LCR.value] = (
                df[Field.LCR_WOS_FORMAT.value].str.split("; ").str.len()
            )
    else:
        df[Field.N_LCR.value] = 0

    save_main_csv_zip(df, root_directory)

    return 1

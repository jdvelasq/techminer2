from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p._intern.enum import Field


def s01_src(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)
    df[Field.SRC.value] = df[Field.SRC.value].str.upper()
    df[Field.SRC.value] = df[Field.SRC.value].str.replace("<.*?>", "", regex=True)
    save_main_csv_zip(df, root_directory)

    return 1

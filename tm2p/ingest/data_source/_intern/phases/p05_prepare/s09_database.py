from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field

from ..get_datab_marker import get_datab_marker


def s09_database(root_directory: str) -> int:

    marker = get_datab_marker(root_directory)

    df = load_main_csv_zip(root_directory)
    df[Field.DATABASE.value] = marker
    save_main_csv_zip(df, root_directory)

    return 1

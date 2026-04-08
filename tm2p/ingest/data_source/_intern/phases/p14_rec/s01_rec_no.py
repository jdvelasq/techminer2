from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s01_rec_no(root_directory):

    df = load_main_csv_zip(root_directory)

    num_zeros = len(str(len(df)))
    df[Field.REC_NO.value] = [f"{i:0{num_zeros}d}" for i in range(1, len(df) + 1)]

    save_main_csv_zip(df, root_directory)

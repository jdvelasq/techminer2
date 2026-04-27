from string import ascii_lowercase

from tm2p._intern.data_access import load_main_csv_zip, save_main_csv_zip
from tm2p.enum import Field


def s03_rec_short_name(root_directory: str) -> int:

    assigned_names = set()

    df = load_main_csv_zip(root_directory)

    for i, row in df.iterrows():

        auth_first = row[Field.AUTH_FIRST.value]
        year = row[Field.YEAR.value]
        src_iso4 = row[Field.SRC_ISO4.value]

        short_name = f"{auth_first}, {year}, {src_iso4}"

        if short_name in assigned_names:

            for letter in ascii_lowercase:
                short_name_letter = short_name + letter
                if short_name_letter not in assigned_names:
                    short_name = short_name_letter
                    break

        assigned_names.add(short_name)
        df.at[i, Field.REC_SHORT_NAME.value] = short_name

    save_main_csv_zip(df, root_directory)

    return 1

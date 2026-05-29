from tm2p._intern.data_access import load_main_csv_zip
from tm2p._intern.mixins import Params
from tm2p.enum import Field

REC_NO = Field.REC_NO.value
YEAR = Field.YEAR.value
TITLE_RAW = Field.TITLE_RAW.value


def main():

    while True:

        print()
        ut_string = input(". Enter the references string > ").strip()

        if ut_string == "" or ut_string.strip() == "q" or ut_string.strip() == "Q":
            print()
            return

        # [UT 1; UT 2; UT 3]
        # [UT 1, UT 2, UT 3]
        # [UT 1], [UT 2], [UT 3]
        # [UT 1][UT 2][UT 3]
        ut_string = ut_string.replace("], [", "; ")
        ut_string = ut_string.replace(",", ";")
        ut_string = ut_string.replace("][", "; ")
        if ut_string.startswith("[") and ut_string.endswith("]"):
            ut_string = ut_string[1:-1]
        ut_string = ut_string.strip()
        ut_string = ut_string.replace(" UT ", "")
        ut_string = ut_string.replace("UT ", "")
        ut_list = ut_string.split(";")

        ut_list = [int(t) for t in ut_list]
        print(ut_list)

        df = load_main_csv_zip(root_directory="./")
        df = df[df[REC_NO].isin(ut_list)]
        df = df.sort_values(YEAR, ascending=False)  # type: ignore
        print()
        for _, record in df.iterrows():
            print(str(record[YEAR]) + " " + record[TITLE_RAW][:70])


if __name__ == "__main__":
    main()

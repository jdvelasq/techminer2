import os

from techminer2._internals import Params
from techminer2._internals.data_access import load_all_records_from_database
from techminer2.shell.colorized_input import colorized_input


def execute_search_command():

    dirpath = os.path.join("./", "outputs", "section_8_references")

    output_filepath = os.path.join(
        dirpath,
        "reference_counts.txt",
    )

    mapping = {}
    with open(output_filepath, "r", encoding="utf-8") as f:
        for line in f:
            ut, count = line.split("\t")
            ut = ut.replace("UT ", "")
            mapping[ut.strip()] = int(count.strip())

    while True:

        print()
        ut_string = colorized_input(". Enter the references string > ").strip()

        if ut_string == "" or ut_string.strip() == "q" or ut_string.strip() == "Q":
            print()
            return

        # [UT 1; UT 2; UT 3]
        # [UT 1, UT 2, UT 3]
        # [UT 1], [UT 2], [UT 3]
        # [UT 1][UT 2][UT 3]
        ut_string = ut_string.replace("] [", "][")
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
        ut_list = sorted(ut_list, key=lambda x: mapping.get(str(x), 0), reverse=True)
        print(ut_list)

        records = load_all_records_from_database(params=Params(root_directory="./"))
        records = records[records["record_no"].isin(ut_list)]
        records = records.sort_values("year", ascending=False)
        print()
        for record in records.itertuples(index=False):
            print(str(record.year) + " " + record.raw_document_title[:70])

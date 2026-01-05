# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=unused-argument

from colorama import Fore

from techminer2.database.tools import RecordViewer


def execute_view_command():

    file_path = "./outputs/documents.txt"

    file_path_text = file_path
    filename = str(file_path_text).rsplit("/", maxsplit=1)[1]
    file_path_text = file_path_text.replace(filename, f"{Fore.RESET}{filename}")
    file_path_text = Fore.LIGHTBLACK_EX + file_path_text

    print()
    print("Generating records view file...")
    print(f"  File : {file_path_text}")

    viewer = (
        RecordViewer()
        #
        .where_root_directory("./")
        .where_database("main")
        .where_record_years_range(None, None)
        .where_record_citations_range(None, None)
        .where_records_match(None)
        .where_records_ordered_by(None)
    )
    documents = viewer.run()

    with open("./outputs/documents.txt", "w", encoding="utf-8") as f:
        for record in documents:
            f.write(f"{record}\n\n--\n\n")

    print("  Generation process completed successfully\n")

from colorama import Fore, init

from techminer2.database.tools import ExtractColons


def execute_colons_command():

    file_path = "./outputs/texts/colons.txt"

    file_path_text = file_path
    filename = str(file_path_text).split("/")[-1]
    file_path_text = file_path_text.replace(filename, f"{Fore.RESET}{filename}")
    file_path_text = Fore.LIGHTBLACK_EX + file_path_text

    print()
    print("Generating text file...")
    print(f"  File : {file_path_text}")

    contexts = (
        ExtractColons()
        #
        .having_n_chars(20)
        .where_root_directory_is("./")
        .where_database_is("main")
        .where_record_years_range_is(None, None)
        .where_record_citations_range_is(None, None)
        #
        .run()
    )

    with open("./outputs/texts/colons.txt", "w", encoding="utf-8") as f:
        for t in contexts:
            f.write(f"{t}\n")

    print("  Generation process completed successfully\n")


#

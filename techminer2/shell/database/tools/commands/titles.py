from colorama import Fore
from colorama import init
from techminer2.database.tools import SearchString  # type: ignore


def execute_titles_command():

    SearchString().where_root_directory_is("./").run()

    print()
    print("Scopus search string saved to: outputs/scopus_search_string.txt")
    print()

from colorama import Fore, init

from techminer2.tools import SearchString  # type: ignore


def execute_titles_command():

    SearchString().where_root_directory_is("./").run()

    print()
    print("Scopus search string saved to: outputs/scopus_search_string.txt")
    print()

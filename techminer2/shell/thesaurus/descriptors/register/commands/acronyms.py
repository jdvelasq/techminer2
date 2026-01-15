import pathlib
from importlib.resources import files

from colorama import Fore, init

from techminer2._internals.package_data.text_processing import (
    internal__sort_text_processing_terms,
)
from techminer2.shell.colorized_input import colorized_input
from techminer2.thesaurus._internals import internal__load_thesaurus_as_data_frame


def execute_acronyms_command():

    print()

    thesaurus_path = "./data/thesaurus/acronyms.the.txt"
    # internal__print_thesaurus_header(
    #     thesaurus_path,
    #     n=10,
    #     use_colorama=True,
    # )

    answer = colorized_input(
        ". do you want to register new noun phrases from acronyms (y/[n]) > "
    ).strip()
    if answer.lower() == "n":
        print()
        return

    df = internal__load_thesaurus_as_data_frame(thesaurus_path)
    n_acronyms = len(df)

    # prepare terms to insert in the register
    new_terms = df.key.to_list() + df.value.to_list()
    new_terms = [t.strip() for t in new_terms if "_" in t]
    new_terms = list(zip(new_terms, new_terms))
    new_terms = [(t1, t2.split("_")) for t1, t2 in new_terms]
    new_terms = [(t1, [len(w) for w in t2]) for t1, t2 in new_terms]
    new_terms = [(t1, min(t2)) for t1, t2 in new_terms]
    new_terms = [t1 for t1, t2 in new_terms if t2 > 2]

    # insertion
    data_path = files("techminer2.package_data.text_processing.data").joinpath(
        "known_noun_phrases.txt"
    )
    data_path = str(data_path)

    # count the number of lines of the datapath file
    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    n_existent_terms = len(lines)

    with open(data_path, "a", encoding="utf-8") as file:
        for t in new_terms:
            file.write(f"{t}\n")

    internal__sort_text_processing_terms()

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    n_new_total_terms = len(lines)
    n_added_terms = n_new_total_terms - n_existent_terms

    print()
    print(
        f"{n_acronyms}"
        + Fore.LIGHTBLACK_EX
        + " terms founded in acronyms.the.txt"
        + Fore.RESET
    )
    print(
        f"{n_added_terms}"
        + Fore.LIGHTBLACK_EX
        + " added terms to known_noun_phrases.txt"
        + Fore.RESET
    )

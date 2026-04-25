from tm2p._intern.packag_data.word_lists.load_builtin_word_list import (
    load_builtin_word_list,
)
from tm2p._intern.packag_data.word_lists.save_builtin_word_list import (
    save_builtin_word_list,
)


def sort_builtin_word_list(filename: str):

    terms = load_builtin_word_list(filename)
    sorted_terms = sorted(set(terms))
    sorted_terms = [t.replace("_", " ").lower().strip() for t in sorted_terms]
    sorted_terms = sorted(set(sorted_terms), key=lambda x: x[::-1])
    sorted_terms = [t for t in sorted_terms if len(t.split(" ")) > 1]
    save_builtin_word_list(filename, sorted_terms)


if __name__ == "__main__":
    sort_builtin_word_list("rhetorical_scaffolding.txt")

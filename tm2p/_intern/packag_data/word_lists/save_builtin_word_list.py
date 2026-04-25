from importlib.resources import files


def save_builtin_word_list(filename, terms):
    """:meta private:"""

    data_path = files("tm2p._intern.packag_data.word_lists.data").joinpath(filename)
    data_path = str(data_path)

    with open(data_path, "w", encoding="utf-8") as file:
        file.writelines(f"{term}\n" for term in terms)

from importlib.resources import files


def save_text_processing_terms(file_name, terms):
    """:meta private:"""

    data_path = files("techminer2._internals.package_data.word_lists.data").joinpath(
        file_name
    )
    data_path = str(data_path)

    with open(data_path, "w", encoding="utf-8") as file:
        file.writelines(f"{term}\n" for term in terms)

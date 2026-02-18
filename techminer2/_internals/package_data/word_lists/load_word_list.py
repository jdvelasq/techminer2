from importlib.resources import files


def load_word_list(filename: str) -> list[str]:

    data_path = files("techminer2._internals.package_data.word_lists.data").joinpath(
        filename
    )
    data_path = str(data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]

    return lines

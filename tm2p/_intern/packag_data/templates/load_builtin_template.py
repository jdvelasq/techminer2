from importlib.resources import files


def load_builtin_template(filename: str) -> str:

    data_path = files("tm2p._intern.packag_data.templates.data").joinpath(filename)
    data_path_str = str(data_path)

    with open(data_path_str, "r", encoding="utf-8") as file:
        text = file.read()

    return text

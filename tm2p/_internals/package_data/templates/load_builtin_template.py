from importlib.resources import files


def load_builtin_template(filename: str) -> str:

    data_path = files("tm2p.package_data.templates").joinpath(filename)
    data_path = str(data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text

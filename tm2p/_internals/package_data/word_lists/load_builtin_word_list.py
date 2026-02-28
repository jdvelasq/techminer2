from importlib.resources import files


def load_builtin_word_list(filename: str) -> frozenset[str]:

    data_path = files("techminer2._internals.package_data.word_lists.data").joinpath(
        filename
    )

    content = data_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    lines = [line.strip() for line in lines]
    lines = [line for line in lines if line]

    return frozenset(lines)

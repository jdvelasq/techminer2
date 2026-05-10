from importlib.resources import files


def load_builtin_word_list(filename: str) -> frozenset[str]:

    data_path = files("tm2p._intern.packag_data.word_lists.data").joinpath(filename)

    content = data_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    lines = [line.strip() for line in lines]
    lines = sorted(set(line for line in lines if line))

    # from .save_builtin_word_list import save_builtin_word_list

    # save_builtin_word_list(filename, lines)

    return frozenset(lines)

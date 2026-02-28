from importlib.resources import files
from pathlib import Path


def add_new_words_to_builtin_word_list(filename: str, new_words: list[str]) -> None:

    data_path = Path(
        str(files("tm2p._intern.packag_data.word_lists.data").joinpath(filename))
    )

    content = data_path.read_text(encoding="utf-8")

    words = content.splitlines()
    words = [word.strip() for word in words]
    words = [word for word in words if word]

    words_set = set(words)
    words_set.update(new_words)

    text = "\n".join(sorted(words_set))

    data_path.write_text(text, encoding="utf-8")

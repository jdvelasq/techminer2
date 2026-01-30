from pathlib import Path

from techminer2._internals import Params


def load_user_stopwords(params: Params) -> list[str]:
    """:meta private:"""

    file_path = Path(params.root_directory) / "data" / "my_keywords" / "stopwords.txt"

    if not file_path.is_file():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = [line.strip() for line in file.readlines()]

    return stopwords

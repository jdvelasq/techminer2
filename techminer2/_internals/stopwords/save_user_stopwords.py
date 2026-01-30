from pathlib import Path


def save_user_stopwords(params, stopwords):
    """:meta private:"""

    file_path = Path(params.root_directory) / "data" / "my_keywords" / "stopwords.txt"

    with open(file_path, "w", encoding="utf-8") as file:
        for stopword in stopwords:
            file.write(f"{stopword}\n")

    return stopwords

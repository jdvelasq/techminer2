from ..package_data.word_lists import load_word_list


def load_builtin_stopwords() -> list[str]:
    """:meta private:"""

    return load_word_list("technical_stopwords.txt")

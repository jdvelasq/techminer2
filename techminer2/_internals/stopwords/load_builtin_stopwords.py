from ..package_data.word_lists import load_builtin_word_list


def load_builtin_stopwords() -> list[str]:
    """:meta private:"""

    return load_builtin_word_list("stopwords.txt")

from ..package_data.text_processing import load_text_processing_terms


def load_builtin_stopwords() -> list[str]:
    """:meta private:"""

    return load_text_processing_terms("technical_stopwords.txt")

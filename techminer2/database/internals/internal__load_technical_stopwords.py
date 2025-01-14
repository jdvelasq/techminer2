"""Loads technical stopwords.

The file contains a combination of stopwords from the following sources:
- NLTK
- USPTO
- Stopwords in technical language processing (PulsOne)

"""

import pkg_resources  # type: ignore


def internal__load_technical_stopwords():
    """:meta private:"""

    file_path = pkg_resources.resource_filename(
        "techminer2",
        "database/subpackage_data/technical_stopwords.txt",
    )

    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = file.readlines()

    return [stopword.strip() for stopword in stopwords]

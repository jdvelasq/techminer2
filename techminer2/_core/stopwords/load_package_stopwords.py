"""
Loads package stopwords.

"""

import pkg_resources  # type: ignore


def load_package_stopwords():
    """Loads system stopwords.

    :meta private:
    """
    file_path = pkg_resources.resource_filename("techminer2", "word_lists/stopwords.txt")

    ###  module_path = dirname(__file__)
    ### file_path = os.path.join(module_path, "word_lists/stopwords.txt")
    with open(file_path, "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    stopwords = [w.strip() for w in stopwords]
    stopwords = [w for w in stopwords if w != ""]
    return stopwords

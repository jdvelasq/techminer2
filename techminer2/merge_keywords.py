"""
Merge Keywords
===============================================================================

Merge keyword keys in the keywords thesaurus.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> merge_keywords(main_keyword='forecast', keywords_to_merge='prediction',  directory=directory)
forecast
    forecast
    forecasts
    prediction
    predictions

"""

from os.path import isfile, join

from .thesaurus import load_file_as_dict


def merge_keywords(main_keyword, keywords_to_merge, directory="./"):
    """
    Merge keyword keys in the keywords thesaurus.

    """

    thesaurus_file = join(directory, "keywords.txt")
    if isfile(thesaurus_file):
        th = load_file_as_dict(thesaurus_file)
    else:
        raise FileNotFoundError("The file {} does not exist.".format(thesaurus_file))

    reversed_th = {value: key for key, values in th.items() for value in values}

    if main_keyword not in reversed_th:
        raise ValueError(f"The main keyword {main_keyword} does not exist.")

    main_keyword = reversed_th[main_keyword]

    if isinstance(keywords_to_merge, str):
        keywords_to_merge = [keywords_to_merge]

    for keyword in keywords_to_merge:
        if keyword not in reversed_th:
            raise ValueError(f"The keyword {keyword} does not exist.")
        keyword = reversed_th[keyword]
        th[main_keyword].extend(th[keyword])
        th[main_keyword] = sorted(list(set(th[main_keyword])))
        if keyword != main_keyword:
            th.pop(keyword)

    with open(thesaurus_file, "w", encoding="utf-8") as file:
        for key in sorted(th.keys()):
            file.write(key + "\n")
            for item in th[key]:
                file.write("    " + item + "\n")

    print(main_keyword)
    for keyword in th[main_keyword]:
        print("    " + keyword)

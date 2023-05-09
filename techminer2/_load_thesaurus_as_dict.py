def load_thesaurus_as_dict(filename):
    """
    Loads thesaurus data from a text file and returns a dictionary.

    Parameters:
        filename (str): The name of the file containing the thesaurus data.

    Returns:
        A dictionary object containing the thesaurus data.
    """
    dic = {}
    key = None
    values = None
    #
    file = open(filename, "r", encoding="utf-8")
    for word in file:
        word = word.replace("\n", "")
        if len(word.strip()) == 0:
            continue
        if len(word) > 0:
            if word[0] != " ":
                if key is not None:
                    if not values:
                        raise Exception(
                            f"Key '{key}' in file '{filename}' without values associated"
                        )
                    dic[key] = values
                key = word.strip()
                values = []
            else:
                if values is not None and len(word.strip()) > 0:
                    values.append(word.strip())
    # checks the exit
    if key not in dic.keys():
        if values == []:
            raise Exception(
                f"Key '{key}' in file '{filename}' without values associated"
            )
        dic[key] = values
    return dic

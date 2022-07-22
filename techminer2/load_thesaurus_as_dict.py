def load_thesaurus_as_dict(filename):
    #
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
                            "Key '"
                            + key
                            + "' in file '"
                            + filename
                            + "' without values associated"
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
                "Key '" + key + "' in file '" + filename + "' without values associated"
            )
        dic[key] = values
    return dic

import json
from importlib.resources import files
from typing import Union


def update_builtin_mapping(
    filename: str,
    mapping: dict[str, list[str]],
) -> None:

    datapath = files("tm2p._intern.packag_data.mappings.data").joinpath(filename)

    with open(str(datapath), "r", encoding="utf-8") as file:
        existent_mapping = json.load(file)

    for key, value_list in mapping.items():
        if key in existent_mapping:
            existent_mapping[key] += value_list
        else:
            existent_mapping[key] = value_list

    for key, value_list in mapping.items():
        existent_mapping[key] = sorted(set(existent_mapping[key]))

    with open(str(datapath), "w", encoding="utf-8") as file:
        json.dump(
            existent_mapping,
            file,
            indent=4,
            ensure_ascii=False,
            sort_keys=True,
        )

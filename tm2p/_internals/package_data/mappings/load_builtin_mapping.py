import json
from importlib.resources import files
from typing import Union


def load_builtin_mapping(filename: str) -> dict[str, Union[str, list[str]]]:

    datapath = files("tm2p._internals.package_data.mappings.data").joinpath(filename)

    with open(str(datapath), "r", encoding="utf-8") as file:
        return json.load(file)

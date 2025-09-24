# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes


def internal_load_core_area():
    """:meta private:"""

    file_path = "./core_area.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    text = text.strip()

    return text

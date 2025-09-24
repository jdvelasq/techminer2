# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes


def internal_load_aims_and_scope():
    """:meta private:"""

    file_path = "./aims_and_scope.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    return "\n".join(lines)

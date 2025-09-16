# flake8: noqa
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-instance-attributes


from importlib.resources import files


def internal_load_template(template_name):
    """:meta private:"""

    data_path = files("techminer2.package_data.templates").joinpath(template_name)
    data_path = str(data_path)

    with open(data_path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


if __name__ == "__main__":
    template = internal_load_template("shell.thesaurus.descriptors.clean.define.txt")
    print(template)

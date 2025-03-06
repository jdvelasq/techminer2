import os
from pprint import pprint


def read_directory_tree(path):
    files = []
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isdir(full_path):
            files += read_directory_tree(full_path)
        else:
            files.append(full_path)
    return files


def read_package_directories():
    directories = [
        "techminer2/database",
        "techminer2/pkgs",
        "techminer2/search",
        "techminer2/thesaurus",
    ]
    files = []
    for directory in directories:
        files += read_directory_tree(directory)
    files = sorted(files)
    return files


def clean_file_names(files):
    files = [file.replace("techminer2/", "") for file in files]
    files = [file for file in files if "_internals" not in file]
    return files


def generate_index_mapping(files):
    files = files[:]
    files = [file for file in files if not file.endswith("__init__.py")]
    mapping = {}
    for file in files:
        parts = file.split("/")
        path = ".".join(parts[:-1])
        filename = parts[-1]
        if path not in mapping:
            mapping[path] = []
        mapping[path].append(filename)
    return mapping


def complete_keys_in_mapping(mapping):

    new_mapping = {**mapping}
    for key in mapping:
        if "." in key:

            key_parts = key.split(".")

            for i in range(1, len(key_parts)):
                key_part = ".".join(key_parts[:i])
                if key_part not in new_mapping:
                    new_mapping[key_part] = []

            for i in range(1, len(key_parts)):
                parts = key_parts[: i + 1]
                parent = ".".join(parts[:-1])
                child = parts[-1]
                if child not in new_mapping[parent]:
                    new_mapping[parent].append(child)

    return new_mapping


def generate_files(mapping):

    for key, value in mapping.items():
        generate_index_file(key, value)

    for key, value in mapping.items():
        generate_final_files(key, value)


def generate_final_files(key, item):
    for file in item:
        generate_final_file(key, file)


def generate_final_file(key, file):

    if not file.endswith(".py"):
        return

    file = file.replace(".py", "")
    filename = "docs-src/source/" + key + "." + file + ".rst"
    automodule = "techminer2." + key + "." + file

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f".. automodule:: {automodule}\n")
        f.write("     :members:\n")
        f.write("     :undoc-members:\n")
        f.write("     :show-inheritance:\n\n")


def generate_index_file(key, item):

    filename = "docs-src/source/" + key + ".rst"

    with open(filename, "w", encoding="utf-8") as f:
        title = key.split(".")[-1].replace("_", " ").capitalize()
        f.write(title + "\n")
        f.write("#" * 80 + "\n\n")
        f.write(".. toctree::\n")
        f.write("    :maxdepth: 1\n")
        f.write("    :hidden:\n\n")

        for child in item:
            if child.endswith(".py"):
                child = child[:-3]
            f.write("    " + key + "." + child + "\n")


def run():

    files = read_package_directories()
    files = clean_file_names(files)
    mapping = generate_index_mapping(files)
    mapping = complete_keys_in_mapping(mapping)
    generate_files(mapping)


if __name__ == "__main__":
    run()

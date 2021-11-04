def import_raw_file_to_directory(file_name, directory):
    """
    Importa un archivo raw a un directorio.
    """
    with open(file_name, "r") as raw_file:
        with open(directory + "/" + file_name, "w") as file:
            for line in raw_file:
                file.write(line)

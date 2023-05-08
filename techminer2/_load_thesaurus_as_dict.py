def load_thesaurus_as_dict(filename):
    """
    Loads thesaurus data from a text file and returns a dictionary.

    Parameters:
        filename (str): The name of the file containing the thesaurus data.

    Returns:
        A dictionary object containing the thesaurus data.
    """

    thesaurus_dict = {}
    current_key = None
    current_values = None

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            # Check for a new key-value pair
            if not line.startswith(" "):
                # If we already have a key, add it to the dictionary
                if current_key is not None:
                    if not current_values:
                        raise ValueError(
                            f"Key '{current_key}' in file '{filename}' has no associated values."
                        )

                    thesaurus_dict[current_key] = current_values
                    current_values = []

                # Update the current key
                current_key = line
            else:
                # Add a value to the current key
                current_values.append(line)

    # Add the last key-value pair
    if current_key not in thesaurus_dict:
        if not current_values:
            raise ValueError(
                f"Key '{current_key}' in file '{filename}' has no associated values."
            )

        thesaurus_dict[current_key] = current_values

    return thesaurus_dict

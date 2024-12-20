# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def transformations__extract_my_keywords(
    source,
    dest,
    file_name,
    #
    # DATABASE PARAMS:
    root_dir,
):
    #
    # Reads my keywords from file
    file_path = os.path.join(root_dir, "my_keywords", file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        my_keywords = [line.strip() for line in file.readlines()]
        my_keywords = [keyword for keyword in my_keywords if keyword != ""]

    #
    # Computes the intersection per database
    files = list(glob.glob(os.path.join(root_dir, "databases/_*.zip")))
    for file in files:
        #
        # Loads data
        data = pd.read_csv(file, encoding="utf-8", compression="zip", dtype=DTYPES)

        #
        #
        data[dest] = data[source].copy()
        data[dest] = (
            data[dest]
            .str.split("; ")
            .map(lambda x: [z for z in x if z in my_keywords], na_action="ignore")
            .map(set, na_action="ignore")
            .map(sorted, na_action="ignore")
            .str.join("; ")
        )

        data.to_csv(file, sep=",", encoding="utf-8", index=False, compression="zip")

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def transformations__replace_noun_phrases(
    column_to_process,
    noun_phrases_column,
    #
    # DATABASE PARAMS:
    root_dir,
):
    documents_path = pathlib.Path(root_dir) / "databases/_main.csv.zip"
    documents = pd.read_csv(documents_path, encoding="utf-8", compression="zip")

    for index, row in tqdm(documents.iterrows(), total=len(documents)):
        #
        if pd.isna(row[noun_phrases_column]):
            continue
        noun_phrases = row[noun_phrases_column]
        noun_phrases = noun_phrases.lower()
        noun_phrases = noun_phrases.replace("_", " ")
        noun_phrases = noun_phrases.split("; ")
        noun_phrases = sorted(
            noun_phrases, key=lambda x: len(x.split(" ")), reverse=True
        )
        noun_phrases = [re.escape(d) for d in noun_phrases]
        noun_phrases += [r"\(" + d + r"\)" for d in noun_phrases]  # parenthesis
        noun_phrases = "|".join(noun_phrases)
        regex = re.compile(
            r"\b(" + noun_phrases + r")\b",
            flags=re.IGNORECASE,
        )

        new_text = re.sub(
            regex,
            lambda z: z.group().upper().replace(" ", "_"),
            str(row[column_to_process].replace("_", " ")),
        )

        documents.loc[index, column_to_process] = new_text

    documents.to_csv(documents_path, index=False, compression="zip")

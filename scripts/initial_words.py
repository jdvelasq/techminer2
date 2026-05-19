from pathlib import Path

from tm2p._intern import Params
from tm2p.enum import ThField, ThFile
from tm2p.ingest.datasrc import Scopus
from tm2p.refine._intern.data_access import load_thesaurus_as_dataframe
from tm2p.refine.concept.merge import Auto

INDENT = " " * 4
PREFERRED = ThField.PREFERRED.value
VARIANT = ThField.VARIANT.value
GROUP = "GROUP"

# root_directory = "/Volumes/GitHub/_delete/genai/"
# root_directory = "/Volumes/GitHub/_delete/peace/"
# root_directory = "/Volumes/GitHub/_delete/business-analytics/"
# root_directory = "/Volumes/GitHub/_delete/healthcare/"
root_directory = "/Volumes/GitHub/_delete/tech/"

# ---

# root_directory = "tests/tinyml-scopus/"
# root_directory = "tests/system-dynamics-scopus/"
# root_directory = "tests/regtech-scopus/"
# root_directory = "/Volumes/GitHub/_delete/building/"


Scopus().where_root_directory(root_directory).run()


Auto().where_root_directory(root_directory).run()


df = load_thesaurus_as_dataframe(
    params=Params(
        root_directory=root_directory,
        thesaurus_file=ThFile.CONCEPT,
    )
)

df = df.loc[df[PREFERRED].str.split(" ").str.len() > 1, :]
df = df.reset_index(drop=True)

df[GROUP] = [int(i / 4000) for i in df.index.to_list()]

for group in df[GROUP].drop_duplicates().to_list():

    filepath = Path("temp") / f"group_{group:>03d}.txt"
    df_current = df.loc[df.GROUP == group, :]

    with open(filepath, "w", encoding="utf-8") as file:

        for _, row in df_current.iterrows():

            preferred = row[PREFERRED]
            variants = row[VARIANT]

            file.write(f"{preferred}\n")

            # if variants:
            #     for variant in variants.split("; "):
            #         file.write(f"{INDENT}{variant}\n")

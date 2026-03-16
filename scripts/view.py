from pathlib import Path

from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import Field

SIZE = 100


def main():

    for folder in [
        # "openalex",
        # "pubmed",
        # "scopus",
        "wos",
    ]:

        print(f"Processing {folder} ...")

        root_directory = str(Path("tests") / folder)
        df = load_main_csv_zip(root_directory=root_directory).head(50)

        for col in df.columns:
            if df[col].dtype == "object":
                max_size = df[col].str.len().max()
                if max_size > SIZE:
                    df[col] = df[col].str[:SIZE]

        filename = f"_{folder}.txt"
        df = df.head(50)
        df = df[[Field.AFFIL_RAW.value]]
        with open(filename, "w", encoding="utf-8") as txt_file:
            txt_file.write(df.to_markdown(index=False))


if __name__ == "__main__":
    main()

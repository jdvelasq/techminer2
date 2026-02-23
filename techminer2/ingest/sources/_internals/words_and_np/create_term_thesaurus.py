from pathlib import Path

from techminer2 import CorpusField
from techminer2._internals.data_access import load_main_data


def create_term_thesaurus(root_directory: str) -> int:

    dataframe = load_main_data(
        root_directory=root_directory, usecols=[CorpusField.TERM_TOK.value]
    )
    dataframe = dataframe.dropna()
    dataframe = dataframe.rename(columns={CorpusField.TERM_TOK.value: "item"})
    series = dataframe["item"]
    series = series.str.split("; ")
    series = series.explode()
    series = series.str.strip()
    counting = series.value_counts()
    counting_df = counting.to_frame(name="count")
    counting_df = counting_df.reset_index()
    counting_df = counting_df.sort_values(by=["item", "count"], ascending=[True, True])

    filepath = Path(root_directory) / "refine" / "thesaurus" / "terms.the.txt"

    with open(filepath, "w", encoding="utf-8") as file:
        for _, row in counting_df.iterrows():
            term = row["item"]
            file.write(f"{term}\n")
            file.write(f"    {term}\n")
            # file.write(f"    {term} # occ: {row['count']}\n")

    return len(counting_df)

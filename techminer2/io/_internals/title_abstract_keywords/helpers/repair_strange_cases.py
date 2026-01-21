import re
from pathlib import Path

import pandas as pd  # type: ignore
from pandarallel import pandarallel  # type: ignore

from techminer2._internals import stdout_to_stderr


def repair_strange_cases(root_directory: str, source: str, target: str) -> int:

    database_file = Path(root_directory) / "data" / "processed" / "main.csv.zip"

    dataframe = pd.read_csv(
        database_file,
        encoding="utf-8",
        compression="zip",
        low_memory=False,
    )

    if source not in dataframe.columns:
        return 0

    with stdout_to_stderr():
        pandarallel.initialize(progress_bar=True)

    def _repair_text(text):
        if pd.isna(text):
            return text
        text = str(text)
        text = text.replace("_,_", "_")
        text = text.replace("_._", "_")
        text = text.replace(" :_", " : ")
        text = text.replace("_:_", " : ")
        text = text.replace("_S_", "_")
        text = text.replace("_http", " http")
        text = text.replace(" i . E . ", " i . e . ")
        text = text.replace(" . S . ", " . s . ")

        text = text.replace(" i.E. ", " i.e. ")
        text = text.replace(" E.g. ", " e.g. ")
        text = text.replace(" innwind.EU ", " innwind . eu ")
        text = text.replace(" you.s ", " you . s ")
        text = text.replace(" THE_F . E . c .", " the f . e . c .")

        text = text.replace(
            " . THE_CONTRIBUTIONS of THIS_PAPER are : ",
            " . the contributions of this paper are : ",
        )
        text = text.replace(
            ". THE_CONCLUSIONS can be summarized as follows :",
            ". the conclusions can be summarized as follows :",
        )

        return text

    with stdout_to_stderr():
        dataframe[target] = dataframe[source].parallel_apply(_repair_text)

    dataframe.to_csv(
        database_file,
        sep=",",
        encoding="utf-8",
        index=False,
        compression="zip",
    )

    return len(dataframe[target].dropna())

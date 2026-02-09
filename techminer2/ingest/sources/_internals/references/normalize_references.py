import re
from pathlib import Path

import pandas as pd  # type: ignore
from tqdm import tqdm

from techminer2 import CorpusField
from techminer2._internals.data_access import (
    get_references_data_path,
    load_main_data,
    load_references_data,
    save_main_data,
)

_SELECTED_FIELDS = [
    CorpusField.REC_ID.value,
    CorpusField.DOC_TITLE_RAW.value,
    CorpusField.AUTH_RAW.value,
    CorpusField.PUBYEAR.value,
]


def _clean_text(text):
    """:meta private:"""
    text = (
        text.str.lower()
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace(":", "", regex=False)
        .str.replace("-", " ", regex=False)
        .str.replace("_", " ", regex=False)
        .str.replace("'", "", regex=False)
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("  ", " ", regex=False)
    )
    return text


def _prepare_cited_references(root_directory: str) -> pd.DataFrame:

    references = load_main_data(root_directory=root_directory)
    references = references[[CorpusField.REF_RAW.value]].copy()
    references = references.dropna()
    references = references.rename(columns={CorpusField.REF_RAW.value: "text"})
    references["text"] = references["text"].str.split(";")
    references = references.explode("text")
    references["text"] = references["text"].str.strip()
    references = references.drop_duplicates()
    references = references.reset_index(drop=True)
    references["key"] = _clean_text(references["text"])

    return references


def _prepare_main_documents(root_directory: str) -> pd.DataFrame:

    main_df = load_main_data(root_directory=root_directory)

    main_df = main_df[_SELECTED_FIELDS]
    main_df = main_df.dropna()
    references_path = get_references_data_path(root_directory)
    if references_path.exists():
        references_df = load_references_data(root_directory=root_directory)
        references_df = references_df[_SELECTED_FIELDS].dropna()
        dataframe = pd.concat([main_df, references_df], axis=0)
        dataframe = dataframe.drop_duplicates()
    else:
        dataframe = main_df

    dataframe[CorpusField.FIRST_AUTH.value] = (
        dataframe[CorpusField.AUTH_RAW.value]
        .str.split(" ")
        .map(lambda x: x[0].lower().replace(",", ""))
    )
    dataframe[CorpusField.DOC_TITLE_RAW.value] = dataframe[
        CorpusField.DOC_TITLE_RAW.value
    ].str.lower()
    dataframe[CorpusField.DOC_TITLE_RAW.value] = _clean_text(
        dataframe[CorpusField.DOC_TITLE_RAW.value]
    )
    dataframe[CorpusField.AUTH_RAW.value] = _clean_text(
        dataframe[CorpusField.AUTH_RAW.value]
    )
    dataframe[CorpusField.PUBYEAR.value] = dataframe[CorpusField.PUBYEAR.value].astype(
        str
    )
    dataframe = dataframe.sort_values(by=[CorpusField.REC_ID.value])

    return dataframe


def _save_thesaurus(mapping: dict[str, list[str]], root_directory: str) -> None:

    path = Path(root_directory) / "refine" / "thesaurus" / "references.the.txt"
    sorted_keys = sorted(mapping.keys())

    with open(path, "w", encoding="utf-8") as file:
        for key in sorted_keys:
            file.write(f"{key}\n")
            for value in mapping[key]:
                file.write(f"    {value}\n")


def _create_mapping(
    main_documents: pd.DataFrame,
    cited_references: pd.DataFrame,
) -> dict[str, list[str]]:

    mapping = {}
    remaining_references = cited_references.copy()

    for i in tqdm(
        range(main_documents.shape[0]),
        total=main_documents.shape[0],
        bar_format="  {percentage:3.2f}% {bar} | {n_fmt}/{total_fmt} [{rate_fmt}] |",
        ascii=" :",
        ncols=73,
    ):
        row = main_documents.iloc[i]
        refs = remaining_references.copy()

        refs = refs.loc[
            refs.key.str.lower().str.contains(
                row[CorpusField.FIRST_AUTH.value].lower()
            ),
            :,
        ]
        refs = refs.loc[
            refs.key.str.lower().str.contains(row[CorpusField.PUBYEAR.value]), :
        ]

        refs = refs.loc[
            refs.key.str.lower().str.contains(
                re.escape(row[CorpusField.DOC_TITLE_RAW.value][:50].lower())
            ),
            :,
        ]

        if len(refs) > 0:
            mapping[row[CorpusField.REC_ID.value]] = sorted(refs.text.tolist())
            remaining_references = remaining_references.drop(refs.index)

    return mapping


def _get_reverse_mapping(mapping: dict[str, list[str]]) -> dict[str, str]:
    reverse_mapping = {}
    for key, values in mapping.items():
        for value in values:
            reverse_mapping[value] = key
    return reverse_mapping


def _process_references(
    mapping: dict[str, str],
    root_directory: str,
) -> int:

    dataframe = load_main_data(root_directory=root_directory)
    dataframe[CorpusField.REF_NORM.value] = dataframe[CorpusField.REF_RAW.value].copy()
    dataframe[CorpusField.REF_NORM.value] = dataframe[
        CorpusField.REF_NORM.value
    ].str.split(";")
    dataframe[CorpusField.REF_NORM.value] = dataframe[CorpusField.REF_NORM.value].apply(
        lambda refs: (
            [y.strip() for y in refs]
            if isinstance(refs, list)
            else refs if isinstance(refs, list) else refs
        ),
    )
    dataframe[CorpusField.REF_NORM.value] = dataframe[CorpusField.REF_NORM.value].apply(
        lambda refs: (
            [mapping[ref] for ref in refs if ref in mapping]
            if isinstance(refs, list)
            else refs
        ),
    )
    dataframe[CorpusField.REF_NORM.value] = dataframe[
        CorpusField.REF_NORM.value
    ].str.join("; ")

    save_main_data(df=dataframe, root_directory=root_directory)

    non_null_count = int(dataframe[CorpusField.REF_NORM.value].notna().sum())

    return non_null_count


def normalize_references(root_directory: str) -> int:

    cited_references = _prepare_cited_references(root_directory=root_directory)
    main_documents = _prepare_main_documents(root_directory=root_directory)
    mapping = _create_mapping(
        main_documents=main_documents, cited_references=cited_references
    )
    _save_thesaurus(mapping=mapping, root_directory=root_directory)
    reverse_mapping = _get_reverse_mapping(mapping)

    return _process_references(mapping=reverse_mapping, root_directory=root_directory)

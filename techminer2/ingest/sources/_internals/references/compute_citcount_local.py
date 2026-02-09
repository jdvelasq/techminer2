from techminer2 import CorpusField
from techminer2._internals.data_access import load_main_data, save_main_data


def compute_citcount_local(root_directory: str) -> int:

    dataframe = load_main_data(root_directory=root_directory, usecols=None)

    rec_id = dataframe[CorpusField.REC_ID.value].tolist()

    dataframe[CorpusField.CIT_COUNT_LOCAL.value] = dataframe[CorpusField.REF_NORM.value]
    dataframe[CorpusField.CIT_COUNT_LOCAL.value] = dataframe[
        CorpusField.CIT_COUNT_LOCAL.value
    ].fillna("")
    dataframe[CorpusField.CIT_COUNT_LOCAL.value] = dataframe[
        CorpusField.CIT_COUNT_LOCAL.value
    ].str.split("; ")
    dataframe[CorpusField.CIT_COUNT_LOCAL.value] = dataframe[
        CorpusField.CIT_COUNT_LOCAL.value
    ].map(
        lambda refs: [ref.strip() for ref in refs],
    )
    dataframe[CorpusField.CIT_COUNT_LOCAL.value] = dataframe[
        CorpusField.CIT_COUNT_LOCAL.value
    ].map(
        lambda refs: [ref for ref in refs if ref in rec_id],
    )
    dataframe[CorpusField.CIT_COUNT_LOCAL.value] = dataframe[
        CorpusField.CIT_COUNT_LOCAL.value
    ].map(
        len,
    )
    save_main_data(df=dataframe, root_directory=root_directory)

    # import sys

    # for d in dataframe[Field.CITCOUNT_LOCAL.value].value_counts().to_dict().items():
    #     sys.stderr.write(f"{d}\n")
    # sys.stderr.flush()

    return len(dataframe)

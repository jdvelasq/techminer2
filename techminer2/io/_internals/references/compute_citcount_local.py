from techminer2 import Field
from techminer2._internals.data_access import load_main_data, save_main_data


def compute_citcount_local(root_directory: str) -> int:

    dataframe = load_main_data(root_directory=root_directory, usecols=None)

    rec_id = dataframe[Field.RECID.value].tolist()

    dataframe[Field.CITCOUNT_LOCAL.value] = dataframe[Field.REF_NORM.value]
    dataframe[Field.CITCOUNT_LOCAL.value] = dataframe[
        Field.CITCOUNT_LOCAL.value
    ].fillna("")
    dataframe[Field.CITCOUNT_LOCAL.value] = dataframe[
        Field.CITCOUNT_LOCAL.value
    ].str.split("; ")
    dataframe[Field.CITCOUNT_LOCAL.value] = dataframe[Field.CITCOUNT_LOCAL.value].map(
        lambda refs: [ref.strip() for ref in refs],
    )
    dataframe[Field.CITCOUNT_LOCAL.value] = dataframe[Field.CITCOUNT_LOCAL.value].map(
        lambda refs: [ref for ref in refs if ref in rec_id],
    )
    dataframe[Field.CITCOUNT_LOCAL.value] = dataframe[Field.CITCOUNT_LOCAL.value].map(
        len,
    )
    save_main_data(df=dataframe, root_directory=root_directory)

    # import sys

    # for d in dataframe[Field.CITCOUNT_LOCAL.value].value_counts().to_dict().items():
    #     sys.stderr.write(f"{d}\n")
    # sys.stderr.flush()

    return len(dataframe)

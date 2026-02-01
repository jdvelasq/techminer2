from techminer2 import Field
from techminer2._internals.data_access import load_main_data, save_main_data


def create_citcount_local(root_directory: str) -> int:

    dataframe = load_main_data(root_directory=root_directory, usecols=None)
    dataframe[Field.CITCOUNT_LOCAL.value] = int(0)
    save_main_data(df=dataframe, root_directory=root_directory)
    return len(dataframe)

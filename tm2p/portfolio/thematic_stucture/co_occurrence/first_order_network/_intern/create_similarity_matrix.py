import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p._intern.networks.normalize_matrix import normalize_matrix

from ...co_occurrence_matrix.matrix import Matrix as BaseMatrix


def create_similarity_matrix(params: Params) -> pd.DataFrame:

    df = BaseMatrix().update(**params.__dict__).run()
    df = normalize_matrix(params.association_index, df, params=params)

    return df

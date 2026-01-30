import pandas as pd  # type: ignore

from techminer2 import Field
from techminer2.io._internals.operations import DataFile, transform_column


def _normalize(series: pd.Series) -> pd.Series:
    #
    # Cases (do not delete):
    #                                                 1
    # 10040007900; 56255739500; 48361045500; 6506221360
    #                          [No author id available]
    #  58065524100;58065658300;57190620397;55567227600;
    #
    series = series.astype("string")

    mask = series.eq("1") | (series.str.startswith("[") & series.str.endswith("]"))
    series = series.mask(mask.fillna(False), pd.NA)

    series = series.str.replace(r";$", "", regex=True)
    return series


def normalize_author_ids(root_directory: str, file: DataFile) -> int:

    return transform_column(
        source=Field.AUTH_ID_RAW,
        target=Field.AUTH_ID_NORM,
        function=_normalize,
        root_directory=root_directory,
        file=file,
    )


#

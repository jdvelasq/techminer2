import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.datab._intern.oper import transform_column


def s03_disambiguate(root_directory: str) -> int:

    full_name_to_name = _build_author_mapping_wos(root_directory)

    def _disambiguate(series: pd.Series) -> pd.Series:
        return series.str.split(";").apply(
            lambda ids: (
                "; ".join(
                    [full_name_to_name[x.strip()] for x in ids if x.strip() != ""]
                )
                if isinstance(ids, list)
                else None
            )
        )

    count = transform_column(
        source=Field.AUTH_FULL_NAME,
        target=Field.AUTH_RAW,
        function=_disambiguate,
        root_directory=root_directory,
    )

    return count


def _build_author_mapping_wos(root_directory: str) -> dict[str, str]:

    df = load_main_csv_zip(
        root_directory,
        usecols=[Field.AUTH_RAW.value, Field.AUTH_FULL_NAME.value],
    )
    df = df.dropna()

    df[Field.AUTH_RAW.value] = df[Field.AUTH_RAW.value].str.split("; ")
    df[Field.AUTH_RAW.value] = df[Field.AUTH_RAW.value].apply(
        lambda x: [i.strip() for i in x if " " in i]
    )
    df[Field.AUTH_FULL_NAME.value] = df[Field.AUTH_FULL_NAME.value].str.split("; ")

    df = df.explode(
        [
            Field.AUTH_RAW.value,
            Field.AUTH_FULL_NAME.value,
        ]
    )

    df[Field.AUTH_RAW.value] = df[Field.AUTH_RAW.value].str.strip()
    df[Field.AUTH_FULL_NAME.value] = df[Field.AUTH_FULL_NAME.value].str.strip()

    df = df.drop_duplicates(subset=[Field.AUTH_FULL_NAME.value])

    df = df.sort_values(Field.AUTH_RAW.value)
    df["counter"] = df.groupby(Field.AUTH_RAW.value).cumcount()

    mask_collision = df["counter"] > 0
    df.loc[mask_collision, Field.AUTH_RAW.value] += "/" + df.loc[
        mask_collision, "counter"
    ].astype(str)

    return dict(
        zip(
            df[Field.AUTH_FULL_NAME.value].str.replace(";", "").str.strip(),
            df[Field.AUTH_RAW.value],
        )
    )

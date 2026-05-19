import sys

import pandas as pd  # type: ignore

from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import transform_column


def s03_disambiguate(root_directory: str) -> int:

    full_name_to_name = _build_author_mapping(root_directory)

    def _disambiguate(series: pd.Series) -> pd.Series:
        return series.str.split(";").apply(
            lambda ids: (
                "; ".join(
                    [
                        full_name_to_name.get(x.strip(), x.strip())
                        for x in ids
                        if x.strip() != ""
                    ]  #  type: ignore
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


def _build_author_mapping(root_directory: str) -> dict[str, str]:

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
    df[Field.AUTH_FULL_NAME.value] = df[Field.AUTH_FULL_NAME.value].apply(
        lambda x: [y for y in x if y.strip() != ""]
    )

    for index, row in df.iterrows():

        auth_raw = row[Field.AUTH_RAW.value]
        auth_full_name = row[Field.AUTH_FULL_NAME.value]

        if len(row[Field.AUTH_RAW.value]) != len(row[Field.AUTH_FULL_NAME.value]):

            if len(auth_raw) > len(auth_full_name):

                def f(raw):
                    surname = raw.split(" ")[0].strip()
                    first_name = raw.split(" ")[1].strip()
                    fixed_name = first_name + " " + surname
                    for full in auth_full_name:
                        if surname in full:
                            return full
                    return fixed_name

                raw2full = {}
                for raw in auth_raw:
                    raw2full[raw] = f(raw)

                fixed_auth_full_names = [raw2full[raw] for raw in auth_raw]

                df.at[index, Field.AUTH_FULL_NAME.value] = fixed_auth_full_names

            else:

                def g(full):
                    surname = full.split(" ")[-1].strip()
                    first_name = "".join([n[0] for n in full.split(" ")[:-1]])
                    fixed_name = surname + " " + first_name
                    for raw in auth_raw:
                        if surname in raw:
                            return raw
                    return fixed_name

                full2raw = {}
                for full in auth_full_name:
                    full2raw[full] = g(full)

                fixed_raw_names = [full2raw[full] for full in auth_full_name]

                df.at[index, Field.AUTH_RAW.value] = fixed_raw_names

            sys.stderr.write("-" * 80 + "\n\n")
            sys.stderr.write(f"{df.at[index, Field.AUTH_RAW.value]} \n")
            sys.stderr.write(f"{auth_raw} \n\n")
            sys.stderr.write(f"{df.at[index, Field.AUTH_FULL_NAME.value]} \n")
            sys.stderr.write(f"{auth_full_name} \n\n")
            sys.stderr.write("-" * 80 + "\n\n")

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

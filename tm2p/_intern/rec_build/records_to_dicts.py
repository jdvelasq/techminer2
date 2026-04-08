from tm2p.enum import Field


def _get_existent_columns(records, candiate_columns):
    columns_to_report = []
    for criterion in candiate_columns:
        if criterion in records.columns:
            columns_to_report.append(criterion)
    return columns_to_report


def _filter_columns(records, selected_columns):
    records = records[selected_columns]
    return records


def _rename_columns(records, names_mapping):
    records = records.rename(columns=names_mapping)
    return records


def _build_dicts(records):
    return records.to_dict(orient="records")


def records_to_dicts(dataframe, field):

    names_mapping = {
        Field.REC_NO.value: "UT",
        Field.REC_ID.value: "AR",
        Field.TITLE_RAW.value: "TI",
        Field.AUTH_NORM.value: "AU",
        Field.GCS.value: "TC",
        Field.SRC_ISO4.value: "SO",
        Field.YEAR.value: "PY",
        Field.AUTHKW_NORM.value: "DE",
        Field.IDXKW_NORM.value: "ID",
    }
    if field == Field.ABSTR_UPPER:
        names_mapping[Field.ABSTR_UPPER.value] = "AB"
    elif field == Field.ABSTR_RAW:
        names_mapping[Field.ABSTR_RAW.value] = "AB"
    elif field == Field.ABSTR_TOK:
        names_mapping[Field.ABSTR_TOK.value] = "AB"
    else:
        raise ValueError(f"Unsupported field: {field}")

    candiate_columns = names_mapping.keys()

    # dataframe = dataframe.copy()

    columns = _get_existent_columns(dataframe, candiate_columns)
    filtered_df = _filter_columns(dataframe, columns)
    renamed_df = _rename_columns(filtered_df, names_mapping)
    dicts = _build_dicts(renamed_df)

    return dicts

# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


def internal__check_field_types(records):

    if "OCC" in records.columns:
        records["OCC"] = records["OCC"].astype(int)

    if "global_citations" in records.columns:
        records["global_citations"] = records["global_citations"].astype(int)

    if "local_citations" in records.columns:
        records["local_citations"] = records["local_citations"].astype(int)

    if "h_index" in records.columns:
        records["h_index"] = records["h_index"].astype(int)

    if "g_index" in records.columns:
        records["g_index"] = records["g_index"].astype(int)

    return records

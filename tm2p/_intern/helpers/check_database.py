from tm2p.ingest.data_source._intern.phases.get_datab_marker import get_datab_marker


def check_database(root_directory: str):

    db = get_datab_marker(root_directory)
    if db != "WoS":
        raise ValueError("\n\nThe analysis is only available for WoS databases.\n\n")

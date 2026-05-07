from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import abstr_metrics


def s10_abstr_metrics(root_directory: str) -> int:
    return abstr_metrics(root_directory=root_directory)

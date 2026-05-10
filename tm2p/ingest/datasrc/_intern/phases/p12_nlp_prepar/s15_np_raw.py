from tm2p.enum import Field
from tm2p.ingest.datasrc._intern.oper import merge_columns


def s15_np_raw(root_directory: str) -> int:

    return merge_columns(
        sources=(
            Field.NP_ABSTR_RAW,
            Field.NP_TITLE_RAW,
        ),
        target=Field.NP_RAW,
        root_directory=root_directory,
    )

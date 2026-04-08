from tm2p._intern.data_access import load_main_csv_zip
from tm2p.enum import Field
from tm2p.ingest.data_source._intern.oper import transform_column


def s08_doctype(root_directory: str) -> int:

    df = load_main_csv_zip(root_directory)

    if Field.DOCTYPE.value in df.columns:
        return transform_column(
            source=Field.DOCTYPE,
            target=Field.DOCTYPE,
            function=lambda x: x.str.capitalize(),
            root_directory=root_directory,
        )

    return 0

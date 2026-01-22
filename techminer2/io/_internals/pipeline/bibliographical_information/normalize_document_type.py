from techminer2.operations.transform import transform_column


def normalize_document_type(root_directory: str) -> int:

    return transform_column(
        source="raw_document_type",
        target="document_type",
        function=lambda x: x.str.capitalize(),
        root_directory=root_directory,
    )

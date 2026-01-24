from techminer2.operations.transform_column import transform_column


def _local_processing_func(text):
    #
    #              DYNA (Colombia)
    # Sustainability (Switzerland)
    #              npj Clean Water
    # Automotive Engineer (London)
    #
    text = text.str.replace("-", "_", regex=False)
    text = text.str.replace("<.*?>", "", regex=True)
    return text


def normalize_source_title(root_directory: str) -> int:

    return transform_column(
        source="raw_source_title",
        target="source_title",
        function=_local_processing_func,
        root_directory=root_directory,
    )

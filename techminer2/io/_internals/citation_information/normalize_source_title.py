from techminer2 import Field
from techminer2.io._internals.operations import transform_column


def _normalize(text):
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
        source=Field.SRCTITLE_RAW,
        target=Field.SRCTITLE_NORM,
        function=_normalize,
        root_directory=root_directory,
    )

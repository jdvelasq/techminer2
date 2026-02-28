from tm2p import CorpusField


def check_required_corpus_field_enum(
    value: CorpusField, param_name: str
) -> CorpusField:

    if not isinstance(value, CorpusField):
        raise TypeError(f"{param_name} must be a Field, got {type(value).__name__}")

    return value

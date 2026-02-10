from techminer2.refine.thesaurus_old._internals.create_fingerprint import (
    internal__create_fingerprint,
)


def test_full_pipeline():
    result = internal__create_fingerprint("MACHINE_LEARNING")
    assert result == "learning machine"

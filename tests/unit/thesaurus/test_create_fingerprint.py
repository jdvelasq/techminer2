from techminer2.refine.thesaurus_old._internals.create_fingerprint import (
    _convert_to_lowercase,
    _convert_words_to_singular,
    _remove_accents_from_text,
    _remove_stop_particles_from_text,
    _replace_underscores_with_spaces,
    _sort_and_deduplicate_words,
)


def test_underscore_replacement():
    assert _replace_underscores_with_spaces("MACHINE_LEARNING") == "MACHINE LEARNING"


def test_case_normalization():
    assert _convert_to_lowercase("MACHINE LEARNING") == "machine learning"


def test_accent_removal():
    assert _remove_accents_from_text("café") == "cafe"


def test_stop_particle_removal():
    result = _remove_stop_particles_from_text("algorithms for ai", ["for"])
    assert result == "algorithms ai"


def test_singularization():
    assert _convert_words_to_singular(["algorithms"]) == ["algorithm"]


def test_word_order():
    result = _sort_and_deduplicate_words(["learning", "machine"])
    assert result == ["learning", "machine"]

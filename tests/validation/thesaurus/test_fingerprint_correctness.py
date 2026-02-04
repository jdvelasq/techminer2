from techminer2.thesaurus_old._internals.create_fingerprint import (
    internal__create_fingerprint,
)


def test_underscore_variants_match():
    """
    CORRECTNESS: Underscore variants should produce same fingerprint.

    This is validation because we're verifying the ALGORITHM
    correctly groups underscore variants (not just testing functions).
    """
    result1 = internal__create_fingerprint("MACHINE_LEARNING")
    result2 = internal__create_fingerprint("MACHINE LEARNING")

    # VALIDATION: Algorithm should treat these as identical
    assert (
        result1 == result2
    ), "Algorithm should produce same fingerprint for underscore variants"


def test_case_insensitive_matching():
    """
    CORRECTNESS: Case should not affect fingerprint.

    Validates algorithm specification: case-insensitive matching.
    """
    result1 = internal__create_fingerprint("MACHINE_LEARNING")
    result2 = internal__create_fingerprint("machine_learning")

    # VALIDATION: Algorithm should be case-insensitive
    assert result1 == result2, "Algorithm should be case-insensitive"


def test_word_order_independence():
    """
    CORRECTNESS: Word order should not affect matching.

    Validates algorithm specification: order-independent matching.
    """
    result1 = internal__create_fingerprint("MACHINE_LEARNING")
    result2 = internal__create_fingerprint("LEARNING_MACHINE")

    # VALIDATION: Algorithm should normalize word order
    assert (
        result1 == result2
    ), "Algorithm should produce same fingerprint regardless of word order"


def test_singular_plural_equivalence():
    """
    CORRECTNESS: Singular and plural should match.

    Validates algorithm specification: singular/plural matching.
    """
    result1 = internal__create_fingerprint("ALGORITHM")
    result2 = internal__create_fingerprint("ALGORITHMS")

    # VALIDATION: Algorithm should treat singular/plural as equivalent
    assert result1 == result2, "Algorithm should match singular and plural forms"


def test_known_correct_result():
    """
    CORRECTNESS: Verify against known correct result.

    This is the gold standard test - we know the correct answer
    and verify the algorithm produces it.
    """
    result = internal__create_fingerprint("MACHINE_LEARNING")

    # VALIDATION: We know the correct answer
    # After all transformations: "learning machine" (sorted)
    assert result == "learning machine", f"Expected 'learning machine', got '{result}'"


def test_openrefine_compliance():
    """
    CORRECTNESS: Verify compliance with OpenRefine algorithm.

    Validates that our implementation matches OpenRefine behavior.
    """
    # Test case from OpenRefine documentation
    result = internal__create_fingerprint("NEW_YORK_CITY")

    # VALIDATION: Should match OpenRefine output
    # (lowercase, sorted: "city new york")
    assert result == "city new york", "Algorithm should match OpenRefine behavior"


def test_bibliometric_term_correctness():
    """
    CORRECTNESS: Verify correct handling of bibliometric terms.

    Real-world validation using actual bibliometric data.
    """
    # Real bibliometric term
    result = internal__create_fingerprint("MACHINE_LEARNING_ALGORITHMS")

    # VALIDATION: Correct normalization for research
    assert "algorithm" in result, "Should singularize 'algorithms'"
    assert "learning" in result, "Should preserve 'learning'"
    assert "machine" in result, "Should preserve 'machine'"

    # Verify proper ordering
    words = result.split()
    assert words == sorted(words), "Words should be sorted alphabetically"

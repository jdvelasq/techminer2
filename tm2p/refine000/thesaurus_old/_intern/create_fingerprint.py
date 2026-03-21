import unicodedata

from textblob import Word  # type: ignore

PARTICLES: list[str] = [
    "aided",
    "and the",
    "and",
    "applied to",
    "assisted",
    "at",
    "based",
    "for",
    "in",
    "like",
    "of the",
    "of using",
    "of",
    "on",
    "s",
    "sized",
    "to",
    "under",
    "using",
]


def _replace_underscores_with_spaces(text: str) -> str:
    return text.replace("_", " ")


def _replace_hyphens_with_spaces(text: str) -> str:
    return text.replace("-", " ")


def _remove_dots(text: str) -> str:
    return text.replace(".", "")


def _convert_to_lowercase(text: str) -> str:
    return text.lower()


def _remove_accents_from_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_bytes = normalized.encode("ascii", "ignore")
    return ascii_bytes.decode("ascii")


def _remove_stop_particles_from_text(text: str, particles: list[str]) -> str:
    text_with_spaces = f" {text} "
    for particle in particles:
        text_with_spaces = text_with_spaces.replace(f" {particle} ", " ")
    return text_with_spaces.strip()


def _convert_words_to_singular(words: list[str]) -> list[str]:
    return [Word(word).singularize().singularize().singularize() for word in words]


def _sort_and_deduplicate_words(words: list[str]) -> list[str]:
    return sorted(set(words))


def _get_stop_particles() -> list[str]:
    return PARTICLES


def internal__create_fingerprint(text: str) -> str:

    # Normalize separators
    text = _replace_underscores_with_spaces(text)
    text = _replace_hyphens_with_spaces(text)
    text = _remove_dots(text)

    # Normalize case
    text = _convert_to_lowercase(text)

    # Normalize accents
    text = _remove_accents_from_text(text)

    # Remove stop particles
    stop_particles = _get_stop_particles()
    text = _remove_stop_particles_from_text(text, stop_particles)

    # Tokenize and clean
    word_list = text.split()
    cleaned_words = [word.strip() for word in word_list]

    # Singularize
    singular_words = _convert_words_to_singular(cleaned_words)

    # Normalize word order
    sorted_words = _sort_and_deduplicate_words(singular_words)

    # Join back to string
    return " ".join(sorted_words)

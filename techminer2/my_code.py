"""text"""

with open(
    "techminer2/package_data/text_processing/data/hyphenated_is_correct.txt",
    "r",
    encoding="utf-8",
) as file:
    hyphenated_is_correct = [line.strip() for line in file.readlines()]


with open(
    "techminer2/package_data/text_processing/data/hyphenated_is_incorrect.txt",
    "r",
    encoding="utf-8",
) as file:
    hyphenated_is_incorrect = [line.strip() for line in file.readlines()]


words = [
    hyphen
    for hyphen in hyphenated_is_correct
    for non_hyphen in hyphenated_is_incorrect
    if hyphen in non_hyphen
]

print(words)

import pandas as pd

# For each key in thesaurus:
#   Replace XML entities with characters:
#     &amp; → &
#     &lt; →
#     &gt; → >
#     &quot; → "
#     &apos; → '
#     &#39; → '
#     &#[number]; → unicode character
#
#   If key changed:
#     Search for decoded version in thesaurus
#     If exists: merge under decoded version
#     If not: update key to decoded version
#
#
# Before:
# r&amp;d
#     r&amp;d
#
# r&d
#     r&d
#
# machine &amp; learning
#     machine &amp; learning
#
# After:
# r&d
#     r&d
#     r&amp;d
#
# machine & learning
#     machine & learning
#     machine &amp; learning
#


def xml_encoding(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe

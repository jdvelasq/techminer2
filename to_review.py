import csv
import difflib
import re


def load_tsv_columns(path):
    """Parse a TSV file where each column is a cluster."""
    with open(path) as f:
        rows = list(csv.reader(f, delimiter="\t"))
    ncols = len(rows[0])
    cols = [[] for _ in range(ncols)]
    for row in rows[1:]:
        for i in range(ncols):
            if i < len(row) and row[i].strip():
                cols[i].append(row[i].strip())
    return cols


def sing_word(w):
    """Strip a regular English plural ending, returning the singular form."""
    if w.endswith("ies"):
        return w[:-3] + "y"
    if re.search(r"(s|x|z|ch|sh)es$", w):
        return w[:-2]
    if w.endswith("s") and not w.endswith("ss"):
        return w[:-1]
    return w


def norm(w):
    """Comparison key: strip hyphens/spaces, lowercase, singularize."""
    w2 = re.sub(r"[-\s]", "", w.lower())
    return sing_word(w2)


def word_key(w):
    """Comparison key for word-order variants: sorted lowercase word tuple."""
    return tuple(sorted(w.lower().split()))


def find_candidates(path):
    cols = load_tsv_columns(path)
    all_terms = [t for col in cols for t in col]
    terms = list(dict.fromkeys(all_terms))  # dedupe, preserve order
    print("total unique terms:", len(terms))

    # --- Pass 1: hyphen/space + plural normalization ---
    groups = {}
    for t in terms:
        groups.setdefault(norm(t), []).append(t)
    for key, group in groups.items():
        if len(group) > 1:
            print("SPACE/HYPHEN+PLURAL:", group)

    # --- Pass 2: word-order variants ---
    groups2 = {}
    for t in terms:
        groups2.setdefault(word_key(t), []).append(t)
    for key, group in groups2.items():
        if len(group) > 1:
            print("WORD-ORDER:", group)

    # --- Pass 3: fuzzy near-duplicates (typos, spelling variants, etc.) ---
    print("---FUZZY---")
    for t in terms:
        matches = difflib.get_close_matches(t, terms, n=3, cutoff=0.87)
        matches = [m for m in matches if m != t]
        if matches:
            print(t, "~", matches)


find_candidates("units_by_isolated_cluster_XXXX_XXXX.tsv")

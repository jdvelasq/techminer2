import pandas as pd  # type: ignore

from techminer2 import ThesaurusField
from techminer2._internals import Params

from ._post_process import _post_process
from ._pre_process import _pre_process

# from techminer2._internals.package_data import load_builtin_word_list


CHANGED = ThesaurusField.CHANGED.value
IS_KEYWORD = ThesaurusField.IS_KEYWORD.value
OCC = ThesaurusField.OCC.value
OLD = ThesaurusField.OLD.value
PREFERRED = ThesaurusField.PREFERRED.value
SIGNATURE = ThesaurusField.SIGNATURE.value
VARIANT = ThesaurusField.VARIANT.value

# -----------
_STABLE_DOUBLES = {"ll", "ss", "ff", "zz"}

_SILENT_E_CLUSTERS = {
    "rg",
    "ng",
    "lg",
    "dg",
    "rc",
    "nc",
    "bl",
    "pl",
    "gl",
    "fl",
    "lv",
    "rv",
    "nv",
    "yz",
}

_LONG_VOWEL_DIGRAPHS_BLOCK = {"oo", "ee", "ou", "ew", "oi", "oy", "ay", "ue", "oe"}

_NO_E_SUFFIXES = (
    "en",
    "er",
    "el",
    "on",
    "al",
    "an",
    "ain",
    "ard",
    "ent",
    "ant",
    "ect",
    "act",
    "uct",
    "est",
    "ost",
    "ust",
    "ist",
    "ast",
    "ilt",
    "ult",
    "olt",
    "ept",
    "apt",
    "irt",
    "art",
    "urt",
    "ort",
    "eck",
    "ack",
    "ock",
    "uck",
    "ick",
    "alk",
    "ilk",
    "ink",
    "ank",
    "unk",
    "onk",
    "gn",
    "mn",
    "rn",
    "wn",
    "ln",
    "ign",
    "awn",
    "own",
    "op",
    "up",
    "ap",
    "ep",
    "it",
    "ail",
    "oil",
    "eil",
)

_IRREGULARS = {
    "drove": "drive",
    "driven": "drive",
    "drives": "drive",
    "driving": "drive",
    "ran": "run",
    "running": "run",
    "runs": "run",
    "went": "go",
    "gone": "go",
    "goes": "go",
    "going": "go",
    "came": "come",
    "coming": "come",
    "comes": "come",
    "took": "take",
    "taken": "take",
    "takes": "take",
    "taking": "take",
    "made": "make",
    "makes": "make",
    "making": "make",
    "found": "find",
    "finds": "find",
    "finding": "find",
    "led": "lead",
    "leads": "lead",
    "leading": "lead",
    "said": "say",
    "says": "say",
    "saying": "say",
    "saw": "see",
    "seen": "see",
    "sees": "see",
    "seeing": "see",
    "gave": "give",
    "given": "give",
    "gives": "give",
    "giving": "give",
    "got": "get",
    "gotten": "get",
    "gets": "get",
    "getting": "get",
    "knew": "know",
    "known": "know",
    "knows": "know",
    "knowing": "know",
    "grew": "grow",
    "grown": "grow",
    "grows": "grow",
    "growing": "grow",
    "drew": "draw",
    "drawn": "draw",
    "draws": "draw",
    "drawing": "draw",
    "chose": "choose",
    "chosen": "choose",
    "choosing": "choose",
    "chooses": "choose",
    "began": "begin",
    "begun": "begin",
    "begins": "begin",
    "beginning": "begin",
    "built": "build",
    "builds": "build",
    "building": "build",
    "held": "hold",
    "holds": "hold",
    "holding": "hold",
    "kept": "keep",
    "keeps": "keep",
    "keeping": "keep",
    "brought": "bring",
    "brings": "bring",
    "bringing": "bring",
    "showed": "show",
    "shown": "show",
    "shows": "show",
    "showing": "show",
    "arose": "arise",
    "arisen": "arise",
    "arising": "arise",
    "arises": "arise",
    "fell": "fall",
    "falls": "fall",
    "falling": "fall",
    "meant": "mean",
    "means": "mean",
    "meaning": "mean",
    "met": "meet",
    "meets": "meet",
    "paid": "pay",
    "pays": "pay",
    "paying": "pay",
    "sold": "sell",
    "sells": "sell",
    "selling": "sell",
    "sent": "send",
    "sends": "send",
    "sending": "send",
    "stood": "stand",
    "stands": "stand",
    "standing": "stand",
    "thought": "think",
    "thinks": "think",
    "thinking": "think",
    "told": "tell",
    "tells": "tell",
    "telling": "tell",
    "understood": "understand",
    "understands": "understand",
    "understanding": "understand",
    "won": "win",
    "wins": "win",
    "winning": "win",
    "wrote": "write",
    "written": "write",
    "writes": "write",
    "writing": "write",
    "united": "unite",
    "unites": "unite",
    "uniting": "unite",
    "underlying": "underlie",
    "underlies": "underlie",
    "underlay": "underlie",
    "added": "add",
    "adds": "add",
    "adding": "add",
    "called": "call",
    "calls": "call",
    "calling": "call",
    "stalled": "stall",
    "stalls": "stall",
    "stalling": "stall",
    "fallen": "fall",
    "discussed": "discuss",
    "discusses": "discuss",
    "discussing": "discuss",
    "assessed": "assess",
    "assesses": "assess",
    "assessing": "assess",
    "addressed": "address",
    "addresses": "address",
    "addressing": "address",
    "controlling": "control",
    "controlled": "control",
    "controls": "control",
    "cutting": "cut",
    "cuts": "cut",
    "cut": "cut",
    "putting": "put",
    "puts": "put",
    "mapping": "map",
    "mapped": "map",
    "maps": "map",
    "planning": "plan",
    "planned": "plan",
    "plans": "plan",
    "popping": "pop",
    "popped": "pop",
    "pops": "pop",
    "stepping": "step",
    "stepped": "step",
    "steps": "step",
    "spanning": "span",
    "spanned": "span",
    "spans": "span",
    "spurred": "spur",
    "spurs": "spur",
    "spurring": "spur",
    "embedded": "embed",
    "embeds": "embed",
    "embedding": "embed",
    "focuses": "focus",
    "focused": "focus",
    "focusing": "focus",
    "disrupts": "disrupt",
    "disrupted": "disrupt",
    "disrupting": "disrupt",
    "developed": "develop",
    "develops": "develop",
    "developing": "develop",
    "involved": "involve",
    "involves": "involve",
    "involving": "involve",
    "preserved": "preserve",
    "preserves": "preserve",
    "preserving": "preserve",
    "received": "receive",
    "receives": "receive",
    "receiving": "receive",
    "solved": "solve",
    "solves": "solve",
    "solving": "solve",
    "interfered": "interfere",
    "interferes": "interfere",
    "interfering": "interfere",
    "unbundled": "unbundle",
    "unbundles": "unbundle",
    "unbundling": "unbundle",
    "behaves": "behave",
    "behaved": "behave",
    "behaving": "behave",
    "analyzed": "analyze",
    "analyzes": "analyze",
    "analyzing": "analyze",
}

_NON_VERBS = {
    "process",
    "access",
    "success",
    "analysis",
    "basis",
    "crisis",
    "thesis",
    "emphasis",
    "series",
    "status",
    "campus",
    "consensus",
    "corpus",
    "virus",
    "nexus",
    "bonus",
    "iris",
    "debris",
    "alias",
    "gas",
    "class",
    "glass",
    "grass",
    "mass",
    "pass",
    "bass",
    "stress",
    "dress",
    "press",
    "bless",
    "mess",
    "chess",
    "excess",
    "express",
    "regress",
    "suppress",
    "congress",
    "recess",
    "possess",
    # adverbs / adjectives
    "nowadays",
    "speed",
    "unexpected",
    "unprecedented",
    "accredited",
    "excesses",
    "sophisticated",
    "unregulated",
    # compound / domain terms
    "crowdfunding",
    "crowdlending",
    "banking",
    "marketing",
    "processing",
    "engineering",
    "peerreviewed",
    "beijing",
    # base forms
    "focus",
    "disrupt",
    "add",
    "call",
    "fall",
    "sell",
    "tell",
    "discuss",
    "assess",
    "address",
}


def _is_vowel(c):
    return c in "aeiou"


def _is_consonant(c):
    return c.isalpha() and c not in "aeiou"


def _should_add_e(stem: str) -> bool:

    if len(stem) < 2:
        return False

    c1 = stem[-1]
    c2 = stem[-2] if len(stem) >= 2 else ""
    c3 = stem[-3] if len(stem) >= 3 else ""

    if c1 in ("w", "y", "x", "h"):
        return False
    if not _is_consonant(c1):
        return False

    for suf in _NO_E_SUFFIXES:
        if stem.endswith(suf) and len(stem) > len(suf):
            return False

    last2 = stem[-2:] if len(stem) >= 2 else ""
    if last2 in _SILENT_E_CLUSTERS:
        return True

    if not _is_vowel(c2):
        return False  # consonant cluster not in our known list

    if c3 and _is_vowel(c3):
        if (c3 + c2) in _LONG_VOWEL_DIGRAPHS_BLOCK:
            return False
        return True  # 'ea','ie','ei','au' before final consonant -> add e

    return True  # plain CVC ending -> add e


def _lemmatize_verb(word: str) -> str:

    if len(word.split(" ")) > 1:
        return word

    w = word.lower().strip()

    if w in _NON_VERBS:
        return w

    if w in _IRREGULARS:
        base = _IRREGULARS[w]
        return base

    # -ying -> -y  (before general -ing)
    if w.endswith("ying") and len(w) > 5:
        return w[:-4] + "y"

    # -ied -> -y  (before general -ed)
    if w.endswith("ied") and len(w) > 4:
        return w[:-3] + "y"

    # -ies -> -y
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"

    # -ing
    if w.endswith("ing") and len(w) > 5:
        stem = w[:-3]
        last2 = stem[-2:] if len(stem) >= 2 else ""
        if (
            len(stem) >= 2
            and stem[-1] == stem[-2]
            and _is_consonant(stem[-1])
            and last2 not in _STABLE_DOUBLES
        ):
            return stem[:-1]
        if _should_add_e(stem):
            return stem + "e"
        return stem

    # -ed
    if w.endswith("ed") and len(w) > 4:
        stem = w[:-2]
        last2 = stem[-2:] if len(stem) >= 2 else ""
        if (
            len(stem) >= 2
            and stem[-1] == stem[-2]
            and _is_consonant(stem[-1])
            and last2 not in _STABLE_DOUBLES
        ):
            return stem[:-1]

        if _should_add_e(stem):
            return stem + "e"

        return stem

    # -ches / -shes / -xes -> remove 'es'
    for suf in ("ches", "shes", "xes"):
        if w.endswith(suf) and len(w) > len(suf) + 1:
            return w[:-2]

    # silent-e third-person endings: remove final 's'
    for suf in (
        "ces",
        "ves",
        "nes",
        "kes",
        "les",
        "res",
        "tes",
        "ges",
        "zes",
        "ses",
        "pes",
    ):
        if w.endswith(suf) and len(w) > 4:
            return w[:-1]

    # generic -s
    if (
        w.endswith("s")
        and len(w) > 4
        and _is_consonant(w[-2])
        and w[-2] != "s"
        and (len(w) < 3 or w[-2] != w[-3])
    ):
        return w[:-1]

    return w


# -----------


def apply_inflected_verb_forms_rule(
    thesaurus_df: pd.DataFrame,
    params: Params,
) -> pd.DataFrame:

    thesaurus_df = _pre_process(params=params, thesaurus_df=thesaurus_df)
    #
    thesaurus_df[PREFERRED] = thesaurus_df[PREFERRED].apply(_lemmatize_verb)
    #
    thesaurus_df = _post_process(thesaurus_df=thesaurus_df)

    return thesaurus_df

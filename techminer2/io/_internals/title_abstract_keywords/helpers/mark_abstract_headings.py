import re

import pandas as pd  # type: ignore

COMPOUND_STRUCTURED_ABSTRACT_HEADINGS = [
    "actionable insights",
    "aim and background",
    "aim and methods",
    "aims / objectives",
    "application design",
    "applications of this study",
    "authors ' conclusions",
    "background / objectives",
    "background and aims",
    "background and objective",
    "background and purpose",
    "clinical impact",
    "clinical relevance",
    "clinical significance",
    "clinical registration",
    "clinical trial registration",
    "conclusion , significance and impact study",
    "conclusion and relevance",
    "contribution of the paper",
    "data collection and analysis",
    "data sources",
    "data visualization tools",
    "design / methodology / approach",
    "design / methods",
    "design / settings",
    "design methodology approach",
    "discussion and conclusions",
    "diverse perspectives",
    "ethical considerations",
    "ethics and dissemination",
    "findings and originality",
    "findings and value added",
    "graphical abstract",
    "impact and implications",
    "impact statement",
    "implications for practice and policy",
    "implications for practice",
    "implications for theory and practice",
    "improvements / applications",
    "intended outcomes",
    "interests design / methodology / approach",
    "key findings",
    "key messages",
    "key results",
    "limitations and implications",
    "main findings",
    "main measures",
    "main outcome ( s )",
    "main outcome measure",
    "main outcome measures",
    "main outcomes and measures",
    "main results",
    "managerial implications",
    "material / methods",
    "material and methods",
    "materials and methods",
    "methodological quality assessment tools include",
    "methodology / results",
    "methodology and results",
    "methods , procedures , process",
    "methods / statistical analysis",
    "methods and analysis",
    "methods and findings",
    "methods and results",
    "novel / additive information",
    "novelty / originality of this study",
    "novelty / originality",
    "objectives / scope",
    "originality / value",
    "originality and value",
    "outcome measures",
    "paper aims",
    "patient or public contribution",
    "place and duration of study",
    "practical examples",
    "practical implications",
    "practical relevance",
    "practice implications",
    "problem definition",
    "public interest summary",
    "purpose of review",
    "purpose of the article",
    "purpose of the study",
    "recent findings",
    "reporting quality assessment tool",
    "research background",
    "research design",
    "research limitations / implications",
    "research method",
    "research question",
    "results , observations , conclusions",
    "results and discussion",
    "results show",
    "review methods",
    "scholarly critique",
    "scientific discussion",
    "search methods",
    "selection criteria",
    "setting / participants / intervention",
    "settings and participants",
    "social implications",
    "some key results",
    "study design",
    "subjects and methods",
    "subjects and methods",
    "teaching implications",
    "the topics include",
    "theoretical framework",
]


_COMPILED_PATTERNS: list[tuple[str, re.Pattern]] = []


def _get_compiled_patterns() -> list[tuple[str, re.Pattern]]:
    if not _COMPILED_PATTERNS:
        _COMPILED_PATTERNS.extend(
            (phrase, re.compile(r"\b(" + re.escape(phrase) + r")\b"))
            for phrase in COMPOUND_STRUCTURED_ABSTRACT_HEADINGS
        )
    return _COMPILED_PATTERNS


def mark_abstract_headings(text):
    if pd.isna(text):
        return text
    text = str(text)
    for phrase, pattern in _get_compiled_patterns():
        if phrase in text:
            text = pattern.sub(lambda m: m.group().lower().replace(" ", "_"), text)
    return text

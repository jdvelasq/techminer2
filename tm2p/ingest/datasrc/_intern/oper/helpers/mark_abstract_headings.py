import re
from typing import Optional

import pandas as pd  # type: ignore

COMPOUND_STRUCTURED_ABSTRACT_HEADINGS = [
    "a summary",
    "actionable insights",
    "advances in knowledge",
    "aim and background",
    "aim and methods",
    "aims / objectives",
    "application design",
    "applications of this study",
    "authors ' conclusions",
    "background / objectives",
    "background / purpose",
    "background and aims",
    "background and objective",
    "background and purpose",
    "case description",
    "clinical impact",
    "clinical registration",
    "clinical relevance",
    "clinical significance",
    "clinical trial registration",
    "conclusion , significance and impact study",
    "conclusion and clinical relevance",
    "conclusions / significance",
    "conclusion and relevance",
    "conclusions and relevance",
    "contribution of the paper",
    "data collection and analysis",
    "data sources and analytic sample",
    "data sources",
    "data visualization tools",
    "design , setting , and participants",
    "design / methodology / approach",
    "design / methods",
    "design / settings",
    "design methodology approach",
    "discussion and conclusions",
    "discussion and evaluation",
    "diverse perspectives",
    "ethical considerations",
    "ethics and dissemination",
    "findings and originality",
    "findings and value added",
    "full license terms",
    "gov registration",
    "graphical abstract",
    "hypothesis / purpose",
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
    "key points",
    "key results",
    "level of evidence",
    "limitations and implications",
    "limitations of the investigation",
    "main conclusion",
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
    "methodology / approach",
    "methodology / design / approach",
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
    "our contributions include",
    "outcome measures",
    "paper aims",
    "patient or public contribution",
    "patients or other participants",
    "place and duration of study",
    "practical contributions",
    "practical examples",
    "practical implications",
    "practical relevance",
    "practice implications",
    "principal findings",
    "problem definition",
    "public interest summary",
    "purpose of review",
    "purpose of the article",
    "purpose of the study",
    "recent findings",
    "recommendations for future research",
    "reporting methods",
    "reporting quality assessment tool",
    "research aims",
    "research background",
    "research design",
    "research findings",
    "research limitation",
    "research limitations / implications",
    "research method",
    "research question",
    "result and discussion",
    "results , observations , conclusions",
    "results and discussion",
    "results and conclusions",
    "results show",
    "review methods",
    "scholarly critique",
    "scientific discussion",
    "search methods",
    "selection criteria",
    "setting / participants / intervention",
    "settings and design",
    "settings and participants",
    "social implications",
    "some key results",
    "study region",
    "study focus",
    "study design",
    "study results",
    "study setting and design",
    "subjects and methods",
    "subjects and methods",
    "supplementary information",
    "teaching implications",
    "the topics include",
    "theoretical framework",
    "tweetable abstract",
    "type of study",
    "value / originality",
    "setting and design",
    "study region",
    "methods and procedures",
    "research purposes",
    "methodology / principal findings",
    "methods / analysis",
    "omprehensive failure analysis",
]


_PATTERN_CACHE: dict[str, list[re.Pattern]] = {}


def _build_heading_pattern(prefix: str, heading: str) -> re.Pattern:
    escaped_heading = re.escape(heading)
    if prefix == r"^":
        return re.compile(f"^({escaped_heading})( :)", re.IGNORECASE)
    return re.compile(f"({prefix})({escaped_heading})( :)", re.IGNORECASE)


def _get_patterns_for_prefix(prefix: str) -> list[re.Pattern]:
    if prefix not in _PATTERN_CACHE:
        _PATTERN_CACHE[prefix] = [
            _build_heading_pattern(prefix, heading)
            for heading in COMPOUND_STRUCTURED_ABSTRACT_HEADINGS
        ]
    return _PATTERN_CACHE[prefix]


def _normalize_heading_match(match: re.Match) -> str:
    groups = match.groups()
    if len(groups) == 2:
        heading, suffix = groups
        return heading.lower().replace(" ", "_") + suffix
    prefix, heading, suffix = groups
    return prefix + heading.lower().replace(" ", "_") + suffix


def mark_abstract_headings(text: Optional[str]) -> Optional[str]:
    if pd.isna(text):
        return None

    text = str(text)

    for prefix in (r"^", r"\. ", r"\? ", r"\) "):
        for pattern in _get_patterns_for_prefix(prefix):
            text = pattern.sub(_normalize_heading_match, text)

    return text

import re
from typing import Optional

import pandas as pd  # type: ignore

from .mark_abstract_headings import COMPOUND_STRUCTURED_ABSTRACT_HEADINGS

SINGLE_STRUCTURED_ABSTRACT_HEADINGS = [
    "abbreviations",
    "abstract",
    "aim",
    "aims",
    "analysis",
    "animals",
    "applications",
    "approach",
    "background",
    "conclusion",
    "conclusions",
    "condusion",
    "context",
    "contribution",
    "design",
    "discussion",
    "evaluation",
    "evidence",
    "exposure",
    "exposures",
    "features",
    "findings",
    "funding",
    "goal",
    "highlights",
    "impact",
    "implementation",
    "implications",
    "importance",
    "interpretation",
    "intervention",
    "interventions",
    "introduction",
    "justification",
    "keywords",
    "limitations",
    "meaning",
    "method",
    "mediations",
    "methodology",
    "methods",
    "objective",
    "objectives",
    "originality",
    "outcomes",
    "overview",
    "participants",
    "patients",
    "place",
    "procedure",
    "program",
    "purpose",
    "recommendations",
    "result",
    "results",
    "setting",
    "settings",
    "significance",
    "subjects",
    "suggestions",
    "summary",
    "uniqueness",
    "value",
]

_COMPILED_PATTERNS: list[tuple[str, re.Pattern]] = []


def _get_compiled_patterns() -> list[tuple[str, re.Pattern]]:
    if not _COMPILED_PATTERNS:
        _COMPILED_PATTERNS.extend(
            (phrase, re.compile(r"\b(" + re.escape(phrase) + r")\b"))
            for phrase in COMPOUND_STRUCTURED_ABSTRACT_HEADINGS
        )
    return _COMPILED_PATTERNS


def repair_abstract_headings(text: Optional[str]) -> Optional[str]:
    if text is None or pd.isna(text):
        return None
    text = str(text)
    for t in (
        COMPOUND_STRUCTURED_ABSTRACT_HEADINGS + SINGLE_STRUCTURED_ABSTRACT_HEADINGS
    ):

        t_lower = t.lower()
        t_under = t.replace(" ", "_")

        text = re.sub(
            re.compile(rf": {t_under} :", re.IGNORECASE),
            f": {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf": {t} :", re.IGNORECASE),
            f": {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"^ {t_under} :", re.IGNORECASE),
            f" {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"^ {t} :", re.IGNORECASE),
            f" {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf" {t_under} \.", re.IGNORECASE),
            f" {t_lower} .",
            text,
        )

        text = re.sub(
            re.compile(rf" {t} \.", re.IGNORECASE),
            f" {t_lower} .",
            text,
        )

        text = re.sub(
            re.compile(rf"\. {t_under} :", re.IGNORECASE),
            f". {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"\. {t} :", re.IGNORECASE),
            f". {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"\) {t_under} :", re.IGNORECASE),
            f") {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"\) {t} :", re.IGNORECASE),
            f") {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"\? {t_under} :", re.IGNORECASE),
            f"? {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"\? {t} :", re.IGNORECASE),
            f"? {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"' {t_under} :", re.IGNORECASE),
            f"' {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf"' {t} :", re.IGNORECASE),
            f"' {t_lower} :",
            text,
        )

        text = re.sub(
            re.compile(rf" {t_under} \[", re.IGNORECASE),
            f" {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf" {t} \[", re.IGNORECASE),
            f" {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"\. {t_under} \[", re.IGNORECASE),
            f". {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"\. {t} \[", re.IGNORECASE),
            f". {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"\) {t_under} \[", re.IGNORECASE),
            f") {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"\) {t} \[", re.IGNORECASE),
            f") {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"\? {t_under} \[", re.IGNORECASE),
            f"? {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"\? {t} \[", re.IGNORECASE),
            f"? {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"' {t_under} \[", re.IGNORECASE),
            f"' {t_lower} [",
            text,
        )

        text = re.sub(
            re.compile(rf"' {t} \[", re.IGNORECASE),
            f"' {t_lower} [",
            text,
        )

    return text

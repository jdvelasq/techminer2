import re
from typing import List


def extract_org_name_from_string(affiliation: str) -> str:

    # organizations = load_builtin_word_list("organizations.txt")
    # for org in organizations:
    #     if org.lower() in affiliation.lower():
    #         return org

    parts = [_clean_part(p) for p in affiliation.split(",")]
    # parts = [f" {p} " for p in parts if p]

    if not parts:
        return "[UNKNOWN]"

    org = _check_for_university(parts)
    org = _check_for_bank(org, parts)
    org = _check_for_research_center(org, parts)
    org = _check_for_corporate_suffix(org, parts)
    org = _check_for_school(org, parts)
    org = _check_for_center(org, parts)
    org = _check_for_college(org, parts)
    org = _check_for_institute(org, parts)
    org = _check_for_polytechnic(org, parts)
    org = _check_for_association(org, parts)
    org = _check_for_hospital(org, parts)
    org = _check_for_boreau(org, parts)

    return org


def _check_for_boreau(org, parts: List[str]) -> str:

    _BUREAU = [
        "agency",
        "authority",
        "bureau",
        "commission",
        "council",
        "department of",
        "division of",
        "government",
        "ministry",
        "office of",
        "section of",
        "unit of",
        "district",
        "state",
        "ministerio",
        "ministère",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _BUREAU):
            return part.strip()

    return org


def _check_for_hospital(org, parts: List[str]) -> str:

    _HOSPITAL = [
        "hospital",
        "clinic",
        "clinica",
        "clínica",
        "klinik",
        "medical center",
        "medical centre",
        "centre hospitalier",
        "centro médico",
        "centro médico",
        "centro de salud",
        "centro sanitario",
        "centro hospitalar",
        "centro hospitalário",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _HOSPITAL):
            return part.strip()

    return org


def _check_for_association(org, parts: List[str]) -> str:

    _ASSOCIATION = [
        "alianza",
        "alliance",
        "asociación",
        "association",
        "coalition",
        "confederación",
        "confederation",
        "consorcio",
        "consortium",
        "directorate",
        "federación",
        "federation",
        "fondation",
        "foundation",
        "fundacion",
        "fundación",
        "network",
        "sociedad",
        "society",
        "stiftung",
        "union",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _ASSOCIATION):
            return part.strip()

    return org


def _check_for_research_center(org, parts: List[str]) -> str:

    _RESEARCH_CENTER = [
        "research center",
        "research centre",
        "national laboratory",
        "national laboratories",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _RESEARCH_CENTER):
            return part.strip()

    return org


def _check_for_polytechnic(org, parts: List[str]) -> str:

    _POLYTECHNIC = [
        "polytechnic",
        "politecnico",
        "politechnic",
        "politechnische",
        "politechnika",
        "technological university",
        "technische universität",
        "tecnológico",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _POLYTECHNIC):
            return part.strip()

    return org


def _check_for_institute(org, parts: List[str]) -> str:

    _INSTITUTE = [
        "institute",
        "instituto",
        "institut",
        "institutt",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _INSTITUTE):
            return part.strip()

    return org


def _check_for_college(org, parts: List[str]) -> str:

    _COLLEGE = [
        "college",
        "colegio",
        "colégio",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _COLLEGE):
            return part.strip()

    return org


def _check_for_center(org, parts: List[str]) -> str:

    _CENTER = [
        "centre for",
        "center for",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _CENTER):
            return part.strip()

    return org


def _check_for_school(org, parts: List[str]) -> str:

    _SCHOOL = [
        "business school",
        "école de",
        "escola de",
        "escuela de",
        "law school",
        "medical school",
        "school of",
        "university school",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _SCHOOL):
            return part.strip()

    return "[UNKNOWN]"


def _check_for_corporate_suffix(org, parts: List[str]) -> str:

    _CORPORATE_SUFFIX = [
        "ag",
        "b.v.",
        "bv",
        "co.",
        "company",
        "corp",
        "corp.",
        "corporation",
        "gmbh",
        "inc.",
        "inc",
        "incorporated",
        "l.l.c.",
        "limited",
        "llc",
        "ltd.",
        "ltd",
        "plc",
        "s.a.",
        "s.l.",
        "s.p.a.",
        "s.r.l.",
        "spa",
        "srl",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _CORPORATE_SUFFIX):
            return part.strip()

    return "[UNKNOWN]"


def _check_for_bank(org, parts: List[str]) -> str:

    _BANK = [
        "bank",
        "banco",
        "banque",
    ]

    if org != "[UNKNOWN]":
        return org

    for part in parts:
        if any(f" {word} " in part.lower() for word in _BANK):
            return part.strip()

    return "[UNKNOWN]"


def _check_for_university(parts: List[str]) -> str:

    _UNIVERSITY = [
        "rijksuniversiteit",
        "univ",
        "universidad",
        "universidade",
        "università",
        "Universitair",
        "universitas",
        "universität",
        "universitāte",
        "universitatea",
        "université",
        "universiteit",
        "universitet",
        "universiti",
        "university",
        "univerza",
        "univerzita",
        "yliopisto",
        "l'université",
    ]

    for part in parts:
        if any(f" {word} " in part.lower() for word in _UNIVERSITY):
            return part.strip()

    return "[UNKNOWN]"


def _clean_part(part: str) -> str:
    part = part.strip()
    part = re.sub(r"\s*\([^)]*\)\s*$", "", part)
    part = part.strip()
    part = f" {part} "
    return part

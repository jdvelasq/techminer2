"""
Smoke tests:
    >>> from techminer2.thesaurus._internals.thesaurus_match_result import ThesaurusMatchResult
    >>> ThesaurusMatchResult(
    ...     colored_output=False,
    ...     output_file="data/thesaurus/candidates.the.txt",
    ...     thesaurus_file="terms.the.txt",
    ...     msg="Found 15 exact match candidates for merging.",
    ...     success=True,
    ...     num_candidates=15,
    ...     num_groups=8,
    ...     field="all_key_np_word_raw",
    ... )
    INFO: Found 15 exact match candidates for merging.
      Success        : True
      Field          : all_key_np_word_raw
      Thesaurus      : terms.the.txt
      Candidates     : 15
      Groups         : 8
      Output File    : data/thesaurus/candidates.the.txt
    <BLANKLINE>

"""

import os
from dataclasses import dataclass
from typing import Optional

from techminer2._internals.colors import (
    RESET,
    TABLEAU10_BLUE,
    TABLEAU10_IRON,
    TABLEAU10_ORANGE,
)

TRUNCATE_FILEPATH_THRESHOLD = 64
TRUNCATE_FILEPATH_TAIL = 60


def _colorize_file_path(
    file_path: Optional[str], colored_output: bool
) -> Optional[str]:
    if colored_output and file_path is not None:
        filename = os.path.basename(file_path or "")
        file_path = file_path.replace(filename, f"{RESET}{filename}")
        file_path = TABLEAU10_IRON + file_path
    return file_path


def _colorize_msg(msg: Optional[str], colored_output: bool) -> Optional[str]:
    if colored_output and msg is not None:
        msg = f"{TABLEAU10_BLUE}INFO:{RESET} {msg}"
    else:
        msg = f"INFO: {msg}"
    return msg


def _colorize_number(num: int, colored_output: bool) -> str:
    if colored_output:
        return f"{TABLEAU10_ORANGE}{num}{RESET}"
    return str(num)


def _truncate_file_path(file_path: str) -> str:
    if len(file_path) > TRUNCATE_FILEPATH_THRESHOLD:
        file_path = "..." + file_path[-TRUNCATE_FILEPATH_TAIL:]
    return file_path


def _build_output_string(
    output_file: str,
    thesaurus_file: str,
    msg: str,
    success: bool,
    field: str,
    num_candidates: int,
    num_groups: int,
    colored_output: bool,
) -> str:

    truncated_output = _truncate_file_path(output_file)
    colored_output_file = _colorize_file_path(truncated_output, colored_output)
    colored_msg = _colorize_msg(msg, colored_output)
    colored_candidates = _colorize_number(num_candidates, colored_output)
    colored_groups = _colorize_number(num_groups, colored_output)

    text = f"{colored_msg}\n"
    text += f"  Success        : {success}\n"
    text += f"  Field          : {field}\n"
    text += f"  Thesaurus      : {thesaurus_file}\n"
    text += f"  Candidates     : {colored_candidates}\n"
    text += f"  Groups         : {colored_groups}\n"
    text += f"  Output File    : {colored_output_file}\n"

    return text


@dataclass
class ThesaurusMatchResult:
    """Result object for thesaurus matching operations."""

    colored_output: bool = True
    output_file: Optional[str] = None
    thesaurus_file: Optional[str] = None
    msg: Optional[str] = None
    success: bool = False
    field: Optional[str] = None
    num_candidates: int = 0
    num_groups: int = 0

    def __str__(self) -> str:
        return _build_output_string(
            output_file=self.output_file or "",
            thesaurus_file=self.thesaurus_file or "",
            msg=self.msg or "",
            success=self.success,
            field=self.field or "",
            num_candidates=self.num_candidates,
            num_groups=self.num_groups,
            colored_output=self.colored_output,
        )

    def __repr__(self) -> str:
        return self.__str__()

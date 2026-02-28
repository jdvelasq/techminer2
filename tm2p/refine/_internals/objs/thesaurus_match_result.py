"""
Smoke tests:
    >>> from techminer2.refine._internals.objs.thesaurus_match_result import ThesaurusMatchResult
    >>> ThesaurusMatchResult(
    ...     colored_output=False,
    ...     output_file="data/thesaurus/candidates.the.txt",
    ...     thesaurus_file="terms.the.txt",
    ...     msg="Found 15 exact match candidates for merging.",
    ...     success=True,
    ...     field="all_key_np_word_raw",
    ... )
    INFO: Found 15 exact match candidates for merging.
      Success        : True
      Field          : all_key_np_word_raw
      Thesaurus      : terms.the.txt
      Output File    : data/thesaurus/candidates.the.txt
    <BLANKLINE>

"""

import os
from dataclasses import dataclass
from typing import Optional

from tm2p._internals.colors import (
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


def _truncate_file_path(file_path: Optional[str]) -> Optional[str]:
    if file_path is None:
        return None
    if len(file_path) > TRUNCATE_FILEPATH_THRESHOLD:
        file_path = "..." + file_path[-TRUNCATE_FILEPATH_TAIL:]
    return file_path


def _build_output_string(
    output_file: Optional[str],
    thesaurus_file: Optional[str],
    msg: Optional[str],
    success: bool,
    field: Optional[str],
    colored_output: bool,
) -> str:

    truncated_output = _truncate_file_path(output_file)
    colored_output_file = _colorize_file_path(truncated_output, colored_output)
    colored_msg = _colorize_msg(msg, colored_output)

    text = f"{colored_msg}\n"
    text += f"  Success        : {success}\n"
    text += f"  Field          : {field}\n"
    text += f"  Thesaurus      : {thesaurus_file}\n"
    if colored_output_file is not None:
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

    def __str__(self) -> str:
        return _build_output_string(
            output_file=self.output_file,
            thesaurus_file=self.thesaurus_file,
            msg=self.msg,
            success=self.success,
            field=self.field,
            colored_output=self.colored_output,
        )

    def __repr__(self) -> str:
        return self.__str__()

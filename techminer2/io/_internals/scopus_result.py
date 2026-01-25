"""
Scopus Result
===============================================================================


Smoke tests:
    >>> import pandas as pd
    >>> df = pd.DataFrame(
    ...     {
    ...         "key": ["KEY_1", "KEY_2", "KEY_3"],
    ...         "value": [
    ...             "VALUE_1_A; VALUE_1_B; VALUE_1_C; VALUE_1_D; VALUE_1_E; VALUE_1_F; VALUE_1_G; VALUE_1_H",
    ...             "VALUE_2_A; VALUE_2_B",
    ...             "VALUE_3_A; VALUE_3_B; VALUE_3_C"
    ...         ],
    ...     }
    ... )
    >>> # Create thesaurus
    >>> from techminer2.io._internals import ScopusResult
    >>> ScopusResult(
    ...     colored_output=False,
    ...     file_path="examples/fintech/thesauri/organizations.the.txt",
    ...     msg="Thesaurus 'organizations.the.txt' loaded successfully.",
    ...     success=True,
    ...     status=None,
    ...     data_frame=df,
    ... )
    INFO: Thesaurus 'organizations.the.txt' loaded successfully.
      Success : True
      File    : examples/fintech/thesauri/organizations.the.txt
      Header  :
        KEY_1
          VALUE_1_A; VALUE_1_B; VALUE_1_C; VALUE_1_D; VALUE_1_E; VALUE_1_F; VALUE_1...
        KEY_2
          VALUE_2_A; VALUE_2_B
        KEY_3
          VALUE_3_A; VALUE_3_B; VALUE_3_C
    <BLANKLINE>



    >>> ThesaurusResult(
    ...     colored_output=False,
    ...     file_path="examples/fintech/thesauri/organizations.the.txt",
    ...     msg="Thesaurus 'organizations.the.txt' loaded successfully.",
    ...     success=True,
    ...     status="Loaded 10 entries.",
    ...     data_frame=df,
    ... )
    INFO: Thesaurus 'organizations.the.txt' loaded successfully.
      Success : True
      File    : examples/fintech/thesauri/organizations.the.txt
      Status  : Loaded 10 entries.
      Header  :
        KEY_1
          VALUE_1_A; VALUE_1_B; VALUE_1_C; VALUE_1_D; VALUE_1_E; VALUE_1_F; VALUE_1...
        KEY_2
          VALUE_2_A; VALUE_2_B
        KEY_3
          VALUE_3_A; VALUE_3_B; VALUE_3_C
    <BLANKLINE>


"""

# python3 - <<'PY'
# import pandas as pd
# from colorama import init
# from techminer2.thesaurus._internals.result import ThesaurusResult
#
# # enable colorama (autoreset keeps colors from leaking)
# init(autoreset=True)
#
# df = pd.DataFrame(
#     {
#         "key": ["KEY_1", "KEY_2", "KEY_3"],
#         "value": [
#             "VALUE_1_A; VALUE_1_B; VALUE_1_C; VALUE_1_D; VALUE_1_E; VALUE_1_F; VALUE_1_G; VALUE_1_H",
#             "VALUE_2_A; VALUE_2_B",
#             "VALUE_3_A; VALUE_3_B; VALUE_3_C"
#         ],
#     }
# )
#
# r = ThesaurusResult(
#     colorized_output=True,
#     file_path="examples/fintech/thesauri/organizations.the.txt",
#     msg="Thesaurus loaded successfully.",
#     success=True,
#     status="Found 42 entries.",
#     data_frame=df,
# )
# print(r)
# PY

import os
import re
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


def _colorize_status(status: str, colored_output: bool) -> str:

    if colored_output and status != "":

        def _wrap_num(m):
            return f"{TABLEAU10_ORANGE}{m.group(0)}{RESET}"

        status = re.sub(r"\b\d+\b", _wrap_num, status)

    return status


def _truncate_file_path(file_path: str) -> str:
    if len(file_path) > TRUNCATE_FILEPATH_THRESHOLD:
        file_path = "..." + file_path[-TRUNCATE_FILEPATH_TAIL:]
    return file_path


def _build_output_string(
    file_path: str,
    msg: str,
    success: bool,
    status: str,
    colored_output: bool,
) -> str:

    truncated_file_path = _truncate_file_path(file_path)
    colored_file_path = _colorize_file_path(truncated_file_path, colored_output)
    colored_msg = _colorize_msg(msg, colored_output)
    colored_status = _colorize_status(status, colored_output)

    text = f"{colored_msg}\n"
    text += f"  Success : {success}\n"
    text += f"  File    : {colored_file_path}\n"
    if colored_status != "":
        text += f"  Status  : {colored_status}\n"

    return text


@dataclass
class ScopusResult:

    colored_output: bool = True
    file_path: Optional[str] = None
    msg: Optional[str] = None
    success: bool = False
    status: Optional[str] = None

    def __str__(self) -> str:
        return _build_output_string(
            file_path=self.file_path or "",
            msg=self.msg or "",
            success=self.success,
            status=self.status or "",
            colored_output=self.colored_output,
        )

    def __repr__(self) -> str:
        return self.__str__()

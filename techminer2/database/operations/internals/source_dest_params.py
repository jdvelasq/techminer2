# flake8: noqa
# pylint: disable=too-few-public-methods

from dataclasses import dataclass
from typing import Optional


@dataclass
class SourceDestParams:
    """:meta private:"""

    source: Optional[str] = None
    dest: Optional[str] = None
    root_dir: str = "./"

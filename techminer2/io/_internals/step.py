from dataclasses import dataclass
from typing import Callable


@dataclass
class Step:
    name: str
    function: Callable
    kwargs: dict
    count_message: str = ""

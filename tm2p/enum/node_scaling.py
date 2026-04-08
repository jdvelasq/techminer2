from enum import Enum


class NodeScaling(str, Enum):

    LINEAR = "LINEAR"
    LOG = "LOG"
    SQRT = "SQRT"

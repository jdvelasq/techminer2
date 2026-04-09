from enum import Enum


class Scaling(str, Enum):

    LINEAR = "LINEAR"
    LOG = "LOG"
    SQRT = "SQRT"

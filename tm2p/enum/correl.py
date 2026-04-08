from enum import Enum


class Correlation(str, Enum):

    PEARSON = "PEARSON"
    SPEARMAN = "SPEARMAN"
    KENDALL = "KENDALL"
    COSINE = "COSINE"
    MAXPROPORTIONAL = "MAXPROPORTIONAL"

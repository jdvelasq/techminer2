"""
Explode a column into multiple columns.

"""


def explode(x, column, sep):
    """
    explode
    """

    if x[column].dtype != "int64":
        x = x.copy()
        x[column] = x[column].map(
            lambda w: sorted(list(set(w.strip().split(sep))))
            if isinstance(w, str)
            else w
        )
        x = x.explode(column)
        x[column] = x[column].map(lambda w: w.strip() if isinstance(w, str) else w)
        x = x.reset_index(drop=True)
    return x

import textwrap


def dicts_to_strings(dicts):

    column_order = [
        "UT",
        "AR",
        "TI",
        "AU",
        "TC",
        "SO",
        "PY",
        "AB",
        "DE",
        "ID",
    ]

    strings = []

    for record in dicts:
        text = ""
        for col in column_order:
            if record[col] is not None and str(record[col]) != "nan":
                text += col + " "
                text += textwrap.fill(
                    str(record[col]),
                    width=79,
                    initial_indent=" " * 3,
                    subsequent_indent=" " * 3,
                    fix_sentence_endings=True,
                )[3:]
                text += "\n"

        strings += [text]

    return strings

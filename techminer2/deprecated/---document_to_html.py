import textwrap

import pandas as pd

colors = ["#FF6433", "#2E86C1", "#2EA405"] * 10


def document_to_html(document):

    HTML = ""
    if "document_title" in document.index:
        HTML += "           document_title : " + document.document_title + "<br>"
    if "pub_year" in document.index:
        HTML += "                 pub_year : " + str(document.pub_year) + "<br>"
    if "authors" in document.index:
        authors = document.authors.split("; ")
        HTML += "                 authors : " + authors[0] + "<br>"
        if len(authors) > 1:
            for author in authors[1:]:
                HTML += "                           " + author + "<br>"

    if "abstract" in document.index:
        abstract = textwrap.fill(
            document.abstract,
            width=120,
            initial_indent=" " * 28,
            subsequent_indent=" " * 28,
            fix_sentence_endings=True,
        )[27:]

        abstract = abstract.split("\n")
        HTML += "                 abstract : " + abstract[0] + "<br>"

    return "<pre>" + HTML + "</pre>"

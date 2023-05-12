"""
Text Screening
===============================================================================

This funcion searchs for them specified in the parameter ``search_for`` in the
abstracts of the records and creates a file with the report.

>>> directory = "data/regtech/"

>>> from techminer2 import tlab
>>> tlab.lexical_tools.text_screening(
...     search_for='regtech',
...     directory=directory,
... )
--INFO-- The file 'data/regtech/reports/text_screening.txt' was created


"""
import os.path
import sys
import textwrap

from ..._load_abstracts import load_abstracts
from ..._read_records import read_records
from ..concordances.concordances import _select_abstracts

# from ..._load_template import load_template
# from ..._save_html_report import save_html_report


def text_screening(
    search_for,
    # top_n=5,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Checks the occurrence contexts of a given text in the abstract's phrases."""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    abstracts = load_abstracts(directory)
    abstracts = abstracts[abstracts.article.isin(records.article)]
    abstracts = _join_phrases(abstracts)
    abstracts = _select_abstracts(abstracts, search_for)
    # _create_report(directory, abstracts)
    # abstracts = abstracts.head(top_n)
    _print_abstracts(directory, abstracts)


def _join_phrases(abstracts):
    abstracts = abstracts.copy()
    abstracts = abstracts.sort_values(
        ["global_citations", "article", "line_no"], ascending=[False, True, True]
    )
    abstracts = abstracts.groupby(["article", "global_citations"], as_index=False).agg(
        list
    )
    abstracts.phrase = abstracts.phrase.str.join(" ")
    return abstracts


# def _create_report(directory, abstracts):

#     abstracts = abstracts.copy()
#     abstracts = abstracts[["article", "phrase"]]
#     abstracts = abstracts.groupby("article", as_index=False).aggregate(
#         lambda x: " <br> ".join(x)
#     )

#     report_name = "text_screening.html"
#     template = load_template(report_name)
#     html = template.render(
#         concordances=zip(abstracts.article.tolist(), abstracts.phrase.tolist())
#     )
#     save_html_report(directory, html, report_name)


def _print_abstracts(directory, abstracts):
    file_path = os.path.join(directory, "reports/text_screening.txt")
    prompt = '''Summarize the text delimited between """ and """ in the following lines, in 50 words or less.
    
"""

"""
'''

    with open(file_path, "w", encoding="utf-8") as file:
        print("-" * 80, file=file)
        print(prompt, file=file)
        print("-" * 80, file=file)

        for article, phrase in zip(abstracts.article, abstracts.phrase):
            print("*** " + article, file=file)

            text = textwrap.fill(phrase, width=80)
            text = text.split("\n")
            text = [x.strip() for x in text]
            text = " \\\n".join(text)
            text = '\n"""\n' + text + '\n"""'

            print(text, file=file)
            print(file=file)
            print(file=file)

    sys.stdout.write(f"--INFO-- The file '{file_path}' was created\n")

"""
Keywords Summarization
===============================================================================

# >>> directory = "data/regtech/"

# >>> from techminer2 import tm2__keywords_summarization
# >>> tm2__keywords_summarization(
# ...     column="author_keywords",
# ...     keywords=["fintech", "blockchain"],
# ...     n_phrases=5,    
# ...     directory=directory,
# ... )
# --INFO-- Generating data/regtech/reports/keywords_summarization.txt

"""
import sys
import textwrap
from os.path import isfile, join

from ._load_thesaurus_as_dict import load_thesaurus_as_dict
from ._read_records import read_records


def tm2__keywords_summarization(
    column,
    keywords=None,
    n_phrases=10,
    sufix="",
    directory="./",
):
    def expand_keywords(keywords):
        #
        # Expands the original keywords list to the equivalent keywords in the thesaurus.
        #
        thesaurus_file = join(directory, "processed", "keywords.txt")
        if isfile(thesaurus_file):
            th = load_thesaurus_as_dict(thesaurus_file)
        else:
            raise FileNotFoundError(
                "The file {} does not exist.".format(thesaurus_file)
            )

        # extract keys for thesaurus
        reversed_th = {value: key for key, values in th.items() for value in values}
        th_keys = []
        for keyword in keywords:
            th_keys.append(reversed_th[keyword])
        expanded_keywords = [text for key in th_keys for text in th[key]]

        return expanded_keywords

    def select_documents(documents, column, expanded_keywords):
        documents = documents.copy()
        documents["_points_"] = 0
        documents["title"] = documents["title"].str.lower()

        for keyword in expanded_keywords:
            documents.loc[
                documents.title.str.contains(keyword, regex=False), "_points_"
            ] += 3

        for keyword in expanded_keywords:
            documents.loc[
                documents.abstract.str.contains(keyword, regex=False, na=False),
                "_points_",
            ] += 1

        #
        documents[column] = documents[column].str.split(";")
        documents[column] = documents[column].map(
            lambda x: [item.strip() for item in x] if isinstance(x, list) else x
        )
        documents[column] = documents[column].map(
            lambda x: len(set(expanded_keywords) & set(x)) if isinstance(x, list) else 0
        )
        documents["_points_"] = documents["_points_"] + documents[column]
        #
        documents = documents[documents._points_ > 0]
        documents = documents.sort_values(
            by=["_points_", "global_citations"], ascending=False
        )

        for keyword in expanded_keywords:
            keyword = keyword.replace("(", "\(").replace(")", "\)")
            keyword = keyword.replace("[", "\[").replace("]", "\]")
            documents["title"] = documents["title"].str.replace(
                r"\b" + keyword + r"\b", keyword.upper()
            )

            documents["abstract"] = documents["abstract"].str.replace(
                r"\b" + keyword + r"\b", keyword.upper()
            )

        return documents

    def write_report(documents, sufix):

        # ----< select columns to report >-----------------------------------------------
        documents = documents.copy()
        column_list = []
        reported_columns = [
            "title",
            "authors",
            "global_citations",
            "source_title",
            "year",
            "abstract",
        ]
        for column in reported_columns:
            if column in documents.columns:
                column_list.append(column)
        documents = documents[column_list]

        # ----< report >-----------------------------------------------------------------
        filename = join(directory, "reports", f"keywords_summarization{sufix}.txt")

        with open(filename, "w") as out_file:

            sys.stdout.write("--INFO-- Generating " + filename + "\n")

            for index, row in documents.iterrows():

                for column in reported_columns:

                    if column not in row.index:
                        continue

                    if column == "title":
                        print("      title :", end="", file=out_file)
                        print(
                            textwrap.fill(
                                row[column],
                                width=115,
                                initial_indent=" " * 23,
                                subsequent_indent=" " * 23,
                                fix_sentence_endings=True,
                            )[22:],
                            file=out_file,
                        )
                        continue

                    if column == "abstract":

                        if not isinstance(row[column], float):
                            print("            abstract :", end="", file=out_file)
                            print(
                                textwrap.fill(
                                    row[column],
                                    width=115,
                                    initial_indent=" " * 23,
                                    subsequent_indent=" " * 23,
                                    fix_sentence_endings=True,
                                )[22:],
                                file=out_file,
                            )
                        continue

                    print(" {:>19} : {}".format(column, row[column]), file=out_file)

                if index != documents.index[-1]:
                    print(
                        "-" * 120,
                        file=out_file,
                    )

    # ----< data must be a list >--------------------------------------------------------
    if isinstance(keywords, str):
        keywords = [keywords]
    keywords = [word for word in keywords if word != ""]

    documents = read_records(directory)
    expanded_keywords = expand_keywords(keywords)
    documents = select_documents(documents, column, expanded_keywords)
    documents = documents.head(n_phrases)
    write_report(documents, sufix)

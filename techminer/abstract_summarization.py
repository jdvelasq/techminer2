import os
import textwrap

import nltk
import pandas as pd
from nltk.stem import PorterStemmer


def abstract_summarization(directory, texts, n_phrases=10, sufix=""):

    if isinstance(texts, str):
        texts = [texts]

    porter_stemmer = PorterStemmer()

    file_name = os.path.join(directory, "abstracts.csv")
    abstracts = pd.read_csv(file_name)
    documents = pd.read_csv(os.path.join(directory, "documents.csv"))

    regex = r"\b(" + "|".join(texts) + r")\b"

    abstracts = abstracts[abstracts.text.str.contains(regex, regex=True)]
    abstracts = abstracts[["record_no", "text"]]

    #
    abstracts["formatted_text"] = abstracts.text.copy()
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(
        r"[[0-9]]*", " "
    )
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(r"s+", " ")
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(
        r"[a-zA-Z]", " "
    )
    abstracts["formatted_text"] = abstracts["formatted_text"].str.replace(r"s+", " ")
    #
    stopwords = nltk.corpus.stopwords.words("english")
    word_frequencies = {}
    for phrase in abstracts["formatted_text"].values:
        for word in nltk.word_tokenize(phrase):
            word = porter_stemmer.stem(word)
            if word not in stopwords:
                if word not in word_frequencies.keys():
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
    #
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / maximum_frequncy

    #
    abstracts["sentence_scores"] = 0
    for index, row in abstracts.iterrows():
        for word in nltk.word_tokenize(row["formatted_text"]):
            word = porter_stemmer.stem(word)
            if word in word_frequencies.keys():
                abstracts.at[index, "sentence_scores"] += word_frequencies[word]

        # length = len(nltk.word_tokenize(row["formatted_text"]))
        # abstracts.at[index, "sentence_scores"] /= max(1, length)

    abstracts = abstracts.sort_values(by=["sentence_scores"], ascending=False)

    abstracts = abstracts.head(n_phrases)
    abstracts["text"] = abstracts.text.str.capitalize()

    for text in texts:
        abstracts["text"] = abstracts["text"].str.replace(text, text.upper())
        abstracts["text"] = abstracts["text"].str.replace(
            text.capitalize(), text.upper()
        )

    with open(
        os.path.join(directory, f"abstract_summarization{sufix}.txt"), "w"
    ) as out_file:
        for index, row in abstracts.iterrows():
            paragraph = textwrap.fill(
                row["text"],
                width=90,
            )
            document_id = documents[documents.record_no == row["record_no"]].document_id
            document_id = document_id.iloc[0]
            print("*** " + document_id, file=out_file)
            print(paragraph, file=out_file)
            print("\n", file=out_file)

    summary = ". ".join(abstracts.text.values)
    return summary

    # return abstracts

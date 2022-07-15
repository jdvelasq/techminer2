# def _complete__source_abbr__column(directory):
#     #
#     def load_iso4_csv():
#         module_path = os.path.dirname(__file__)
#         file_path = os.path.join(module_path, "files/iso4.csv")
#         iso4 = pd.read_csv(file_path, sep=",")
#         return iso4

#     def get_source_abbr():
#         iso4data = []
#         files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
#         for file in files:
#             data = pd.read_csv(file, encoding="utf-8")
#             iso4data.append(data.source_abbr.dropna())
#         iso4data = pd.concat(iso4data)
#         return iso4data

#     def get_words2abbr(table):
#         #
#         table = table.copy()
#         table = table.dropna()
#         #
#         table = table.str.replace(" AND ", "")
#         table = table.str.replace(" IN ", "")
#         table = table.str.replace(" OF ", "")
#         table = table.str.replace(" ON ", "")
#         table = table.str.replace(" THE ", "")
#         table = table.str.split()
#         table = table.explode()
#         table = table.drop_duplicates()
#         table = table.to_frame()
#         table = table.reset_index(drop=True)
#         table = table.rename(columns={"source_abbr": "name"})
#         table = table.assign(iso4=table.name)

#         # ---------------------------------------------------------------------
#         # builds the dictionary
#         iso4_abrev = load_iso4_csv()
#         complete_words = {
#             name: abbr
#             for name, abbr in zip(iso4_abrev.WORDS, iso4_abrev.ABBREVIATIONS)
#             if "-" not in name
#         }
#         table.iso4 = table.iso4.replace(complete_words)

#         # ---------------------------------------------------------------------
#         # endswith replacement
#         ends_dict = {
#             name: abbr
#             for name, abbr in zip(iso4_abrev.WORDS, iso4_abrev.ABBREVIATIONS)
#             if name[0] == "-" and name[-1] != "-"
#         }

#         for key, value in ends_dict.items():
#             table = table.assign(
#                 iso4=table.iso4.str.replace(
#                     key[1:] + r"\b",
#                     value[1:],
#                     regex=True,
#                 )
#             )

#         # ---------------------------------------------------------------------
#         # startswith replacement
#         begins_dict = {
#             key: value
#             for key, value in table.items()
#             if key[0] != "-" and key[-1] == "-"
#         }

#         for key, value in begins_dict.items():
#             table = table.assign(
#                 iso4=table.iso4.map(
#                     lambda x: begins_dict[key] if x.startswith(key[:-1]) else x
#                 )
#             )

#         # ---------------------------------------------------------------------
#         return dict(zip(table.name, table.iso4))

#     def appy_words2abbr(words2abbr):
#         files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
#         for file in files:
#             data = pd.read_csv(file, encoding="utf-8")
#             data.source_abbr__ = data.source_abbr.map(
#                 lambda x: " ".join([words2abbr.get(word, word) for word in x.split()])
#                 if x is not pd.NA
#                 else x
#             )
#             data.to_csv(file, sep=",", encoding="utf-8", index=False)

#     #
#     #
#     #
#     sys.stdout.write("--INFO-- Completing ISO4 source names\n")

#     source_abbr = get_source_abbr()
#     words2abbr = get_words2abbr(source_abbr)
#     appy_words2abbr(words2abbr)


# def default():

#     # search new iso source names not included in files/source_abbr.csv
#     if "source_abbr" in documents.columns:

#         # iso souce names in the current file
#         documents = documents.copy()
#         documents.source_abbr = documents.source_abbr.str.upper()
#         documents.source_abbr = documents.source_abbr.map(
#             lambda x: x.replace(".", "") if not pd.isna(x) else x
#         )
#         current_iso_names = documents[["source_name", "source_abbr"]].copy()
#         current_iso_names = current_iso_names.assign(
#             source_name=current_iso_names.source_name.str.strip()
#         )
#         current_iso_names = current_iso_names.assign(
#             source_abbr=current_iso_names.source_abbr.str.strip()
#         )
#         current_iso_names = current_iso_names.dropna()
#         current_iso_names = current_iso_names.sort_values(
#             by=["source_name", "source_abbr"]
#         )
#         current_iso_names = current_iso_names.drop_duplicates("source_name")

#         # adds the abbreviations the the current file
#         module_path = os.path.dirname(__file__)
#         file_path = os.path.join(module_path, "files/source_abbr.csv")
#         pdf = pd.read_csv(file_path, sep=",")
#         pdf = pd.concat([pdf, current_iso_names])
#         pdf = pdf.sort_values(by=["source_name", "source_abbr"])
#         pdf = pdf.drop_duplicates("source_name")
#         pdf.to_csv(file_path, index=False)
#     return documents


def _complete__source_abbr__colum(documents):

    if "source_abbr" in documents.columns:
        #
        # Loads existent iso source names and make a dictionary
        # to translate source names to iso source names
        #
        module_path = os.path.dirname(__file__)
        file_path = os.path.join(module_path, "files/source_abbr.csv")
        pdf = pd.read_csv(file_path, sep=",")
        existent_names = dict(zip(pdf.source_name, pdf.source_abbr))

        # complete iso source names
        documents = documents.copy()
        documents.source_abbr = [
            abb
            if not pd.isna(abb)
            else (existent_names[name] if name in existent_names.keys() else abb)
            for name, abb in zip(documents.source_name, documents.source_abbr)
        ]
    return documents


def _repair__source_abbr__column(documents):
    if "source_abbr" in documents.columns:
        documents = documents.copy()
        documents.source_abbr = [
            "--- " + name[:25] if pd.isna(abb) and not pd.isna(name) else abb
            for name, abb in zip(documents.source_name, documents.source_abbr)
        ]
        documents = documents.assign(
            source_abbr=documents.source_abbr.map(
                lambda x: x[:29] if isinstance(x, str) else x
            )
        )
    return documents

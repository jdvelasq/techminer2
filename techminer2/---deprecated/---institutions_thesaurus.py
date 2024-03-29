# """
# Create institutions thesaurus
# ===============================================================================

# Creates a institutions thesaurus from the data in the database.

# # >>> from techminer2 import *
# # >>> directory = "data/regtech/"

# # >>> create_institutions_thesaurus(directory)
# # --INFO-- Creating institutions thesaurus
# # --INFO-- Affiliations without country detected - check file data/processed/ignored_affiliations.txt
# # --INFO-- Affiliations without country detected - check file data/ignored_affiliations.txt
# # --INFO-- Thesaurus file 'data/processed/institutions.txt' created

# # >>> apply_institutions_thesaurus(directory)
# # --INFO-- Applying thesaurus to institutions
# # --INFO-- The thesaurus was applied to institutions in all databases

# """

# import glob
# import os.path
# import sys

# import pandas as pd

# # from .extract_country import extract_country_from_string
# # from ..._thesaurus import Thesaurus, load_file_as_dict

# #
# # The algorithm searches in order until detect a match
# #
# NAMES = [
#     "ministry",
#     "national",
#     "univ ",
#     "unisversidade",
#     "univerza",
#     "univerrsity",
#     "universidad",
#     "universidade",
#     "universita",
#     "universitas",
#     "universitat",
#     "universite",
#     "universiteit",
#     "university",
#     "univesity",
#     "univesrity",
#     "unversitat",
#     "universiti",
#     "institut",
#     "instituto",
#     "college",
#     "colegio",
#     "bank",
#     "banco",
#     "centre",
#     "center",
#     "centro",
#     "agency",
#     "agencia",
#     "council",
#     "commission",
#     "comision",
#     "consejo",
#     "politec",
#     "polytechnic",
#     "politecnico",
#     "department",
#     "direction",
#     "laboratory",
#     "laboratoire",
#     "laboratorio",
#     "school",
#     "skola",
#     "scuola",
#     "ecole",
#     "escuela",
#     "hospital",
#     "association",
#     "asociacion",
#     "company",
#     "organization",
#     "academy",
#     "academia",
#     "tecnologico",
#     "empresa",
#     "inc.",
#     "ltd.",
#     "office",
#     "oficina",
#     "corporation",
#     "corporacion",
#     "ministerio",
#     "technologies",
#     "unidad",
#     "tecnologico",
#     "consorcio",
#     "autoridad",
#     "compania",
#     "sociedad",
#     "servicio",
#     "government",
#     "institute",
#     "sociedad",
#     "society",
# ]

# SPANISH = [
#     "ARG",
#     "CHL",
#     "COL",
#     "CUB",
#     "ECU",
#     "ESP",
#     "GTM",
#     "HND",
#     "MEX",
#     "NIC",
#     "PAN",
#     "PER",
#     "VEN",
# ]

# PORTUGUES = [
#     "BRA",
#     "PRT",
# ]


# def create_institutions_thesaurus(directory="./"):
#     """
#     Creates an insitutions thesaurus from the data in the database.
#     """

#     #
#     def clean_name(w):
#         w = w.replace(".", "").lower().strip()
#         w = w.replace("&", " and ")
#         w = w.replace(" aandm ", " a and m ")
#         w = w.replace("the university of ", "university of ")
#         w = w.replace(" univ. nacional de ", " universidad nacional de ")
#         w = w.replace(" univ. de la ", " universidad de la ")
#         w = w.replace(" univ. del ", " universidad del ")
#         w = w.replace(" univ. do ", " universidade do ")
#         w = w.replace(" univ. of ", " university of ")

#         w = (
#             w.replace("'", "")
#             .replace('"', "")
#             .replace("“", "")
#             .replace("”", "")
#             .replace(".", "")
#             .replace("’", "")
#             .strip()
#         )

#         if "(" in w:
#             w = w.replace(w[w.find("(") : w.find(")") + 1], "").strip()
#             w = " ".join(w.split())

#         return w

#     #
#     def search_name(w):
#         ##
#         ## Searchs a exact match
#         ##
#         for institution in VALID_NAMES:
#             if institution in w:
#                 return institution

#         ##
#         ## Preprocessing
#         ##
#         w = clean_name(w)

#         ##
#         ## Searchs for a possible match
#         ##
#         for name in NAMES:
#             for elem in w.split(","):
#                 if "-" in elem:
#                     elem = elem.split("-")
#                     elem = [e.strip() for e in elem]
#                     elem = elem[0] if len(elem[0]) > len(elem[1]) else elem[1]

#                 if name in elem:
#                     selected_name = elem.strip().lower()

#                     return selected_name.lower()

#         return None

#     sys.stdout.write("--INFO-- Creating institutions thesaurus\n")

#     thesaurus_file = os.path.join(directory, "processed", "institutions.txt")

#     #
#     # Valid names of institutions
#     #
#     module_path = os.path.dirname(__file__)
#     with open(
#         os.path.join(module_path, "files/institutions.txt"),
#         "rt",
#         encoding="utf-8",
#     ) as f:
#         VALID_NAMES = f.readlines()
#     VALID_NAMES = [w.replace("\n", "").lower() for w in VALID_NAMES]
#     VALID_NAMES = [w for w in VALID_NAMES if len(w) > 0]

#     #
#     # List of standardized country names
#     #
#     module_path = os.path.dirname(__file__)
#     filename = os.path.join(module_path, "files/country_codes.txt")
#     country_codes = load_file_as_dict(filename)
#     country_names = list(country_codes.values())
#     country_names = [w[0].lower() for w in country_names]
#     country_names_to_codes = {
#         item: code
#         for code in country_codes.keys()
#         for item in country_codes[code]
#     }

#     # --------------------------------------------------------------------------[]
#     affiliations = []
#     files = list(glob.glob(os.path.join(directory, "processed/_*.csv")))
#     for file in files:
#         data = pd.read_csv(file, encoding="utf-8")
#         affiliations += data["affiliations"].tolist()
#     # --------------------------------------------------------------------------

#     #
#     # Transform affiliations to lower case
#     #
#     x = pd.Series(affiliations, name="affiliations")
#     x = x.map(lambda w: w.lower().strip(), na_action="ignore")

#     #
#     # Explodes the list of affiliations
#     #
#     x = x.dropna()
#     x = x.map(lambda w: w.split(";"))
#     x = x.explode()
#     x = x.map(lambda w: w.strip())
#     x = x.unique().tolist()

#     #
#     # Loads the current thesaurus and
#     # select only new affiliations
#     #
#     if os.path.isfile(thesaurus_file):
#         dict_ = load_file_as_dict(thesaurus_file)
#         clustered_text = [word for key in dict_.keys() for word in dict_[key]]
#         x = [word for word in x if word not in clustered_text]

#     else:
#         dict_ = {}

#     #
#     # Processing of new affiliations
#     #
#     x = pd.DataFrame({"affiliation": x})

#     #
#     # Extracts the country and drop rows
#     # without country
#     #
#     x["country"] = x.affiliation.map(
#         extract_country_from_string, na_action="ignore"
#     )
#     if any(x.country.isna()):
#         sys.stdout.write(
#             "--INFO-- Affiliations without country detected - check file "
#             + os.path.join(
#                 directory, "processed", "ignored_affiliations.txt\n"
#             )
#         )

#     #
#     # Converts country name to code
#     #
#     x["country"] = x.country.map(
#         lambda w: country_names_to_codes[w], na_action="ignore"
#     )

#     #
#     # Ignore institutions without country
#     #
#     ignored_affiliations = x[x.country.isna()]["affiliation"].tolist()
#     x = x.dropna()

#     #
#     # Searches a possible name for the institution
#     #
#     x["key"] = x.affiliation.map(search_name)
#     if any(x.key.isna()):
#         msg = (
#             "Affiliations without country detected - check file "
#             + directory
#             + "ignored_affiliations.txt"
#         )
#         sys.stdout.write("--INFO-- " + msg + "\n")
#     ignored_affiliations += x[x.key.isna()]["affiliation"].tolist()

#     #
#     # list of ignored affiliations for manual review
#     #
#     ignored_affiliations_file = os.path.join(
#         directory, "processed", "ignored_affiliations.txt"
#     )
#     with open(ignored_affiliations_file, "wt", encoding="utf-8") as text_file:
#         for aff in ignored_affiliations:
#             print(aff, file=text_file)

#     #
#     # Search keys in foreign languages
#     #
#     institutions = x.key.copy()
#     institutions = institutions.dropna()
#     institutions = institutions.tolist()

#     for key, country in zip(x.key, x.country):
#         if pd.isna(key) or pd.isna(country):
#             continue

#         aff = key.split(" ")
#         if country in SPANISH:
#             #
#             # Rule: XXX university ---> universidad XXX
#             #

#             for foreign, local in [
#                 ("university", "universidad de "),
#                 ("university", "universidad de la "),
#                 ("university", "universidad "),
#                 ("institute of technology", "instituto de tecnologia de "),
#                 ("institute of technology", "instituto tecnologico de "),
#             ]:
#                 if len(aff) > len(foreign.split(" ")):
#                     proper_name = " ".join(
#                         aff[: len(aff) - len(foreign.split())]
#                     )
#                     local_name = local + proper_name

#                     if local_name in institutions + VALID_NAMES:
#                         x["key"] = x.key.map(
#                             lambda w: local_name if w == key else w,
#                             na_action="ignore",
#                         )

#             #
#             # Rule: YYY university of XXX ---> universidad YYY de XXX
#             #       YYY school of XXX ---> escuela YYY de XXX
#             #
#             for foreign, spanish in [
#                 ("national university of", "universidad nacional de "),
#                 ("catholic university of", "universidad catolica de "),
#                 ("central university of", "universidad central de "),
#                 ("technical university of", "universidad tecnica de "),
#                 ("technological university of", "universidad tecnologica de "),
#                 ("autonomous university of", "universidad autonoma de "),
#                 ("polytechnic university of", "universidad politecnica de "),
#                 ("politechnic university of", "universidad politecnica de "),
#                 ("universitat politecnica de", "universidad politecnica de "),
#                 (
#                     "metropolitan university of",
#                     "universidad metropolitana de ",
#                 ),
#                 ("politechnic school of", "escuela politecnica de "),
#                 ("polytechnic school of", "escuela politecnica de "),
#                 ("industrial university of", "universidad industrial de "),
#                 (
#                     "pontifical catholic university of",
#                     "pontificia universidad catolica de ",
#                 ),
#             ]:
#                 foreign_len = len(foreign.split())
#                 if " ".join(aff[:foreign_len]) == foreign:
#                     new_name = spanish + " ".join(aff[foreign_len:])
#                     if new_name in institutions + VALID_NAMES:
#                         x["key"] = x.key.map(
#                             lambda w: new_name if w == key else w,
#                             na_action="ignore",
#                         )

#             #
#             # Rule: university of XXX ----> universidad de
#             #
#             for foreign, spanish in [
#                 ("universitat de", "universidad de "),
#                 ("university of", "universidad de "),
#                 ("university of", "universidad del "),
#                 ("university of", "universidad de el "),
#                 ("university of", "universidad de la "),
#             ]:
#                 if " ".join(aff[:2]) == foreign:
#                     new_name = spanish + " ".join(aff[2:])
#                     if new_name in institutions + VALID_NAMES:
#                         x["key"] = x.key.map(
#                             lambda w: new_name if w == key else w,
#                             na_action="ignore",
#                         )

#         if country in PORTUGUES:
#             #
#             #
#             #
#             for foreign, portugues in [
#                 ("state university of", "universidade estadual do "),
#                 ("state university of", "universidade estadual de "),
#                 ("state university of", "universidade estadual da "),
#                 ("state univesity of", "universidade estadual do "),
#                 ("state univesity of", "universidade estadual de "),
#                 ("state univesity of", "universidade estadual da "),
#                 ("federal university of", "universidade federal do "),
#                 ("federal university of", "universidade federal de "),
#                 ("federal university of", "universidade federal da "),
#                 ("universidad federal de", "universidade federal do "),
#                 ("universidad federal de", "universidade federal de "),
#                 ("universidad federal de", "universidade federal da "),
#                 ("universidad estatal de", "universidade federal do "),
#                 ("universidad estatal de", "universidade federal de "),
#                 ("universidad estatal de", "universidade federal da "),
#                 ("federal institute of", "instituto federal do "),
#                 ("federal institute of", "instituto federal de "),
#                 ("federal institute of", "instituto federal da "),
#                 ("polytechnic institute of", "instituto politecnido do "),
#                 ("polytechnic institute of", "instituto politecnido de "),
#                 ("polytechnic institute of", "instituto politecnido da "),
#                 (
#                     "pontifical catholic university of",
#                     "pontificia universidade catolica do ",
#                 ),
#             ]:
#                 foreign_len = len(foreign.split())
#                 if " ".join(aff[:foreign_len]) == foreign:
#                     new_name = portugues + " ".join(aff[foreign_len:])
#                     if new_name in institutions + VALID_NAMES:
#                         x["key"] = x.key.map(
#                             lambda w: new_name if w == key else w,
#                             na_action="ignore",
#                         )

#             #
#             # Rule
#             #
#             for foreign, portugues in [
#                 ("state university", "universidade estadual do "),
#                 ("state university", "universidade estadual de "),
#                 ("state university", "universidade estadual da "),
#                 ("federal university", "universidade federal do "),
#                 ("federal university", "universidade federal de "),
#                 ("federal university", "universidade federal da "),
#             ]:
#                 if " ".join(aff[-2:]) == foreign:
#                     new_name = portugues + " ".join(aff[:-2])
#                     if new_name in institutions + VALID_NAMES:
#                         x["key"] = x.key.map(
#                             lambda w: new_name if w == key else w,
#                             na_action="ignore",
#                         )

#             for foreign, portugues in [
#                 ("university of", "universidade do "),
#                 ("university of", "universidade de "),
#                 ("university of", "universidade da "),
#                 ("universidad de", "universidade do "),
#                 ("universidad de", "universidade de "),
#                 ("universidad de", "universidade da "),
#             ]:
#                 if " ".join(aff[:2]) == foreign:
#                     new_name = portugues + " ".join(aff[2:])
#                     if new_name in institutions + VALID_NAMES:
#                         x["key"] = x.key.map(
#                             lambda w: new_name if w == key else w,
#                             na_action="ignore",
#                         )

#             for foreign, portugues in [
#                 ("university", "universidade do "),
#                 ("university", "universidade de "),
#                 ("university", "universidade da "),
#             ]:
#                 if aff[-1] == foreign:
#                     new_name = portugues + " ".join(aff[:-1])
#                     if new_name in institutions + VALID_NAMES:
#                         x["key"] = x.key.map(
#                             lambda w: new_name if w == key else w,
#                             na_action="ignore",
#                         )

#     #
#     # Format key string
#     #
#     x["key"] = x.key.map(lambda w: w.title(), na_action="ignore")
#     x["key"] = x.key.map(
#         lambda w: w.replace(" Of ", " of "), na_action="ignore"
#     )
#     x["key"] = x.key.map(
#         lambda w: w.replace(" And ", " and "), na_action="ignore"
#     )
#     x["key"] = x.key.map(
#         lambda w: w.replace(" For ", " for "), na_action="ignore"
#     )
#     x["key"] = x.key.map(
#         lambda w: w.replace(" At ", " at "), na_action="ignore"
#     )
#     x["key"] = x.key.map(
#         lambda w: w.replace(" De ", " de "), na_action="ignore"
#     )
#     x["key"] = x.key.map(
#         lambda w: w.replace(" La ", " la "), na_action="ignore"
#     )
#     x["key"] = x.key.map(
#         lambda w: w.replace(" Del ", " del "), na_action="ignore"
#     )
#     x["key"] = x.key.map(
#         lambda w: w.replace(" Do ", " do "), na_action="ignore"
#     )
#     x["key"] = x.key.map(lambda w: w.replace(" Y ", " y "), na_action="ignore")
#     x["key"] = x.key.map(
#         lambda w: w.replace(" Em ", " em "), na_action="ignore"
#     )

#     #
#     # Adds the country to the key
#     #
#     x["key"] = x.key + " " + x.country

#     #
#     # groups by key
#     #
#     grp = x.groupby(by="key").agg({"affiliation": list})
#     result = {
#         key: value
#         for key, value in zip(grp.index.tolist(), grp["affiliation"].tolist())
#     }

#     if os.path.isfile(thesaurus_file):
#         result = {**result, **dict_}

#     Thesaurus(
#         result, ignore_case=False, full_match=True, use_re=False
#     ).to_textfile(thesaurus_file)

#     sys.stdout.write(f"--INFO-- Thesaurus file '{thesaurus_file}' created\n")

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from techminer.utils.datastore import load_datastore
# from techminer.utils.explode import explode


# class CoreAuthors:
#     """
#     Core authors analysis and Lotka law


#     """

#     def __init__(
#         self,
#         datastorepath="./",
#     ):
#         self._datastorepath = datastorepath
#         self._datastore = load_datastore(self._datastorepath)
#         self._table = None

#     def _compute_core_authors(self):
#         """
#         Compute core authors
#         """

#         x = self._datastore.copy()

#         #
#         #  Num_Documents per Author
#         #
#         x["num_documents"] = 1
#         x = explode(
#             x[
#                 [
#                     "authors",
#                     "num_documents",
#                     "record_id",
#                 ]
#             ],
#             "authors",
#         )
#         result = x.groupby("authors", as_index=True).agg(
#             {
#                 "num_documents": np.sum,
#             }
#         )
#         z = result
#         authors_dict = {
#             author: num_docs
#             for author, num_docs in zip(z.index, z.num_documents)
#             if not pd.isna(author)
#         }

#         #
#         #  Num Authors x Documents written per Author
#         #
#         z = z[["num_documents"]]
#         z = z.groupby(["num_documents"]).size()
#         w = [str(round(100 * a / sum(z), 2)) + " %" for a in z]
#         z = pd.DataFrame(
#             {"Num Authors": z.tolist(), "%": w, "Documents written per Author": z.index}
#         )
#         z = z.sort_values(["Documents written per Author"], ascending=False)
#         z["Acum Num Authors"] = z["Num Authors"].cumsum()
#         z["% Acum"] = [
#             str(round(100 * a / sum(z["Num Authors"]), 2)) + " %"
#             for a in z["Acum Num Authors"]
#         ]
#         m = explode(self._datastore[["authors", "record_id"]], "authors")
#         m = m.dropna()
#         m["Documents_written"] = m.authors.map(lambda w: authors_dict[w])

#         n = []
#         for k in z["Documents written per Author"]:
#             s = m.query("Documents_written >= " + str(k))
#             s = s[["record_id"]]
#             s = s.drop_duplicates()
#             n.append(len(s))

#         k = []
#         for index in range(len(n) - 1):
#             k.append(n[index + 1] - n[index])
#         k = [n[0]] + k
#         z["Num Documents"] = k
#         z["% Num Documents"] = [str(round(i / max(n) * 100, 2)) + "%" for i in k]
#         z["Acum Num Documents"] = n
#         z["% Acum Num Documents"] = [str(round(i / max(n) * 100, 2)) + "%" for i in n]

#         z = z[
#             [
#                 "Num Authors",
#                 "%",
#                 "Acum Num Authors",
#                 "% Acum",
#                 "Documents written per Author",
#                 "Num Documents",
#                 "% Num Documents",
#                 "Acum Num Documents",
#                 "% Acum Num Documents",
#             ]
#         ]

#         self._table = z.reset_index(drop=True)

#     @property
#     def table_(self):
#         """
#         Get the top documents.

#         """
#         if self._table is None:
#             self._compute_core_authors()
#         return self._table

#     def plot(self, colormap="Greys", figsize=(8, 6), fontsize=11):

#         if self._table is None:
#             self._compute_core_authors()

#         data = self.table_
#         percentage_authors = data["%"].map(lambda w: float(w[:-2])).tolist()
#         documents_written = data["Documents written per Author"].tolist()

#         matplotlib.rc("font", size=fontsize)
#         fig, axs = plt.subplots(figsize=figsize)

#         cmap = plt.cm.get_cmap(colormap)
#         color = cmap(0.6)

#         percentage_authors.reverse()
#         documents_written.reverse()

#         axs.plot(
#             documents_written,
#             percentage_authors,
#             linestyle="-",
#             linewidth=2,
#             color="k",
#         )
#         axs.fill_between(
#             documents_written,
#             percentage_authors,
#             color=color,
#             alpha=0.6,
#         )

#         #
#         # Theoretical
#         #
#         total_authors = data["Num Authors"].max()
#         theoretical = [total_authors / float(x * x) for x in documents_written]
#         total_theoretical = sum(theoretical)
#         perc_theoretical_authors = [w / total_theoretical * 100 for w in theoretical]

#         axs.plot(
#             documents_written,
#             perc_theoretical_authors,
#             linestyle=":",
#             linewidth=4,
#             color="k",
#         )

#         for side in ["top", "right", "left", "bottom"]:
#             axs.spines[side].set_visible(False)

#         axs.grid(axis="y", color="gray", linestyle=":")
#         axs.grid(axis="x", color="gray", linestyle=":")
#         axs.set_ylabel("% of Authors")
#         axs.set_xlabel("Documets written per Author")

#         fig.set_tight_layout(True)
#         return axs

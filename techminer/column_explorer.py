"""
Column explorer
===============================================================================


"""


# import ipywidgets as widgets
# from IPython.display import display
# from ipywidgets import GridspecLayout, Layout

# from .dashboard import document_to_html
# from .utils import load_filtered_documents


# class _App:
#     def __init__(self, directory, top_n=100):

#         # Data
#         self.documents = load_filtered_documents(directory)
#         columns = sorted(self.documents.columns)

#         # Left panel controls
#         self.command_panel = [
#             widgets.HTML("<hr><b>Column:</b>", layout=Layout(margin="0px 0px 0px 5px")),
#             widgets.Dropdown(
#                 description="",
#                 value=columns[0],
#                 options=columns,
#                 layout=Layout(width="auto"),
#                 style={"description_width": "130px"},
#             ),
#             widgets.HTML("<hr><b>Term:</b>", layout=Layout(margin="0px 0px 0px 5px")),
#             widgets.Dropdown(
#                 description="",
#                 value=None,
#                 options=[],
#                 layout=Layout(width="auto"),
#                 style={"description_width": "130px"},
#             ),
#             widgets.HTML(
#                 "<hr><b>Found documents:</b>", layout=Layout(margin="0px 0px 0px 5px")
#             ),
#             widgets.Select(
#                 options=[],
#                 layout=Layout(height="360pt", width="auto"),
#             ),
#         ]

#         # interactive output function
#         widgets.interactive_output(
#             f=self.interactive_output,
#             controls={
#                 "column": self.command_panel[1],
#                 "value": self.command_panel[3],
#                 "article_title": self.command_panel[5],
#             },
#         )

#         # Grid size (Generic)
#         self.app_layout = GridspecLayout(
#             max(9, len(self.command_panel) + 1), 4, height="700px"
#         )

#         # Creates command panel (Generic)
#         self.app_layout[:, 0] = widgets.VBox(
#             self.command_panel,
#             layout=Layout(
#                 margin="10px 8px 5px 10px",
#             ),
#         )

#         # Output area (Generic)
#         self.output = widgets.Output()  # .add_class("output_color")
#         self.app_layout[0:, 1:] = widgets.VBox(
#             [self.output],
#             layout=Layout(margin="10px 4px 4px 4px", border="1px solid gray"),
#         )

#         # self.execute()

#     def run(self):
#         return self.app_layout

#     def execute(self):

#         with self.output:

#             column = self.column
#             documents = self.documents.copy()
#             documents[column] = documents[column].str.split("; ")
#             x = documents.explode(column)

#             # populate terms
#             all_terms = x[column].copy()
#             all_terms = all_terms.dropna()
#             all_terms = all_terms.drop_duplicates()
#             all_terms = all_terms.sort_values()
#             self.command_panel[3].options = all_terms

#             #
#             # Populate titles
#             #
#             keyword = self.command_panel[3].value
#             s = x[x[column] == keyword]
#             s = s[["global_citations", "document_title"]]
#             s = s.sort_values(
#                 ["global_citations", "document_title"], ascending=[False, True]
#             )
#             s = s[["document_title"]].drop_duplicates()
#             self.command_panel[5].options = s["document_title"].tolist()

#             #
#             # Print info from selected title
#             #
#             out = self.documents[
#                 self.documents["document_title"] == self.command_panel[5].value
#             ]
#             out = out.reset_index(drop=True)
#             out = out.iloc[0]
#             self.output.clear_output()
#             with self.output:
#                 display(widgets.HTML(document_to_html(out)))

#     def interactive_output(self, **kwargs):

#         for key in kwargs.keys():
#             setattr(self, key, kwargs[key])

#         self.execute()


# def column_explorer(directory, top_n=100):
#     """
#     Column explorer

#     :param directory:
#     :param top_n:
#     :return:
#     """

#     app = _App(directory, top_n)
#     return app.run()

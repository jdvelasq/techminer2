# from .heat_map import heat_map


# class Matrix:
#     def __init__(self):
#         self.matrix = None

#     def sort_values(
#         self,
#         by,
#         axis=0,
#         ascending=True,
#         inplace=False,
#         kind="quicksort",
#         na_position="last",
#         ignore_index=False,
#         key=None,
#     ):
#         matrix = self.matrix.sort_values(
#             by=by,
#             axis=axis,
#             ascending=ascending,
#             inplace=False,
#             kind=kind,
#             na_position=na_position,
#             ignore_index=ignore_index,
#             key=key,
#         )

#         if inplace is True:
#             self.matrix = matrix
#             return self
#         return matrix

#     def sort_index(
#         self,
#         axis=0,
#         level=None,
#         ascending=True,
#         inplace=False,
#         kind="quicksort",
#         na_position="last",
#         sort_remaining=True,
#         ignore_index=False,
#         key=None,
#     ):
#         matrix = self.matrix.sort_index(
#             axis=axis,
#             level=level,
#             ascending=ascending,
#             inplace=False,
#             kind=kind,
#             na_position=na_position,
#             sort_remaining=sort_remaining,
#             ignore_index=ignore_index,
#             key=key,
#         )

#         if inplace is True:
#             self.matrix = matrix
#             return self
#         return matrix

#     @property
#     def columns(self):
#         return self.matrix.columns

#     @columns.setter
#     def columns(self, columns):
#         self.matrix.columns = columns

#     @property
#     def values(self):
#         return self.matrix.values

#     def heat_map(
#         self,
#         cmap="Greys",
#         figsize=(6, 6),
#         fontsize=9,
#         **kwargs,
#     ):
#         return heat_map(
#             self.matrix,
#             cmap=cmap,
#             figsize=figsize,
#             fontsize=fontsize,
#             **kwargs,
#         )

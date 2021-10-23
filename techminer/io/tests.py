from importer import Importer


Importer().transform(
    src=[
        # ("Scopus", "data/scopus.csv"),
        ("WoS", "../tests/data/savedrecs.txt"),
        # ("Dimensions", "data/dimensions.csv"),
    ],
)

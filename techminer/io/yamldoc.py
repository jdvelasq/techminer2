import yaml


class _YamlDocument:
    def __init__(self, log_dir="."):

        if log_dir[-1] != "/":
            log_dir += "/"
        self.log_dir_ = log_dir

    def dump(self, dataframe):

        print(dataframe.to_dict(orient="records"))

        text = yaml.dump(
            dataframe.to_dict(orient="records"),
            sort_keys=False,
            width=80,
            indent=4,
            default_flow_style=None,
        )

        with open(self.log_dir_ + "corpus.txt", "w", encoding="utf-8") as file:
            file.write(text)

    def load(self):
        pass


def savefile(dataframe, log_dir="."):
    """Saves the corpus to disk"""
    yamldocument = _YamlDocument(log_dir=log_dir)
    yamldocument.dump(dataframe)

from techminer2.database.tools import CollectDescriptors, ExtractCopyrightText

from ....colorized_input import colorized_input


def execute_copyright_command():

    print()

    while True:
        n_chars = colorized_input(". Enter n_chars (140) >").strip()
        if n_chars.isdigit() or n_chars == "":
            break

    if not n_chars:
        n_chars = 140
    else:
        n_chars = int(n_chars)

    CollectDescriptors(root_directory="./").run()

    text = ExtractCopyrightText(
        pattern=None,
        n_chars=n_chars,
        root_directory="./",
    ).run()

    with open("./outputs/texts/copyright_text.txt", "w") as f:
        for t in text:
            f.write(t)
            f.write("\n")

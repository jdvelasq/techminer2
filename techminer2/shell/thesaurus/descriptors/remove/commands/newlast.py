from ......thesaurus.descriptors import RegisterLastWord


def execute_newlast_command():

    print()
    word = input(". new last word > ").strip()
    if word == "":
        print()
        return
    RegisterLastWord().having_word(word).run()

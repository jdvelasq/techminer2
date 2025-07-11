from ......thesaurus.descriptors import RegisterInitialWord


def execute_newinitial_command():

    print()
    word = input(". new initial word > ").strip()
    if word == "":
        print()
        return
    print()
    RegisterInitialWord().having_word(word).run()

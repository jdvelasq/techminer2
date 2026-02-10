from fuzzywuzzy import fuzz  # type: ignore


def compute_fuzzy_match(self, string1, string2):

    string1 = string1.split()
    string2 = string2.split()

    if len(string1) > len(string2):
        shorten_string = string2
        lengthen_string = string1
    else:
        shorten_string = string1
        lengthen_string = string2

    scores_per_word = []
    for base_word in shorten_string:
        best_match = 0
        for candidate_word in lengthen_string:
            score = fuzz.ratio(base_word, candidate_word)
            if score > best_match:
                best_match = score
        scores_per_word.append(best_match)

    score = min(scores_per_word)
    match = all(score >= self.params.fuzzy_threshold for score in scores_per_word)

    return score, match

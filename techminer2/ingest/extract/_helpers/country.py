from techminer2._internals.package_data.word_lists import load_builtin_word_list
from techminer2.ingest.extract._helpers.values import extract_values


def extract_country(params):

    df = extract_values(params)
    country_names = load_builtin_word_list("country_names.txt")

    def _extract(text):
        for country in country_names:
            if country.lower() in text.lower():
                return country
        return None

    series = df.term.apply(_extract)
    series = series.dropna().sort_values(ascending=True).drop_duplicates()
    return series.tolist()

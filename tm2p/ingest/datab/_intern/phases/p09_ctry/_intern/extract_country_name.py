from tm2p._intern.packag_data import load_builtin_word_list

from .country_replacements import _COUNTRY_REPLACEMENTS


def extract_country_name_from_string(affiliation: str) -> str:

    country = affiliation.split(",")[-1].strip()

    for pat, repl in _COUNTRY_REPLACEMENTS:
        country = country.replace(pat, repl)

    country_names = load_builtin_word_list("country_names.txt")
    if country not in country_names:
        country = "[UNKNOWN]"

    if country == "[UNKNOWN]":
        for ctry in country_names:
            if f", {ctry}." in affiliation:
                country = ctry
                break
            if affiliation.endswith(ctry):
                country = ctry
                break

    if country == "[UNKNOWN]":
        for abbr, ctry in [
            ("UK", "United Kingdom"),
            ("United States of America", "United States"),
            ("USA", "United States"),
            ("Republic of Korea", "South Korea"),
            ("The Netherlands", "Netherlands"),
        ]:
            if f", {abbr}." in affiliation:
                country = ctry
                break
            if f", {abbr}," in affiliation:
                country = ctry
                break
            if affiliation.endswith(abbr):
                country = ctry
                break

    if country == "[UNKNOWN]":
        for state in [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawaii",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Louisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Michigan",
            "Minnesota",
            "Mississippi",
            "Missouri",
            "Montana",
            "Nebraska",
            "Nevada",
            "New Hampshire",
            "New Jersey",
            "New Mexico",
            "New York",
            "North Carolina",
            "North Dakota",
            "Ohio",
            "Oklahoma",
            "Oregon",
            "Pennsylvania",
            "Rhode Island",
            "South Carolina",
            "South Dakota",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "West Virginia",
            "Wisconsin",
            "Wyoming",
            "District of Columbia",
        ]:
            if f", {state}." in affiliation:
                country = "United States"
                break
            if affiliation.endswith(state):
                country = "United States"
                break

    if country == "[UNKNOWN]":
        for city, ctry in [
            ("Ann Arbor", "United States"),
            ("Athens", "United States"),
            ("Atlanta", "United States"),
            ("Aurora", "United States"),
            ("Baltimore", "United States"),
            ("Birmingham", "United States"),
            ("Boston", "United States"),
            ("Buffalo", "United States"),
            ("Chicago", "United States"),
            ("Columbus", "United States"),
            ("Corvallis", "United States"),
            ("Dallas", "United States"),
            ("Denver", "United States"),
            ("East Lansing", "United States"),
            ("Honolulu", "United States"),
            ("Houston", "United States"),
            ("Indianapolis", "United States"),
            ("Iowa City", "United States"),
            ("Kansas City", "United States"),
            ("La Jolla", "United States"),
            ("Los Angeles", "United States"),
            ("Madison", "United States"),
            ("Minneapolis MN", "United States"),
            ("Minneapolis", "United States"),
            ("New York", "United States"),
            ("Oakland", "United States"),
            ("Omaha", "United States"),
            ("Palto Alto", "United States"),
            ("Philadelphia", "United States"),
            ("Phoenix", "United States"),
            ("Sacramento", "United States"),
            ("San Antonio", "United States"),
            ("San Diego", "United States"),
            ("San Francisco", "United States"),
            ("San Jose", "United States"),
            ("Seattle", "United States"),
            #
            ("Ann Arbor, MI", "United States"),
            ("Athens, OH", "United States"),
            ("Atlanta, GA", "United States"),
            ("Aurora, CO", "United States"),
            ("Baltimore, MD", "United States"),
            ("Birmingham, AL", "United States"),
            ("Boston, MA", "United States"),
            ("Buffalo, NY", "United States"),
            ("Chicago, IL", "United States"),
            ("Columbus, OH", "United States"),
            ("Corvallis, OR", "United States"),
            ("Dallas, TX", "United States"),
            ("Denver, CO", "United States"),
            ("East Lansing, MI", "United States"),
            ("Honolulu, HI", "United States"),
            ("Houston, TX", "United States"),
            ("Indianapolis, IN", "United States"),
            ("Iowa City, IA", "United States"),
            ("Kansas City, MO", "United States"),
            ("La Jolla, CA", "United States"),
            ("Los Angeles, CA", "United States"),
            ("Madison, WI", "United States"),
            ("Minneapolis, MN", "United States"),
            ("New York, NY", "United States"),
            ("Oakland, CA", "United States"),
            ("Omaha, NE", "United States"),
            ("Palo Alto, CA", "United States"),
            ("Philadelphia, PA", "United States"),
            ("Phoenix, AZ", "United States"),
            ("Sacramento, CA", "United States"),
            ("San Antonio, TX", "United States"),
            ("San Diego, CA", "United States"),
            ("San Francisco, CA", "United States"),
            ("San Jose, CA", "United States"),
            ("Seattle, WA", "United States"),
            #
            ("Ann Arbor MI", "United States"),
            ("Athens OH", "United States"),
            ("Atlanta GA", "United States"),
            ("Aurora CO", "United States"),
            ("Baltimore MD", "United States"),
            ("Birmingham AL", "United States"),
            ("Boston MA", "United States"),
            ("Buffalo NY", "United States"),
            ("Chicago IL", "United States"),
            ("Columbus OH", "United States"),
            ("Corvallis OR", "United States"),
            ("Dallas, TX", "United States"),
            ("Denver CO", "United States"),
            ("East Lansing MI", "United States"),
            ("Honolulu HI", "United States"),
            ("Houston TX", "United States"),
            ("Indianapolis IN", "United States"),
            ("Iowa City IA", "United States"),
            ("Kansas City MO", "United States"),
            ("La Jolla CA", "United States"),
            ("Los Angeles CA", "United States"),
            ("Madison WI", "United States"),
            ("Minneapolis MN", "United States"),
            ("New York NY", "United States"),
            ("Oakland CA", "United States"),
            ("Omaha NE", "United States"),
            ("Palo Alto CA", "United States"),
            ("Philadelphia PA", "United States"),
            ("Phoenix AZ", "United States"),
            ("Sacramento CA", "United States"),
            ("San Antonio TX", "United States"),
            ("San Diego CA", "United States"),
            ("San Francisco CA", "United States"),
            ("San Jose CA", "United States"),
            ("Seattle WA", "United States"),
            #
            ("Alberta", "Canada"),
            ("British Columbia", "Canada"),
            ("Calgary", "Canada"),
            ("Edmonton", "Canada"),
            ("Manitoba", "Canada"),
            ("Montreal", "Canada"),
            ("New Brunswick", "Canada"),
            ("Newfoundland and Labrador", "Canada"),
            ("Northwest Territories", "Canada"),
            ("Nova Scotia", "Canada"),
            ("Nunavut", "Canada"),
            ("Ontario", "Canada"),
            ("Ottawa", "Canada"),
            ("Prince Edward Island", "Canada"),
            ("Quebec", "Canada"),
            ("Saskatchewan", "Canada"),
            ("Toronto", "Canada"),
            ("Vancouver", "Canada"),
            ("Winnipeg", "Canada"),
            ("Yukon", "Canada"),
        ]:
            if f", {city}." in affiliation:
                country = ctry
                break
            if f", {city}," in affiliation:
                country = ctry
                break
            if affiliation.endswith(city):
                country = ctry
                break

    return country

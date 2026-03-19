import pandas as pd

# Load country codes
countries = pd.read_csv(
    "countryInfo.txt",
    sep="\t",
    comment="#",
    usecols=[0, 4],
    names=["iso", "country"],
    header=None,
)
iso_to_country = dict(zip(countries.iso, countries.country))

# Load admin1 (states/provinces)
admin1 = pd.read_csv(
    "admin1CodesASCII.txt", sep="\t", names=["code", "name", "asciiname", "geonameid"]
)

# Extract ISO country code from the "AU.02" code
admin1["iso"] = admin1["code"].str.split(".").str[0]
admin1["country"] = admin1["iso"].map(iso_to_country)

# Final lookup dictionary
geo_to_country = dict(zip(admin1["asciiname"], admin1["country"]))
# {"New South Wales": "Australia", "California": "United States", ...}

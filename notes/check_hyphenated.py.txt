from tqdm import tqdm
from openai import OpenAI
import os
from techminer2.package_data.text_processing import internal__load_text_processing_terms


PROMPT = """
INSTRUCTION:
You will be provided with two variations of the same word: one in hyphenated form and the other in non-hyphenated form.

TASK:
1. Analyze the two forms and determine which is correct in scientific or technical English usage.
2. Respond with "yes" if:
    - The hyphenated form is the only form correct.
    - If the word is not standard English.
    - If both forms (hyphenated and non-hyphenated) are correct.
3. Respond "no" if:
    - "no": the non-hyphenated form is the only form correct.

WORDS:
- Hyphenated: {}
- Non-hyphenated: {}


"""

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

terms = internal__load_text_processing_terms("hyphenated_is_correct.txt")
terms += internal__load_text_processing_terms("hyphenated_is_incorrect.txt")

hyphenated_is_incorrect = []
hyphenated_is_correct = []


for term in tqdm(
    terms,
    total=len(terms),
    desc=f"  Progress",
    ncols=80,
):

    if "_" not in term:
        continue

    words = term.split("_")
    if words[0] == words[1]:
        hyphenated_is_correct.append(term)
        continue

    query = PROMPT.format(term.lower().replace("_", "-"), term.lower().replace("_", ""))

    try:
        response = client.responses.create(
            model="o4-mini",
            input=query,
        )
        answer = response.output_text
        answer = answer.strip().lower()

        if answer == "no":
            hyphenated_is_incorrect.append(term)
        else:
            hyphenated_is_correct.append(term)

    except Exception as e:
        print(f"Error processing {e}")


with open("hyphenated_is_incorrect.txt", "w") as f:
    for term in hyphenated_is_incorrect:
        f.write(f"{term}\n")

with open("hyphenated_is_correct.txt", "w") as f:
    for term in hyphenated_is_correct:
        f.write(f"{term}\n")

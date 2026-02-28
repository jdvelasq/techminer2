import os

from openai import OpenAI

from tm2p._intern.packag_data.templates.load_builtin_template import (
    load_builtin_template,
)


def internal__paraphrase(text):

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    template = load_builtin_template("internals.genai.paraphrase.txt")
    prompt = template.format(text=text)

    try:
        response = client.responses.create(
            model="gpt-4-turbo",
            input=prompt,
        )
        answer = response.output_text
        return answer

    except Exception as e:
        print(f"Error processing: {e}")

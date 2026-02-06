import os
import re
from openai import OpenAI

USE_MOCK = True

if not USE_MOCK:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(system_prompt, user_prompt):

    if USE_MOCK:
        text = user_prompt.lower()

        match = re.search(r"(in|at|for)\s+([a-zA-Z\s]+)", text)

        if match:
            city = match.group(2).strip().title()
        else:
            city = "Delhi"

        return f"""
        {{
            "steps": [
                {{
                    "tool": "weather",
                    "city": "{city}"
                }}
            ]
        }}
        """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content

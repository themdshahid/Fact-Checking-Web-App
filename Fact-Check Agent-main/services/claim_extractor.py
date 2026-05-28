import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_claims(text):
    prompt = f"""
You are an AI fact-checking assistant.

Extract ONLY factual claims from the following text.

Focus on:
- Statistics
- Financial numbers
- Dates
- Technical facts
- Growth percentages
- Market size
- Scientific claims

Return the output as a numbered list.

TEXT:
{text[:12000]}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You extract factual claims."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    claims_text = response.choices[0].message.content

    claims = []

    for line in claims_text.split("\n"):
        line = line.strip()

        if line and any(char.isdigit() for char in line):
            claims.append(line)

    return claims
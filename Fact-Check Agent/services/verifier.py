import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def verify_claim(claim, web_data):
    prompt = f"""
You are an expert fact-checking AI.

Your job:
1. Verify whether the claim is accurate.
2. Compare against web evidence.
3. Return one label only:
   - Verified
   - Inaccurate
   - False

Definitions:
- Verified = claim matches trusted evidence.
- Inaccurate = partially correct or outdated.
- False = no supporting evidence or clearly wrong.

Then provide:
- Explanation
- Correct fact if available

CLAIM:
{claim}

WEB DATA:
{web_data[:10000]}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional fact-checker."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content
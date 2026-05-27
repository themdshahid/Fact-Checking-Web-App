import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_claim(claim):
    try:
        response = client.search(
            query=claim,
            search_depth="advanced",
            max_results=5
        )

        results = response.get("results", [])

        combined_text = ""

        for result in results:
            combined_text += f"Title: {result.get('title')}\n"
            combined_text += f"Content: {result.get('content')}\n"
            combined_text += f"URL: {result.get('url')}\n\n"

        return combined_text

    except Exception as e:
        return f"Search error: {str(e)}"
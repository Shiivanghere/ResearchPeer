from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

session = requests.Session()

session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml",
    "Connection": "keep-alive"
})

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    results = tavily.search(query=query,max_results=5)

    #web_search.invoke("What impacts the stock market the most ?")

    out = []

    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    
    return "\n----\n".join(out)

# @tool
# def scrape_url(url: str) -> str:
#     """Scrape and return clean text content from a given URL for deeper reading."""
#     try:
#         resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
#         soup = BeautifulSoup(resp.text, "html.parser")
#         for tag in soup(["script", "style", "nav", "footer"]):
#             tag.decompose()
#         return soup.get_text(separator=" ", strip=True)[:3000]
#     except Exception as e:
#         return f"Could not scrape URL: {str(e)}"

@tool
def scrape_url(url: str) -> str:
    """Scrape webpage content for deeper reading."""

    try:
        response = session.get(
            url,
            timeout=20,
            allow_redirects=True
        )

        response.raise_for_status()

        response.encoding = response.apparent_encoding

        if "text/html" not in response.headers.get("Content-Type", ""):
            return "URL is not an HTML page."

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup([
            "script",
            "style",
            "header",
            "footer",
            "nav",
            "aside",
            "noscript",
            "svg",
            "img"
        ]):
            tag.decompose()

        text = soup.get_text(" ", strip=True)
        text = " ".join(text.split())

        if len(text) < 200:
            return "Could not extract meaningful content."

        return text[:6000]

    except requests.exceptions.Timeout:
        return "Request timed out."

    except requests.exceptions.ConnectionError:
        return "Connection failed."

    except requests.exceptions.HTTPError as e:
        return f"HTTP Error: {e}"

    except Exception as e:
        return f"Scraping failed: {e}"
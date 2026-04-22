from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from typing import List

def web_search(
    web_query: str, 
    num_results: int) -> List[str]:
    wrapper = DuckDuckGoSearchAPIWrapper(
        time='d',
        max_results=num_results)
    try:
        results =wrapper.results(web_query, num_results)
        return [r['link'] for r in results]
    except Exception as e:
        print(f"An error occurred during web search: {e}")
        return []
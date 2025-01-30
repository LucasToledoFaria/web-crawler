import aiohttp
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.crawler.utils import is_valid_url, is_media_url


async def fetch(session, url, semaphore):
    async with semaphore:
        try:
            async with session.get(url) as response:
                if response.status != 200:
                    return None
                content_type = response.headers.get('Content-Type', '').lower()
                if 'text/html' not in content_type:
                    return None
                return await response.text()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None


async def get_links(session, url, depth, max_urls, visited, all_urls, semaphore):
    if depth == 0 or max_urls <= 0:
        return {"link": url, "founded_links": []}

    data = await fetch(session, url, semaphore)
    if data is None:
        return {"link": url, "founded_links": []}

    soup = BeautifulSoup(data, "html.parser")
    links = soup.find_all("a")

    urls = []
    for link in links:
        route = link.get("href")
        if route:
            full_url = urljoin(url, route)
            if is_valid_url(full_url) and not is_media_url(full_url):
                all_urls.append(full_url)
                if full_url not in visited:
                    visited.add(full_url)
                    urls.append(full_url)
                    if len(urls) >= max_urls:
                        break

    tasks = [
        get_links(
            session, link, depth - 1, max_urls - len(urls), visited, all_urls, semaphore
        )
        for link in urls
    ]
    founded_links = await asyncio.gather(*tasks)

    return {"link": url, "founded_links": founded_links}


async def main(url, **kwargs):
    max_depth = kwargs.get("max_depth", 100)
    max_urls = kwargs.get("max_urls", 5000)
    max_connections = kwargs.get("max_connections", 10)
    max_host_connections = kwargs.get("max_host_connections", 5)

    visited = set()
    all_urls = []
    semaphore = asyncio.Semaphore(max_connections)
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(
            limit_per_host=max_host_connections,
        )
    ) as session:
        urls_dict = await get_links(
            session, url, max_depth, max_urls, visited, all_urls, semaphore
        )

    return urls_dict, all_urls


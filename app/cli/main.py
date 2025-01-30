import typer
from typing_extensions import Annotated
from typing import Optional
from app.crawler.utils import is_valid_url
from app.crawler.crawler import main as crawler
import asyncio
import json

app = typer.Typer()

def url_callback(url: str):
    while not is_valid_url(url):
        raise typer.BadParameter("The provided URL is not valid.")
    return url

@app.command()
def main(
    url: Annotated[str, typer.Option("--url", "-url", prompt="Please enter the URL of the site to be crawled", callback=url_callback, help="The URL of the site to be crawled")], 
    max_depth: Annotated[Optional[int], typer.Option("--max-depth", "-d", help="The maximum depth to crawl", show_default="3")] = None,
    max_urls: Annotated[Optional[int], typer.Option("--max-urls", "-u", help="The maximum number of URLs to crawl", show_default="200")] = None,
    max_connections: Annotated[Optional[int], typer.Option("--max-connections", "-c", help="The maximum number of concurrent connections", show_default="20")] = None,
    max_host_connections: Annotated[Optional[int], typer.Option("--max-host-connections", "-h", help="The maximum number of concurrent connections per host", show_default="10")] = None
):

    print(f"Crawling {url}. Please wait for the files to be saved in the output folder.")
    
    kwargs = {
        "max_depth": max_depth,
        "max_urls": max_urls,
        "max_connections": max_connections,
        "max_host_connections": max_host_connections
    }
    kwargs = {k: v for k, v in kwargs.items() if v is not None}
    
    urls_dict, all_urls = asyncio.run(
        crawler(url, **kwargs)
    )

    print(f"Found {len(all_urls)} URLs in total.")
    
    with open("crawl_result.json", "w") as f:
        json.dump(urls_dict, f, indent=4)
    with open("all_urls.txt", "w") as f:
        f.write("\n".join(all_urls))
    print("Results saved in the output folder.")

if __name__ == "__main__":
    app()

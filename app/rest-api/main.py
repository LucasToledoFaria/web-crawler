from fastapi import FastAPI, HTTPException
from typing import List, ForwardRef
from pydantic import BaseModel, HttpUrl, Field, ValidationError
from app.crawler.crawler import main as crawler

app = FastAPI(
    title="Website Crawler API",
    description="Crawl a site to extract all links from the main page and its referenced pages.",
    version="0.0.1"
)

URLsDictRef = ForwardRef("URLsDict")

class URLsDict(BaseModel):
    link: HttpUrl = Field(..., description="The URL of the crawled page.")
    founded_links: List[URLsDictRef] = Field(default=list([]), description="List of URLs found on the crawled page.")

URLsDict.model_rebuild()

class Params(BaseModel):
    url: str = Field(..., description="The URL of the site to be crawled.")
    max_depth: int | None = Field(3, description="The maximum depth to crawl (default: 3).")
    max_urls: int | None = Field(200, description="The maximum number of URLs to crawl (default: 200).")
    max_connections: int | None = Field(20, description="The maximum number of concurrent connections (default: 20).")
    max_host_connections: int | None = Field(10, description="The maximum number of concurrent connections per host (default: 10).")

class CrawlResponse(BaseModel):
    urls_dict: URLsDict = Field(..., description="A dictionary representing the structure of the crawled URLs.")
    all_urls: List[str] = Field(..., description="A list of all URLs found during the crawl.")

@app.post("/", response_model=CrawlResponse, summary="Crawl a website", description="Crawl a website to extract all links from the main page and its referenced pages.")
async def crawl(params: Params) -> CrawlResponse:
    try:
        urls_dict, all_urls = await crawler(params.url, **params.dict(exclude={"url"}))
        return CrawlResponse(urls_dict=urls_dict, all_urls=all_urls)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

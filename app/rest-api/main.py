from fastapi import FastAPI, HTTPException
from typing import List, ForwardRef
from pydantic import BaseModel, HttpUrl, Field, ValidationError
from app.crawler.crawler import main as crawler

app = FastAPI()

URLsDictRef = ForwardRef("URLsDict")

class URLsDict(BaseModel):
    link: HttpUrl
    founded_links: List[URLsDictRef] = Field(default=list([]))

URLsDict.model_rebuild()

class Params(BaseModel):
    url: str
    max_depth: int | None = 3
    max_urls: int | None = 200
    max_connections: int | None = 20
    max_host_connections: int | None = 10

class CrawlResponse(BaseModel):
    urls_dict: URLsDict
    all_urls: List[str]

@app.post("/", response_model=CrawlResponse)
async def crawl(params: Params) -> CrawlResponse:
    try:
        urls_dict, all_urls = await crawler(params.url, **params.dict(exclude={"url"}))
        return CrawlResponse(urls_dict=urls_dict, all_urls=all_urls)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")

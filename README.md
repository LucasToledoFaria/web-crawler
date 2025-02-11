# Website Crawler

> Crawl a site to extract all links from the main page and its referenced pages.

This project was created to test my development skills. Feel free to give me feedback and help me improve my abilities!

## Usage

### As a Python Module

1. Install the required dependencies:

   ```bash
   pip install -r app/requirements.txt
   ```

2. Use the crawler in your Python code:

   ```python
   import asyncio
   from app.crawler.crawler import main as crawl

   url = 'http://example.com'

   urls_dict, all_urls = asyncio.run(crawl(url, max_depth=3, max_urls=200, max_connections=20, max_host_connections=10))

   print(urls_dict)
   print(all_urls)
   ```

   The `main` function returns two values:

   - `urls_dict`: A dictionary representing the structure of the crawled URLs.
   - `all_urls`: A list of all URLs found during the crawl.

#### Optional Arguments

- `max_depth`: The maximum depth to crawl (default: 3). This controls how many levels deep the crawler will go from the initial URL.
- `max_urls`: The maximum number of URLs to crawl (default: 200). This limits the total number of URLs the crawler will visit.
- `max_connections`: The maximum number of concurrent connections (default: 20). This sets the limit on how many simultaneous requests the crawler can make.
- `max_host_connections`: The maximum number of concurrent connections per host (default: 10). This restricts the number of simultaneous connections to a single host.

You can adjust these parameters to control the behavior of the crawler according to your needs.

### Using the CLI Tool

1. Make sure the `install.sh` file is executable:

   ```bash
   chmod +x app/cli/install.sh
   ```

2. Run the `install.sh` script:

   ```bash
   ./app/cli/install.sh
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Run the CLI tool:

   ```bash
   python app/cli/main.py --url http://example.com --max-depth 3 --max-urls 200 --max-connections 20 --max-host-connections 10
   ```

   The CLI tool saves the results in two files:

   - `crawl_result.json`: A JSON file containing the structure of the crawled URLs.
   - `all_urls.txt`: A text file listing all URLs found during the crawl.

#### Optional Arguments

- `--max-depth` (`-d`): The maximum depth to crawl (default: 3). This controls how many levels deep the crawler will go from the initial URL.
- `--max-urls` (`-u`): The maximum number of URLs to crawl (default: 200). This limits the total number of URLs the crawler will visit.
- `--max-connections` (`-c`): The maximum number of concurrent connections (default: 20). This sets the limit on how many simultaneous requests the crawler can make.
- `--max-host-connections` (`-h`): The maximum number of concurrent connections per host (default: 10). This restricts the number of simultaneous connections to a single host.

You can adjust these parameters to control the behavior of the crawler according to your needs.

### Using the REST API

1. Make sure the `install.sh` file is executable:

   ```bash
   chmod +x app/rest-api/install.sh
   ```

2. Run the `install.sh` script:

   ```bash
   ./app/rest-api/install.sh
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

4. Start the REST API server:

   ```bash
   uvicorn app.rest-api.main:app --host 0.0.0.0 --port 8080
   ```

5. Use the API to crawl a website by sending a POST request to `http://localhost:8080/` with the following JSON body:

   ```json
   {
     "url": "http://example.com",
     "max_depth": 3,
     "max_urls": 200,
     "max_connections": 20,
     "max_host_connections": 10
   }
   ```

   The API will respond with a JSON object containing:

   - `urls_dict`: A dictionary representing the structure of the crawled URLs.
   - `all_urls`: A list of all URLs found during the crawl.

6. To see the API documentation, visit the `/docs` endpoint:

   ```bash
   http://localhost:8080/docs
   ```

#### Optional Arguments

- `max_depth`: The maximum depth to crawl (default: 3). This controls how many levels deep the crawler will go from the initial URL.
- `max_urls`: The maximum number of URLs to crawl (default: 200). This limits the total number of URLs the crawler will visit.
- `max_connections`: The maximum number of concurrent connections (default: 20). This sets the limit on how many simultaneous requests the crawler can make.
- `max_host_connections`: The maximum number of concurrent connections per host (default: 10). This restricts the number of simultaneous connections to a single host.

You can adjust these parameters to control the behavior of the crawler according to your needs.

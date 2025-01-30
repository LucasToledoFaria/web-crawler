from urllib.parse import urljoin, urlparse


def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def is_media_url(url):
    media_extensions = (
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp",
        ".mp4",
        ".mp3",
        ".avi",
        ".mov",
        ".wmv",
        ".flv",
        ".mkv",
        ".pdf",
        ".zip",
        ".rar",
        ".tar",
        ".gz",
        ".doc",
        ".docx",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".txt",
    )
    return url.lower().endswith(media_extensions)


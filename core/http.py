import requests

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))

def get(url, **kwargs):
    response = requests.get(
        url,
        timeout=30,
        headers={
            "User-Agent": "DevOps-Security-Digest"
        },
        **kwargs
    )
    response.raise_for_status()
    return response

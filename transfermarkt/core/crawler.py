import requests

from bs4 import BeautifulSoup

TRANSFERMARKT_URL = "https://www.transfermarkt.com"

CRAWLER_AGENT = "tranfermarkt-py"


def fetch_content(url_endpoint: str) -> BeautifulSoup:
    res = requests.get(
        TRANSFERMARKT_URL + url_endpoint,
        headers={'user-agent': CRAWLER_AGENT}
    )
    return BeautifulSoup(res.text, 'html.parser')

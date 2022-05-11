from __future__ import annotations

import time

import requests


HEADERS = {
    "User-Agent": "wupch"
}


def get_page(url: str) -> str:
    r = requests.get(url, headers=HEADERS)
    if not r:
        r.raise_for_status()
    return r.text


def notify() -> None:
    pass


def main() -> None:
    last_fetch = ""
    while True:
        print("fetching...")
        body = get_page("http://3dscapture.com/ds/order.html")
        print("fetched!")
        if body != last_fetch:
            print("change detected!")
            last_fetch = body
        time.sleep(10)


if __name__ == "__main__":
    main()

import time
import requests


def get_json(url, params=None, retries=3):
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, params=params, timeout=10)
        except (requests.Timeout, requests.ConnectionError):
            print(f"attempt {attempt}: no reply")
        else:
            if r.status_code == 200:
                return r.json()
            if r.status_code < 500 and r.status_code != 429:
                r.raise_for_status()
            print(f"attempt {attempt}: status {r.status_code}")
        time.sleep(2 ** attempt)
    raise RuntimeError(f"gave up on {url} after {retries} attempts")


def fetch_all_pages(url, page_size=20):
    rows = []
    page = 1
    while True:
        batch = get_json(url, params={"_page": page, "_limit": page_size})
        if not batch:
            break
        rows.extend(batch)
        page += 1
    return rows


if __name__ == "__main__":
    posts = fetch_all_pages("https://jsonplaceholder.typicode.com/posts")
    print("posts fetched:", len(posts))
    get_json("https://jsonplaceholder.typicode.com/posts/9999")

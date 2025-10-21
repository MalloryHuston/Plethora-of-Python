# wikipedia app

import os
import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
requests.packages.urllib3.disable_warnings()

HEADERS = {
    "User-Agent": (
        "WikiCLI-Scraper/1.0 (https://example.com; contact@example.com)"
    )
}


def sanitize_filename(name: str) -> str:
    return "".join(
        c if c.isalnum() or c in (' ', '-', '_') else '_'
        for c in name
    )


def get_first_paragraph(soup: BeautifulSoup) -> str:
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if text:
            return text
    return "No content found."


def download_image(
    soup: BeautifulSoup,
    output_dir: str,
    base_url: str = 'https://en.wikipedia.org'
) -> None:
    """Download the main image from a Wikipedia article, if one exists."""
    # First try <a class='image'> logic
    a = soup.find('a', class_='image')
    if a:
        try:
            image_page_url = base_url + a['href']
            img_page_resp = requests.get(
                image_page_url, headers=HEADERS, timeout=10
            )
            img_page_resp.raise_for_status()
            img_soup = BeautifulSoup(img_page_resp.text, 'html.parser')
            div = img_soup.find('div', class_='fullImageLink')

            if div and (img_tag := div.find('a')):
                image_url = 'https:' + img_tag['href']
            else:
                raise ValueError("No fullImageLink found.")

            img_data = requests.get(
                image_url, headers=HEADERS, timeout=10
            ).content
            image_name = os.path.basename(image_url)
            image_path = os.path.join(output_dir, image_name)

            with open(image_path, 'wb') as img_file:
                img_file.write(img_data)

            print(f"✅  Image saved as: {image_path}")
            return

        except Exception as e:
            print(f"⚠️  Failed to fetch full-res image: {e}")

    # Fallback: image from infobox
    try:
        infobox = soup.find('table', class_='infobox')
        if infobox:
            img_tag = infobox.find('img')
            if img_tag and img_tag.get('src'):
                image_url = 'https:' + img_tag['src']
                img_data = requests.get(
                    image_url, headers=HEADERS, timeout=10
                ).content
                image_name = os.path.basename(image_url)
                image_path = os.path.join(output_dir, image_name)

                with open(image_path, 'wb') as img_file:
                    img_file.write(img_data)

                print(f"✅  Fallback image saved as: {image_path}")
                return

        print("⚠️  No suitable image found in infobox fallback.")
    except Exception as e:
        print(f"❌  Failed to download fallback image: {e}")


def query_wikipedia(
    keyword: str,
    output_dir: str = None,
    download: bool = False
) -> None:
    """Fetch a Wikipedia summary and optionally save the lead image."""
    base_url = 'https://en.wikipedia.org'
    search_term = sanitize_filename(keyword)
    output_dir = output_dir or os.getcwd()
    article_dir = os.path.join(output_dir, search_term)

    os.makedirs(article_dir, exist_ok=True)

    url = f"{base_url}/wiki/{keyword.replace(' ', '_')}"
    print(f"🔎  Fetching Wikipedia page for: {keyword} ...")

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            print(f"❌  Page not found (status code {response.status_code}).")
            return
    except requests.RequestException as e:
        print(f"❌  Failed to connect to Wikipedia: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraph = get_first_paragraph(soup)

    article_path = os.path.join(article_dir, f"{search_term}.txt")
    with open(article_path, 'w', encoding='utf-8') as f:
        f.write(f"{paragraph}\n\n\nFor more info, visit {url}.")

    print(f"✅  Article saved to: {article_path}")

    if download:
        download_image(soup, article_dir)

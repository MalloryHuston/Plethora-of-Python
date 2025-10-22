import requests as rq
from bs4 import BeautifulSoup

url = input("Enter link: ").strip()

if url.startswith(("http://", "https://")):
    data = rq.get(url)
else:
    data = rq.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")
links = []

for link in soup.find_all("a"):
    href = link.get("href")
    if href and href.startswith("http"):
        links.append(href)

# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
with open("myLinks.txt", 'a') as saved:
    for link in links:
        print(link, file=saved)

print(f"A total of {len(links)} links have been found. "
      "Check out myLinks.txt for the radical list! 😎")

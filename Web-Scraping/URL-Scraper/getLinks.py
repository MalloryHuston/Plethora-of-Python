import requests as rq
from bs4 import BeautifulSoup

url = input("Enter link: ")
if ("https" or "http") in url:
    data = rq.get(url)
else:
    data = rq.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

# Writing the output to a file (myLinks.txt) instead of to stdout
# You can change 'a' to 'w' to overwrite the file each time
with open("myLinks.txt", 'a') as saved:
    print(links[:10], file=saved)
print("A total of {len(links)} links have been found. "
      "Check out myLinks.txt for the radical list! 😎")

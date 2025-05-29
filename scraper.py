import requests
from bs4 import BeautifulSoup
import csv

url = input("Enter the website URL to scrape (e.g., http://isg.rnu.tn/): ").strip()

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"Error fetching {url}: {e}")
    exit(1)

soup = BeautifulSoup(response.text, 'html.parser')

links = []
for link in soup.find_all('a', href=True):
    text = link.get_text(strip=True)
    href = link['href']
    links.append({'text': text, 'href': href})

csv_filename = 'scraped_links.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['text', 'href'])
    writer.writeheader()
    writer.writerows(links)

print(f"Saved {len(links)} links to {csv_filename}") 
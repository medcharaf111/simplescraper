# SimpleScraper

A simple Python web scraper that extracts all links from a user-provided website and saves them to a CSV file.

## Features
- Prompts the user for a website URL
- Scrapes all `<a>` links from the page
- Saves the link text and href to `scraped_links.csv`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/medcharaf111/simplescraper.git
   cd simplescraper
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the scraper with:
```bash
python scraper.py
```
Enter the website URL when prompted (e.g., `http://isg.rnu.tn`).

## Output
- The script creates a file called `scraped_links.csv` containing two columns:
  - `text`: The visible text of the link
  - `href`: The URL the link points to

## Example
```
text,href
"Home","/index.html"
"Contact","/contact.html"
...
```

## License
MIT

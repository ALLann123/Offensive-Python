from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import time

session = HTMLSession()

def scrape_links(url):
    """Extracts all valid links from the given webpage."""
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    links = set()
    for a_tag in soup.find_all('a', href=True):
        full_url = urljoin(url, a_tag['href'])  # Handle absolute and relative URLs properly
        links.add(full_url)

    return list(links)

def extract_emails(text):
    """Extracts all emails from the given text."""
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    return set(re.findall(email_pattern, text))

def scrape_emails(url):
    """Scrapes emails from the main page and sub-pages."""
    visited_urls = set()
    emails = set()

    # Start with the main URL
    urls_to_visit = [url]

    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
    ]

    while urls_to_visit:
        current_url = urls_to_visit.pop(0)

        if current_url in visited_urls:
            continue

        try:
            user_agent = user_agents[hash(current_url) % len(user_agents)]
            response = session.get(current_url, headers={'User-Agent': user_agent})
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract emails from the current page
            emails.update(extract_emails(soup.get_text()))

            # Extract new links to visit
            new_links = scrape_links(current_url)
            urls_to_visit.extend(new_links)

            visited_urls.add(current_url)

            # Rate limiting
            time.sleep(1)

        except Exception as e:
            print(f"Error scraping {current_url}: {e}")

    return list(emails)

# Input and execution
url = input("Enter the site>> ").strip()
result = scrape_emails(url)
print("Extracted Emails:", result)
import requests
from bs4 import BeautifulSoup
import time
import random

# URL of the page to scrape
url = "https://quotes.toscrape.com/"

# Make an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print quotes
quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)

# Extract and print authors
authors = soup.find_all("small", class_="author")
for author in authors:
    print(author.text)

# Sleep for a random interval between 1 and 3 seconds
s = random.uniform(1, 3)
print(f"Sleeping for {sleep_time:.2f} seconds")
time.sleep(sleep_time)

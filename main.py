
import requests
from bs4 import BeautifulSoup
import time
import random

# URL of the page to scrape
url = "https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/"

# Make an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the main content of the article
article_content = soup.find("div", class_="entry-content")

# Extract and print the text content of the article
paragraphs = article_content.find_all("p")
for para in paragraphs:
    print(para.get_text())

# Sleep for a random interval between 1 and 5 seconds
sleep_time = random.uniform(1, 5)
print(f"Sleeping for {sleep_time:.2f} seconds")
time.sleep(sleep_time)

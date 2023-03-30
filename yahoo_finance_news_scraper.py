# Programmer: Noah Bird
# Date: 3/11/23
# web scraper that pulls the most recent news headlines from yahoofinance.com
# best used to get a quick snapshot of current economic/market related news

# import the necessary libraries
import requests
from bs4 import BeautifulSoup

# define the url of the website to be scraped
url = 'https://finance.yahoo.com/news/'

# send a GET request to the website and get HTML content
response = requests.get(url)
html_content = response.content

# parse the HTML content using beautfulsoup
soup = BeautifulSoup(html_content, 'html.parser')

# find all the new headline elements
news_headlines = soup.find_all('h3', {'class': 'Mb(5px)'})

# print the numbered headlines with 1 being the most recent article
# strip extra white space and jump to next line after each article
for i, headline in enumerate(news_headlines, start=1):
    print(f"{i}. {headline.text.strip()}  \n")

# provide link to user in case they want to learn more
print("\nTo read these article visit\n https://finance.yahoo.com/news/ \n")
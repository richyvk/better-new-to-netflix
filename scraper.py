# scraper.py

from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.whats-on-netflix.com/australia/'
HEADERS = {'user-agent': 'better-new-to-netflix/1.0 (https://github.com/richyvk/better-new-to-netflix)'}


def scrap_new_movies(url=BASE_URL, which_article=0):
    """ Scrap most recent What's on Netflix Australia article for new
    movie titles.

    Returns list of {'title': title, 'year': year} dicts"""

    # scrap homepage for article urls
    homepage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(homepage.text, 'html.parser')
    articles = soup.find_all('h5', 'entry-title')
    selected_article = articles[which_article].contents
    selected_article_url = BASE_URL + selected_article[0]['href']
    print(f'Scraping {selected_article_url}')
    # scrap movies data from first article
    article_page = requests.get(selected_article_url, headers=HEADERS)
    article_soup = BeautifulSoup(article_page.text, 'html.parser')
    article_content = article_soup.find_all('div', 'post-content-container')
    uls = article_content[0].find_all('ul')
    if uls:  # check ul tags found
        new_movies = [li.text for li in uls[0].find_all('li')]

        # clean up movies data
        # remove first item if not a movie - i.e. no (date)
        if '(' not in new_movies[0]:
            new_movies.pop(0)
        # split movies into (title, date) tuples
        new_movies_split = []
        for m in new_movies:
            name = m[:m.find("(")-1]
            year = m[m.find("(")+1:m.find(")")]
            new_movies_split.append({'title': name, 'year': year})
        print('scrape successful')
        return new_movies_split
    print('Scrape failed: no ULs found')
    return False


def scrape_article_titles(url=BASE_URL):
    """ (str) -> list of string
    Scrape article titles from url.
    """
    homepage = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(homepage.text, 'html.parser')
    articles = soup.find_all('h5', 'entry-title')
    return [article.find('a').text for article in articles]

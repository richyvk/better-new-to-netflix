# main.py

import pickle
import sys

import db_models
import omdb
import scraper


if __name__ == '__main__':
    article_titles = scraper.scrape_article_titles()
    with open('last_scraped_title.p', 'rb') as f:
        last_scraped_title = pickle.load(f)

    scraped_movies = scraper.scrap_new_movies()
    if scraped_movies:
        if article_titles[0] != last_scraped_title:
            omdb_results = omdb.get_omdb_results(scraped_movies)

            if len(sys.argv) == 2 and sys.argv[1] == '--test':
                # test option - no db write
                print([m['Title'] for m in omdb_results if m['Response'] == 'True'])
            else:
                # write to db
                for m in omdb_results:
                    if m['Response'] == 'True':
                        db_models.add_movie(m['Title'],
                                            m['Year'],
                                            m['Genre'],
                                            m['Plot'],
                                            m['imdbRating'])
                print('Movies added to database')
            with open('last_scraped_title.p', 'wb') as f:
                pickle.dump(article_titles[0], f)
        else:
            print('No new article found')
    else:
        print('ERROR: No ULs found on scraped page')

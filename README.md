# Better new to netflix
> A tool to get data on new movies added to Netflix Australia.

A tool written in Python3 that scrapes the [What's New On Netflix](https://www.whats-on-netflix.com/australia/) site for new movies added to Netflix Australia. It then queries the [OMDb movie api](http://www.omdbapi.com/) for information about each movie, and adds the results to an sqlite database.

#  Requirements
- Python 3.6 - only because I used f-strings
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [PonyORM](https://ponyorm.com/)
- [Requests](http://docs.python-requests.org/en/master/)
- An OMDb api key

## Installation

From a terminal run:

```
pip install -r requirements.txt
python setup.py
```

## Usage

From a terminal run:
```
python main.py
```

## Other

- This is a work in progress. It's not class based because this is the limit of my knowledge currently.
- There are currently no tests.
- It will be subject to change, possibly radical change.
- I'm currently working on a Flask front-end.
- LICENCE: None (public domain)

# Better new to netflix
> A tool to get data on new movies added to Netflix Australia.

A tool written in Python3 that scrapes the [What's New On Netflix](https://www.whats-on-netflix.com/australia/) site for new movies added to Netflix Australia. It then queries the [OMDb movie api](http://www.omdbapi.com/) for information about each movie, and adds the results to an sqlite database.

#  Requirements
- Python 3.6
- BeautifulSoup
- PonyORM
- requests
- An OMDb api key

## Installation

For a terminal run:

```
pip install -r requirements.txt
python setup.py
```

## Usage

From a terminal run:
```
python main.py
```

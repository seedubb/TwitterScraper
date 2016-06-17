# TwitterScraper
A twitter scraper written in python which pulls recent tweets by account name, conducts sentiment analysis, and saves a file.

You will need to install some dependencies for this to run.

I recommend home-brew if running on mac : http://brew.sh/

Twython:
brew install twython

Dateutil:
pip install python-dateutil

TextBlob:
pip install text blob

	Note: will install NLTK. Both are used for sentiment analysis.

To run a file, run: python [candidate_name.py]

Example: python berne.py

TODO: 
Re-write script so python screen name is not hard coded.
Edit output file to be dynamically named and unique for screen/datetime.
Conduct additional analysis, and expand time range to fit with twitters API.
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# News from The New York Times Canada

toi_r = requests.get("https://www.nytimes.com/ca/section/politics")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



# News from CNN 

ht_r = requests.get("https://www.cnn.com/politics")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})
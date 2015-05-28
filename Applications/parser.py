#!/usr/bin/python

import sys
import feedparser
import utils
import html
import array
from goose import Goose
g = Goose()
from textblob import Word,TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

f1 = html.open_html_file("monogramme")
f2 = html.open_html_file("bigramme")
f3 = html.open_html_file("trigramme")

rss = "https://news.google.fr/news/feeds?tbm=nws&q="+sys.argv[1] 
#On recupere tous le contenu du rss avec une query
feeds = feedparser.parse(rss)
check = ""

for i in range(0, len(feeds.entries)):
  check = utils.check_ncl(feeds.entries[i]['summary_detail']['value'])
  if check != -1:
    break

if check == -1:
  sys.exit('Pas de cluster trouve')

#On a recupere le cluster, on recupere la liste de news
feeds = feedparser.parse(check)
news = []
for j in range(0, len(feeds.entries)):
	check = utils.check_news(feeds.entries[j]['links'][0]['href'])
	if check != -1:
		news.append(check)

#On recupere le contenu de la news
articles = []
for article in news:
	a = g.extract(url=article)
	articles.append(a.cleaned_text)

#On lemmatize et ensuite on calcul les ngrammes (mono, bi, tri)
for article in articles:
	blobs = TextBlob(article, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
	for sentence in blobs.sentences:
		tri = sentence.ngrams(n=3)
		for mono in tri:
			f3.write(" ".join(mono).encode('utf-8'))
			f3.write("\n")

html.close_html_file(f1)
html.close_html_file(f2)
html.close_html_file(f3)
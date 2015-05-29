#!/usr/bin/python

import sys
import feedparser
import utils
import html
import array
from nltk.corpus import stopwords
from goose import Goose
g = Goose()
from textblob import Word,TextBlob
from textblob.taggers import NLTKTagger
from pattern.vector import count, LEMMA
from pattern.en import parse,Sentence,Text,ngrams
from pattern.graph import Graph

reload(sys)  
sys.setdefaultencoding('utf8')


f = html.open_html_file()

rss = "https://news.google.fr/news/feeds?tbm=nws&hl=en&q="+sys.argv[1] 
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

stopwordsList = stopwords.words('english');

#On lemmatize et ensuite on calcul les ngrammes (mono, bi, tri)

'''
s = 'The black cat was spying on the white cat.'
s = Sentence(parse(s))
k=count(s, stemmer=LEMMA, exclude=['.', ','])
f3.write('\n'.join("{!s}={!r}".format(key,val) for (key,val) in k.items()))
exclude=[' ', '/', '.', ',', ';', ':', '!', '?', '(', ')', '[', ']', '{', '}', '\'', '`', '"', '@', '#', '$', '*', '+', '-', '|', '=', '~', '_', '...']
'''

dict = {}

from nltk.corpus import stopwords
cachedStopWords = stopwords.words("english")

for article in articles:
    text = TextBlob(article)
    for sentence in text.sentences:
        s = Sentence(parse(''.join(sentence), lemmata=True))
        for i in range (1, len(s.words)):
            k = ngrams(' '.join([word for word in s.lemmata if word not in cachedStopWords]), n=i, punctuation=".,;:!?()[]{}`'\"@#$^&*+-|=~_", continuous=False)
            if i not in dict:
                dict[i] = {}
            for kgram in k:
                if i > 1:
                    key = '#'.join(unkgram for unkgram in kgram)
                else:
                    key = kgram[0]
                if key in dict[i]:
                    dict[i][key] += 1
                else:
                    dict[i][key] = 1

for dgram in dict:
    html.make_graph(dict[dgram], dgram, 1000)
    for key in dict[dgram]:
        f.write(key.encode('utf-8').replace("#", ", "))
        f.write(' : ')
        f.write(str(dict[dgram][key]))
        f.write('<br>')
    f.write('_____________________________________________________________<br><br>')

html.close_html_file(f)

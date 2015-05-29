#!/usr/bin/python
"""Module utils contenant les fonctions de recuperation d url"""

def check_ncl(a):
	"""Fonction qui recupere l id du cluster"""
  #On recupere l index du cluster 
	e = a.find('ncl')
	if e == -1:
		return -1
	#On recupere l index du &
	i = a.find('&', e)
	#On recupere le cluster
	o =  a[e:i]
	#On reconstruit l url du cluster
	u = 'http://news.google.com/news/story?' + o + '&output=rss'
	return u

def check_news(a):
	"""Fonction qui recupere la liste de liens du cluster"""
	e = a.find('url=')
	if e == -1:
		return -1
	e+= 4
	return a[e:]
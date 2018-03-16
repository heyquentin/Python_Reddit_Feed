#! /usr/bin/python
import feedparser
d = feedparser.parse('http://www.reddit.com/r/vancouver/new/.rss')

for TELEDILDONICS in range(0,8):
	print d['entries'][TELEDILDONICS]['title'].encode('utf-8')
	print "-"	
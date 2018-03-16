#! /usr/bin/python
import feedparser
d = feedparser.parse('http://www.reddit.com/r/vancouver/new/.rss')

for TELEDILDONICS in range(0,8):
	print d['entries'][TELEDILDONICS]['title'].encode('utf-8')
	print "-"	


'''
stuff that might be useful down the road
-------------

print d['entries'][0]['title'].encode('utf-8')
print "-"
print d['entries'][1]['title'].encode('utf-8')
print "-"
print d['entries'][2]['title'].encode('utf-8')
print "-"
print d['entries'][3]['title'].encode('utf-8')
print "-"
print d['entries'][4]['title'].encode('utf-8')
print "-"
print d['entries'][5]['title'].encode('utf-8')
print "-"
print d['entries'][6]['title'].encode('utf-8')
print "-"
print d['entries'][7]['title'].encode('utf-8')

-------------

posts = []
#! for i in range(0, 5(d['entries'])):
for i in range(0,2):
	posts.append({
		d['entries'][i]['title'].encode('utf-8')
	})

print posts

-------------

for post in d.entries:
	print post.title + ":" + post.link + " "

print d['feed']['title']
print d['feed']['link']

'''
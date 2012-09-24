#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pub:
	def __init__(self, name, p, n):
		self.name = name
		self.p = p
		self.n = n

	def __str__(self):
		return ("%28s  :  %g/%g" % (self.name, self.p, self.n)).encode("utf-8")


from urllib2 import urlopen
from bs4 import BeautifulSoup
import re


p_n_regex = re.compile('.*(\d+\.\d+)/(\d+).*')

url = "http://www.pilsnerpubs.cz"
entryPage = urlopen(url).read().decode("windows-1250")
root = BeautifulSoup(entryPage, "html5lib")

pubs = []
table = root.find("table", {"class":"index-info"})
for tr in table("tr"):
	imgs = tr("img")
	if len(imgs) == 2:
		name = imgs[0]["alt"]
		p_n = re.match(p_n_regex, imgs[1]["title"])
		p = p_n.group(1)
		n = p_n.group(2)
		pub = Pub(name, float(p), float(n))
		print pub

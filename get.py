#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

MAX_RANK = float(5)

class Pub:
	def __init__(self, name, p, n):
		self.name = name
		self.p = p
		self.n = n

	def __str__(self):
		return ("%28s  :  %1.2g/%1g   " % (self.name, self.p, self.n)).encode("utf-8")


def score(pub, z):
	p = pub.p / MAX_RANK
	n = pub.n
	z = float(z)
	return MAX_RANK * (p + z*z/(2*n) - 
			z*math.sqrt((p*(1-p) + z*z/(4*n))/n)) / (1+z*z/n)



if __name__ == "__main__":
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
			print pub, round(score(pub, .5), 2)

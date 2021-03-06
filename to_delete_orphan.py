#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pywikibot
site = pywikibot.Site()
import requests
from wmflabs import db
conn = db.connect('cswiki')

params = {
	"action": "query",
	"format": "json",
	"meta": "siteinfo",
	"siprop": "namespaces"
}
r = requests.get('https://cs.wikipedia.org/w/api.php', params=params)
namespaces = r.json()['query']['namespaces']

cur = conn.cursor()
with cur:
	sql = open('sql.sql').read()
	cur.execute(sql)
	data = cur.fetchall()

for row in data:
	page = pywikibot.Page(site, namespaces[str(row[0])]['*'] + u':' + row[1].decode('utf-8'))
	page.delete(reason=u"Robot: Osiřelá diskusní stránka", mark=True)

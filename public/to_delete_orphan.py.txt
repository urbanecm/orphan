#!/usr/bin/env python
#-*- coding: utf-8 -*-

from wmflabs import db
conn = db.connect('cswiki')
import json

sql = u'SELECT page.page_id, page.page_namespace, page.page_title, page_1.page_title, page_1.page_id, page_1.page_namespace FROM page LEFT JOIN page AS page_1 ON (page.page_namespace = page_1.page_namespace+1) AND (page.page_title = page_1.page_title) WHERE (page.page_namespace=1) AND (page_1.page_title Is Null);'
cur = conn.cursor()
with cur:
	cur.execute(sql)
	data = cur.fetchall()

r_f = open('result.json', 'w')
r_f.write(json.dumps(data))

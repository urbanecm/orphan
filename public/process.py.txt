#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json

j_f = open('result.json', 'r')
j = json.loads(j_f.read())

r = []
for item in j:
	if u"/" not in unicode(item[2]):
		if item[1] == 1:
			r.append("Diskuse:" + item[2])
		elif item[1] == 15:
			r.append("Diskuse ke kategorii:" + item[2])
		elif item[1] == 5:
			r.append("Diskuse k Wikipedii:" + item[2])
		elif item[1] == 101:
			r.append("Diskuse k portálu:" + item[2])

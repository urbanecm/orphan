#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json

j_f = open('result.json', 'r')
j = json.loads(j_f.read())

r_f = open('result.txt', 'w')
r = []
for item in j:
	if u"/Úkoly" not in unicode(item[2]):
		r.append(item[2])

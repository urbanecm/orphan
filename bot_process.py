#!/usr/bin/env python

import os
import datetime
from process import *

d = datetime.date.today()

if len(r) != 0:
	filename = d.isoformat() + ".json"
	os.system('cp result.json ' + filename)
#	os.system('echo -e "Subject: [Wiki] Existuji nejake stranky ke smazani\\n\\nVysledek skriptu je na Toollabs ve slozce orphan s nazvem ' + filename +'.json." | /usr/sbin/exim -odf -i martin@urbanec.cz')
	os.system('echo "Vysledek skriptu je na toollabs ve slozce orphan s nazvem ' + filename + '."|/usr/bin/mail -s "[Wiki] Existuji nejake stranky ke smazani" martin@urbanec.cz')

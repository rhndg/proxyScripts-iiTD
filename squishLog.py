import re
import mechanize
import datetime
import fnmatch,time, sys, os

br = mechanize.Browser()

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
sq = 'https://proxy22.iitd.ernet.in/squish/squish1.cgi'



while 'true':
	ok = 'true'
	nw = datetime.datetime.now()
	time.sleep(3600-60*nw.minute)

	try :
		br.open(sq)
	except:
		ok = 'false'

	if ok == 'true' :
		br.select_form(nr=0)
		br.form['uid'] = 'entry number'
		br.form['magic_word'] = 'password'
		r=br.submit()
		html = r.read()
		pattern = '[0-9]+\.?[0-9]*(mb|Gb)'
		regex = re.compile(pattern,re.MULTILINE)
		print nw
		for match in regex.finditer(html):
			print match.group(0)

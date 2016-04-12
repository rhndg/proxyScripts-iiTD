import mechanize
import re
import time

br = mechanize.Browser()
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

pr = 'https://proxy22.iitd.ernet.in/cgi-bin/proxy.cgi'
loggedIn='false'
timeout = 1
pattern = '.*(success).*'
regex = re.compile(pattern,re.DOTALL)
ok='true'
while 'true':

	try :
		br.open(pr)
	except:
		ok = 'false'
		timeout = 1
	if ok == 'true' :
		br.select_form(nr=0)
		br.form['userid'] = 'entry number'
		br.form['pass'] = 'password'
		html = br.submit().read()
		print html
		if re.match(regex,html) is not None:
			timeout = 60
		else:
			timeout = 1
	
	time.sleep(timeout)



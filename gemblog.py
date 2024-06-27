#!/usr/bin/env python3
import os
import sys
import datetime
import time
import config as config

path = os.getenv('PATH_INFO', "")
splitted = [s for s in path.split("/") if s != ""]
query = os.getenv('QUERY_STRING', "")
cwd = os.getenv('SCRIPT_NAME', "")
gemfiles = os.listdir(config.GEMBLOG_ROOT)

def ok():
	print("20 text/gemini;charset=utf-8;lang="+config.GEMBLOG_LANGUAGE)
	print("# " + config.GEMBLOG_HEADER)
	print("## " + config.GEMBLOG_HEADER2)

def redirect(path="/"):
	print("31 "+path)
	return

def blogentry(url, title, date, sample):
	print("=> /"+url.replace(" ", "%20")+" "+config.GEMBLOG_ICON_ENTRY+title)
	print(date)
	print(sample)
	

def list_years():
	print("### "+config.GEMBLOG_POSTS)
	years = []
	for d in gemfiles:
		create = datetime.datetime.strptime(time.ctime(os.path.getmtime(config.GEMBLOG_ROOT+d)), "%a %b %d %H:%M:%S %Y")
		year = create.year
		if year not in years:
			years.append(year)
	for y in years:
		print("=> "+cwd+"/"+str(y)+" "+config.GEMBLOG_ICON_YEAR+str(y))

def list_month(pyear):
	try:
		ptest = int(pyear) + 1
	except:
		redirect(cwd)

	ok()
	print("=> "+cwd+"/ "+config.GEMBLOG_INDEX)
	print("")
	print("### " +config.GEMBLOG_ICON_YEAR+ str(pyear) + ":")
	months = []
	for d in gemfiles:
		create = datetime.datetime.strptime(time.ctime(os.path.getmtime(config.GEMBLOG_ROOT+d)), "%a %b %d %H:%M:%S %Y")
		year = create.year
		if str(year) != str(pyear):
			continue
		month = create.month
		if month not in months:
			months.append(month)
	for m in months:
		print("=> "+cwd+"/"+str(year)+"/"+str(m)+" "+config.GEMBLOG_ICON_MONTH+str(datetime.date(1900, m, 1).strftime("%B")))

def list_blogentries(pyear, pmonth):
	try:
		ptest = int(pyear) + 1
	except:
		redirect(cwd)
	try:
		ptest = int(pmonth) + 1
	except:
		redirect(cwd)

	if int(pmonth) < 1 or int(pmonth) > 12:
		redirect(cwd)

	ok()
	print("=> "+cwd+"/ "+config.GEMBLOG_INDEX)
	print("=> "+cwd+"/"+pyear+"/ "+config.GEMBLOG_ICON_YEAR+str(pyear))
	print("")
	print("### " +config.GEMBLOG_ICON_MONTH+ pyear + " / " + datetime.date(1900, int(pmonth), 1).strftime("%B") + ":")
	sortedf = gemfiles.copy()
	sortedf.sort(key=lambda x: os.path.getmtime(config.GEMBLOG_ROOT+x))
	sortedf.reverse()
	for filep in sortedf:
		create = datetime.datetime.strptime(time.ctime(os.path.getmtime(config.GEMBLOG_ROOT+filep)), "%a %b %d %H:%M:%S %Y")
		year = create.year
		if str(year) != str(pyear):
			continue
		month = create.month
		if str(month) != str(pmonth):
			continue
		with open(config.GEMBLOG_ROOT+filep) as input_file:
			head = [next(input_file) for _ in range(2)]
		head.insert(0, "")
		blogentry(config.GEMBLOG_ROOT+filep, filep.replace(".gmi", ""), create, "> ".join(head))

def list_recent(num):
	print("### "+config.GEMBLOG_RECENT)
	listed = []
	sortedf = gemfiles.copy()
	sortedf.sort(key=lambda x: os.path.getmtime(config.GEMBLOG_ROOT+x))
	sortedf.reverse()
	counter = 0
	for filep in sortedf:
		counter += 1
		if counter > num:
			return
		with open(config.GEMBLOG_ROOT+filep) as input_file:
			head = [next(input_file) for _ in range(2)]
		head.insert(0, "")
		blogentry(config.GEMBLOG_ROOT+filep, filep.replace(".gmi", ""), datetime.datetime.strptime(time.ctime(os.path.getmtime(config.GEMBLOG_ROOT+filep)), "%a %b %d %H:%M:%S %Y"), "> ".join(head))


def index():
	print(config.GEMBLOG_INTRO)
	print("")
	list_years()
	if config.GEMBLOG_ENABLE_RECENT:
		print("")
		list_recent(config.GEMBLOG_RECENT_COUNT)

if not path or path == "/":
	ok()
	index()
else:
	count = len(splitted)
	if count == 1:
		# hónap
		list_month(splitted[0])
	elif count == 2:
		# nap
		list_blogentries(splitted[0], splitted[1])
	else:
		redirect(cwd)

print("")
print(config.GEMBLOG_OUTRO)
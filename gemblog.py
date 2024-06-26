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

def list_years():
	print("### "+config.GEMBLOG_POSTS)
	years = []
	for d in gemfiles:
		create = datetime.datetime.strptime(time.ctime(os.path.getmtime(config.GEMBLOG_ROOT+d)), "%a %b %d %H:%M:%S %Y")
		year = create.year
		if year not in years:
			years.append(year)
	for y in years:
		print("=> "+cwd+"/"+str(y)+" "+str(y))

def list_month(pyear):
	print("=> "+cwd+"/ "+config.GEMBLOG_BACK)
	print("")
	print("### " + str(pyear) + ":")
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
		print("=> "+cwd+"/"+str(year)+"/"+str(m)+" "+str(datetime.date(1900, m, 1).strftime("%B")))

def list_days(pyear, pmonth):
	print("=> "+cwd+"/"+pyear+"/ "+config.GEMBLOG_BACK)
	print("")
	print("### " + pyear + " / " + datetime.date(1900, int(pmonth), 1).strftime("%B") + ":")
	listed = []
	for filep in gemfiles:
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
		print("=> /"+config.GEMBLOG_ROOT+filep + " " + filep)
		print(create)
		print(">".join(head))

def list_recent(num):
	print("### "+config.GEMBLOG_RECENT)
	listed = []
	sortedf = gemfiles.copy()
	sortedf.sort(key=lambda x: os.path.getmtime(config.GEMBLOG_ROOT+x))
	counter = 0
	for filep in sortedf:
		counter += 1
		if counter > num:
			return
		with open(config.GEMBLOG_ROOT+filep) as input_file:
			head = [next(input_file) for _ in range(2)]
		head.insert(0, "")
		print("=> /"+config.GEMBLOG_ROOT+filep + " " + filep)
		print(datetime.datetime.strptime(time.ctime(os.path.getmtime(config.GEMBLOG_ROOT+filep)), "%a %b %d %H:%M:%S %Y"))
		print(">".join(head))


def index():
	print(config.GEMBLOG_INTRO)
	print("")
	list_years()
	if config.GEMBLOG_ENABLE_RECENT:
		print("")
		list_recent(5)

print("20 text/gemini")
print("# " + config.GEMBLOG_HEADER)
print("## " + config.GEMBLOG_HEADER2)
if not path or path == "/":
	index()
else:
	count = len(splitted)
	if count == 1:
		# hónap
		list_month(splitted[0])
	elif count == 2:
		# nap
		list_days(splitted[0], splitted[1])
	else:
		print("oh no :c")
		print(str(count))

print("")
print(config.GEMBLOG_OUTRO)
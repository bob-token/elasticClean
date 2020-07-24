#!/usr/local/bin/python2
# -*- encoding: utf-8 -*-

from requests.auth import HTTPBasicAuth

import requests
import datetime


def deleteIndex(index):
    ret = requests.delete('http://118.31.52.80:9200/'+index, auth=HTTPBasicAuth('elastic', 'elastic'))
    index = ret.content
    return index


def validate(date_text):
    try:
        return datetime.datetime.strptime(date_text, '%Y.%m.%d')
    except ValueError:
        # print ValueError(date_text+": Incorrect data format, should be YYYY.MM.DD")
        return ""

ret=requests.get('http://118.31.52.80:9200/_cat/indices?v&s=index', auth=HTTPBasicAuth('elastic', 'elastic'))
index=ret.content.splitlines()

for p in index:

    line = p.split( )
    iname = line[2]
    date=iname.rsplit("-")
    date = date[date.__len__()-1]
    newtime = validate(date)
    if newtime == "":
        continue
    now = datetime.datetime.now()
    ts = now.strftime('%Y.%m.%d')
    now_7 = now - datetime.timedelta(days=7)

    if now_7 > newtime:
        print "delete iname result:"+deleteIndex(iname)






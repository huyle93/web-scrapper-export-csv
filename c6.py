#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:21:06 2017

@author: Huy
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

myRec = []
d = []
html = urlopen("http://www.showmeboone.com/sheriff/jailresidents/")
soup = BeautifulSoup(html, "html.parser")
tbl = soup.find("tbody", {"id": "mrc_main_table"})

for row in tbl.findAll("tr")[1:]:
    for a in row.find_all('a', href=True):
        href = a['href']
    col = row.findAll('td')
    column = href,col[1].text, col[2].text, col[3].text, col[4].text, col[5].text, col[6].text, col[7].text, col[8].text
    myRec.append(column)
with open('myfile.csv', 'a') as outcsv:   
    writer = csv.writer(outcsv, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for item in myRec:
        writer.writerow(item)

#!/usr/bin/python3

# coding: utf-8

import sys

import io

import urllib.parse

from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = "comment.txt"


html="""Content-type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<h1>WEC1掲示板</h1>
<p>===========================================</p>
"""

print(html)

def print_msg(name,text):

    data = {}

    with open(files,"a",encoding='utf-8') as w_data:

        w_data.write(name+':'+text+'<br>\n')

 

def documentsDisplay():

    with open(files,"r",encoding='utf-8') as r_data:

        #html_scan = r_data.read()

        #print(html_scan)

        for text in r_data:

            print(text)

documentsDisplay()

data_scan = {}

html2="""
<p>===========================================</p>
<form action="board.cgi" method="POST">
名前:<input type="text" name="id" value="名無しの学生" size="30"/><br>
コメント:<br><textarea style="line-hight: 20px" name="message" row="8" cols="50" wrap="hard" placeholder="コメントを記入"></textarea>
<input type="submit" name="submit" value="投稿"/>
</form>
</body>
</html>
"""
 
print(html2)

scan = input()

scan = urllib.parse.unquote(scan) 

scan = scan.split("&") 

for scanner in scan:

    (key,value)=scanner.split("=")

    data_scan[key] = value

print_msg(data_scan["id"],data_scan["message"])

print('<meta http-equiv="Refresh" content="0;URL=">')

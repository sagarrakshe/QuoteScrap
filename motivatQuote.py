#! /usr/bin/python 
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import commands
from datetime import *

mech = Browser()
url = "file:life-lessons.html"
page = mech.open(url)
html = page.read()

soup = BeautifulSoup(html)
temp = soup.html.ol
temp = temp.findAll("li")

#selection job
date=str(datetime.now()).split(" ")[0].split("-")[2]
fp=open(".DateAndNo","r")
dateIndex=str(fp.readline()).split(" ")
fp.close()

if dateIndex[0]==date:
    #print "same"
    index=int(dateIndex[1][0])
else:
    #print "different"
    index=int(dateIndex[1][0])
    fp=open(".DateAndNo","w")
    if index==541:
        index=0
    else:
        index=index+1
    fp.write(date+" "+str(index)+"\n")
    fp.close()

tmp=str(temp[index])[4:][:-5].split("(")[0]
string= "notify-send \"" + tmp +"\""

#display job (decide when to display)
commands.getoutput(string)

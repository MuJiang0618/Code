# -*- coding:utf-8 -*-
import bs4
import requests
from bs4 import BeautifulSoup

def thesoup(url):
    r=requests.get(url)
    r.encoding='utf-8'
    demo=r.text
    return demo

def fillunivlist(univlist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            list1=tr('td')
            univlist.append([list1[0].string,list1[1].string,list1[3].string])

def printunivlist(univlist,num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名','学校名称','总分'))
    for i in range(num):
        u=univlist[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))

def main():
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    univlist=[]
    html=thesoup(url)
    fillunivlist(univlist,html)
    printunivlist(univlist,20)

main()
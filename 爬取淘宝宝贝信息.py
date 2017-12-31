import re 
import requests

def getHTMLText(url):
    s=requests.get(url)
    s.encoding='utf-8'
    return s.text

def ParsePage(infolist,html):
    pricelist=re.findall(r'"view_price":"[\d.]*"',html)
    goodsnamelist=re.findall(r'"raw_title":".*?"',html)
    for n in range(len(pricelist)):
        price=eval(pricelist[n].split(':')[1])
        goodsname=eval(goodsnamelist[n].split(':')[1])
        infolist.append([price,goodsname])

def PrintInfo(infolist):
    match='{:4}\t{:8}\t{:16}'
    counter=1
    for i in infolist:
        print(match.format(counter,i[0],i[1]))
        counter=counter+1


def main():
    goods=input('你想要什么宝贝?\n')
    infolist=[]
    start_html='https://s.taobao.com/search?q=' + goods
    depth=3     #获取的信息的页面数
    for i in range(depth):
        url =start_html+'&s='+str(44*i)
        html=getHTMLText(url)
        ParsePage(infolist,html)
        
    PrintInfo(infolist)

if __name__ == '__main__':
    main()


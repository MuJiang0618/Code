# -*- coding:utf-8 -*-
import re
from bs4 import BeautifulSoup
import requests

def GetPage(url):
    headers_={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"}
    r=requests.get(url,headers=headers_)
    r.encoding='utf-8'
    return r.text

def ParsePage(html,imglist):
    soup=BeautifulSoup(html,'html.parser')
    list_=soup.find_all('img',src=True)    #得到所有图片信息标签的一个列表
    for i in list_:
        imglist.append(i.get('src'))   #得到所有图片地址的一个列表，地址此时为字符串对象

def StoreImg(imglist):
    for i in range(len(imglist)):
        try:
            b=requests.get(imglist[i])
            b.encoding='utf-8'
            with open('D:\\test\\'+str(i)+'.'+imglist[i][-3:],'wb') as f:
                    f.write(b.content)
        except:
            continue

def main():
    url_='https://tieba.baidu.com/p/5182823169?pn='
    depth_=input('请输入访问页面深度:')
    depth=int(depth_)
    imglist=[]
    for n in range(depth):
        url=url_+str(n+1)
        html=GetPage(url)
        ParsePage(html,imglist)

    StoreImg(imglist)

if __name__ == '__main__':
    main()
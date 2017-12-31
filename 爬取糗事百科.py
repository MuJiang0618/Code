from lxml import etree
from urllib import request

def GetPage(url):              #获取源代码
    header={'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    page=request.Request(url,headers=header)
    org_code=request.urlopen(page).read()
    return org_code

def ParseOrg_code(org_code):    #抓取数据
    tree=etree.HTML(org_code)
    match='//a[@class="contentHerf"]/div/span/text()'  #获取段子文本，改进版本会考虑点赞数
    container=tree.xpath(match)
    return container

def download(container):       #保存数据
    with open(r'C:\Users\Administrator\Desktop\糗事百科.txt','w',) as f:
        f.writelines(container)               

def main():
    url=input('输入糗事百科网址:')   # https://www.qiushibaike.com/
    org_code=GetPage(url)
    container=ParseOrg_code(org_code)
    download(container)

if __name__ == '__main__':
    main()
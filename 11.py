from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)  
    return formataddr((Header(name,'utf-8').encode(),addr))  #formataddr函数返回一个字符串，应该是把参数转化为邮件收件人、发件人的标准形式

from_addr=input('From：')
password=input('Password:')
to_addr=input('To：')
smtp_server=input('SMTP server：')

msg=MIMEText('这里是梁康','plain','utf-8')
msg['from']=_format_addr('大木<%s>' %from_addr)
msg['to']=_format_addr('刘慧<%s>' %to_addr)   #若有多个收件人，逗号隔开再用_format_addr函数
msg['subject']=Header('来自梁康的问候','utf-8').encode()

server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
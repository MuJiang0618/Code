from email.mime.text import MIMEText
msg=MIMEText('刘慧，这里是梁康，这封邮件是我完全用一堆代码而不是通过QQ邮箱写出来发给你的（扮酷）', 'plain', 'utf-8')

from_addr=input('请输入本地地址\n')
password=input('请输入登录口令\n')   #授权码，不是邮箱登录密码
to_addr=input('请输入收件人邮箱地址\n')
smtp_server=input('SMTP server:\n')

import smtplib
server=smtplib.SMTP_SSL(smtp_server,465)  #SMTP协议默认端口是25,与收件人的SMTP服务器建立连接
server.set_debuglevel(0)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
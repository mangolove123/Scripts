#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmailAnalysis(fromaddr,toaddrList,emailTitle,html):

    type(toaddrList)

    msg = MIMEMultipart()
    msg['Subject'] = emailTitle
    msg['From'] = fromaddr
    msg['To'] = ",".join(toaddrList)

    html_part = MIMEText(html, 'html', 'utf-8')  # 实例化为html部分
    html_part.set_charset('utf-8')  # 设置编码
    msg.attach(html_part) #绑定到message里

    print('开始发送邮件给：'+str(toaddrList))
    print('请稍等...')
    try:
        s = smtplib.SMTP('smtp.qq.com',587) #登录SMTP服务器,发信
        s.starttls()
        s.login(fromaddr,'fdmjxzipitemecej')

        s.sendmail(fromaddr,toaddrList,msg.as_string())

        s.quit()
        print(s)
        print("发送成功")
    except Exception as e:
        print(e)
        print("发送失败")

    print("什么情况")

fromaddr = sys.argv[1]
toaddr = sys.argv[2]
emailTitle = sys.argv[3]
emailContent = sys.argv[4]

toaddrList = [toaddr]

print(fromaddr)
print(toaddrList)
print(emailTitle)
print(emailContent)


if __name__ == '__main__':sendEmailAnalysis(fromaddr,toaddrList,emailTitle,emailContent)




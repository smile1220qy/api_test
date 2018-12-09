
import smtplib #连接smtp服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from conf import config
#1.组装邮件正文
msg = MIMEMultipart() #混合格式
body = MIMEText("python发送的邮件",'plain','utf-8')#plain 纯文字html
msg.attach(body) #将正文添加到msg对象中
#2.组装邮件头
msg['From'] = 'test_results@sina.com'
msg["To"] = '1126894245@qq.com'
msg["Subject"] = "from python"

#4.附件
with open(config.report_path,"rb") as f:
    att_file = f.read()

att = MIMEText(att_file,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'# 声明附件的内容格式 MIME数据流格式
att["Content-Disposition"] = "attachment;filename'report.html'" #附件描述信息
msg.attach(att) #将附件添加到对象中

#3.连接smtp服务器并发送
smtp = smtplib.SMTP_SSL("smtp.163.com") #加密的方式,建立连接
smtp.login("ivan-me@163.com","hanzhichao123")#登录邮箱
smtp.sendmail("ivan-me@163.com","1126894245@qq.com",msg.as_string())#将MIME格式邮件转成字符串发送
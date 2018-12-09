
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'
#项目路径
import os
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #项目路径
#数据路径
data_path = os.path.join(project_path,'data','data.xlsx')
#用例路径
test_path = os.path.join(project_path,'testcase')
#日志路径
log_path = os.path.join(project_path,'log','log.txt')
#报告路径
report_path = os.path.join(project_path,'report','report.html')

#log配置
import logging
logging.basicConfig(level=logging.DEBUG,
                format= "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                filename=log_path,
                # filemode="a"
                )
#邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'ivan-me@163.com'
smtp_password='hanzhichao123'

receiver = '1126894245@qq.com'
subject = '接口测试报告'
body = 'hi,all,\n附件中是接口测试报告，请查收。'
is_send_email = True


if __name__ == '__main__':
    # logging.info("hello,word")
    print(data_path)




import pymysql
from jinja2 import Template
conn = pymysql.connect(host='localhost', user='root', password='14421442', database='test')
cursor = conn.cursor()
# ins = input("输入名字")
# sql = "insert into test2(name) values(%s)"
sql = "select*from test2"
cursor.execute(sql)
res = cursor.fetchall()
print(res)
cursor.close()
conn.close()

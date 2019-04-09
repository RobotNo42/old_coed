import pymysql


def get_list(sql,args):
    conn = pymysql.connect(host='47.99.237.167', user='root', password='946971', db='wzc', charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute(sql, args)
    receive = cursor.fetchall()
    cursor.close()
    conn.close()
    return receive


def get_one(sql,args):
    conn = pymysql.connect(host='47.99.237.167', user='root', password='946971', db='wzc', charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute(sql, args)
    receive = cursor.fetchone()
    cursor.close()
    conn.close()
    return receive

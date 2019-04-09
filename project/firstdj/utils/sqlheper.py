import pymysql


def get_list(sql, args):
    conn = pymysql.connect(host='localhost', user='root', password='14421442', database='new', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    receive = cursor.fetchall()
    cursor.close()
    conn.close()
    return receive


def get_one(sql, args):
    conn = pymysql.connect(host='localhost', user='root', password='14421442', database='new', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    receive = cursor.fetchone()
    cursor.close()
    conn.close()
    return receive


def modify(sql, args):
    conn = pymysql.connect(host='localhost', user='root', password='14421442', database='new', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


def creat_modify(sql, args):
    conn = pymysql.connect(host='localhost', user='root', password='14421442', database='new', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    last_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return last_id


class SqlHelper(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='14421442', database='new', charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_one(self, sql, args):
        self.cursor.execute(sql, args)
        receive = self.cursor.fetchone()
        return receive

    def get_list(self, sql, args):
        self.cursor.execute(sql, args)
        receive = self.cursor.fetchall()
        return receive

    def modify(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multiple_modify(self, sql, args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
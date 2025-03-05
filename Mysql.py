import pymysql
from pymysql import cursors

class Mysql:
    host = "localhost"
    user = "root" # Mysql用户名
    password = "2002829" # Mysql密码
    db = "demo" # 数据库名字
    port = 3306
    def __init__(self, host=host, user=user, password=password, database=db, port=port):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def update(self, sql, param=()):
        sql = sql.strip()
        count = rowid = None
        cursor = self.db.cursor()
        try:
            if sql.startswith("insert") and isinstance(param, tuple):
                count = cursor.executemany(sql, param)
            else:
                count = cursor.execute(sql, param)
            self.db.commit()
            rowid = cursor.lastrowid
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            cursor.close()
        return count, rowid

    def select(self, sql, param=(), limit=0):
        sql = sql.strip()
        result = None
        cursor = self.db.cursor()
        try:
            cursor.execute(sql, param)
            result = cursor.fetchall() if limit == 0 else cursor.fetchmany(limit)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
        return result

    def sql(self, sql, param=(), limit=0):
        sql = sql.strip()
        return self.select(sql, param, limit) if sql.startswith("select") else self.update(sql, param)

    def close(self):
        self.db.close()

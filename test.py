# 定义查询语句
from Mysql import Mysql

query = """
    SELECT u.username, COUNT(book.id) AS book_count
    FROM book
    LEFT JOIN tbl_user u ON book.uid = u.id
    GROUP BY u.username
"""

# 初始化结果存储
pie = []

# 使用封装的 Mysql 类进行数据库操作
with Mysql() as db:
    # 执行查询
    result = db.select(query)

    # 处理查询结果
    for row in result:
        pie.append({
            'value': row['book_count'],
            'name': row['username'],
        })

print(pie)

import pymysql
from pymysql import cursors


db = pymysql.connect(host='localhost', user='root', password='2002829', database='demo',
                     charset='utf8', cursorclass=pymysql.cursors.DictCursor)


cursor = db.cursor()

cursor.execute("SELECT u.username, COUNT(book.id) AS book_count FROM book LEFT JOIN tbl_user u ON book.uid = u.id GROUP BY u.username")

db.commit()

cursor.close()
db.close()

pie = []

for row in cursor.fetchall():
    pie.append({
        'value': row['book_count'],
        'name': row['username'],
    })
print(pie)

with open('饼图.html', 'r+', encoding='utf-8') as f:
    html = f.read()
    # print(html)

    # 回到行开头
    f.seek(0)
    # 删除原文
    f.truncate()

    html = html.replace("[{ value: 1048, name: 'Search Engine' }]", str(pie))

    f.write(html)
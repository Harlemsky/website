from Mysql import Mysql

pie = []

with Mysql() as db:
    # print(db.sql("SELECT u.username, COUNT(book.id) AS book_count FROM book LEFT JOIN tbl_user u ON book.uid = u.id GROUP BY u.username"))

    for row in db.sql(db.sql("SELECT u.username as username, COUNT(book.id) AS book_count FROM book LEFT JOIN tbl_user u ON book.uid = u.id GROUP BY u.username")):
        print(row['username'])
with Mysql() as db:
    for row in db.sql('select editor,avg(price) avg from book group by editor'):
        pie.append({
            'value': row['avg'],
            'name': row['editor'],
        })
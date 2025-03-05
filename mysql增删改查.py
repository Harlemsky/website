import json

from Mysql import Mysql

pie = []

with Mysql() as db:
    # print(db.sql('select * from book'))

    # db.sql('insert into book (book, price, uid, editor) values (%s, %s, %s, %s)',
    #        ['红楼梦','51',4,'清华出版社'])

    # 批量添加
    # db.sql('insert into book (book, price, uid, editor) values (%s, %s, %s, %s)',
    #     (
    #             ['三国演义', '40', 2, '川大出版社'],
    #             ['三国杀', '30', 1, '人民出版社']
    #     )
    # )

    # print(db.sql('select * from book where book in (%s, %s)',(['红楼梦', '三国杀'])))
    for row in db.sql('select editor,avg(price) avg from book group by editor'):
        pie.append({
            'value': row['avg'],
            'name': row['editor'],
        })
# print(pie)

with open('饼图.html', 'r+', encoding='utf-8') as f:
    html = f.read()
    # print(html)

    # 回到行开头
    f.seek(0)
    # 删除原文
    f.truncate()

    html = html.replace("[{ value: 1048, name: 'Search Engine' }]", str(pie))

    f.write(html)
# print(html)



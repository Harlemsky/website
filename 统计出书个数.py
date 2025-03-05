from Mysql import Mysql

x = []

y = []

with Mysql() as db:
    for row in db.sql('select editor, count(*) count from book group by editor '):
        x.append(row['editor'])
        y.append(row['count'])

# print(x)

with open('柱状图.html', 'r+', encoding='utf-8') as f:
    html = f.read()
    # print(html)

    # 回到行开头
    f.seek(0)
    # 删除原文
    f.truncate()

    html = html.replace("['Shirts', 'Cardigans', 'Chiffons', 'Pants', 'Heels', 'Socks']", str(x))
    html = html.replace("[5, 20, 36, 10, 10, 20]", str(y))

    f.write(html)
    print(html)
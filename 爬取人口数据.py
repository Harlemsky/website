import urllib.request

from pyquery import PyQuery

url = 'https://www.maigoo.com/news/480576.html'
html = urllib.request.urlopen(url).read()

pq = PyQuery(html)# print(html)

with open('人口数据网页.html', 'wb') as f:
    f.write(html)

table1 = pq('.mod_table')[0]
# print(type(table1))
i = 0
name = []
value = []
for td in pq(table1).find('td')[3:-3]:
    if i % 3 == 0:
        name.append(td.text)
    if i % 3 == 1:
        value.append(int(td.text.split('.')[0]))
    i += 1

result = [{"name": key, "value": value} for key, value in zip(name, value)]

for data in result:
    if data['name'] == '西藏':
        data['name'] = '西藏自治区'
    if data['name'] == '新疆':
        data['name'] = '新疆维吾尔自治区'
    if data['name'] == '广西':
        data['name'] = '广西壮族自治区'
    if data['name'] == '宁夏':
        data['name'] = '宁夏回族自治区'
    if data['name'] == '内蒙古':
        data['name'] = '内蒙古自治区'
    if data['name'] == '香港':
        data['name'] = '香港特别行政区'
    if data['name'] == '澳门':
        data['name'] = '澳门特别行政区'
    # 1 3 4 6 7 9 10
with open('人口地图.html', 'r', encoding='utf-8') as f:
    html = f.read()
    # print(html)

    html = html.replace("[{ name: '中西区', value: 20057.34 }]", str(result))


with open('人口地图统计.html', 'w', encoding='utf-8') as f:
    f.write(html)
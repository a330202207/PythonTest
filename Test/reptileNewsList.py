import requests
import json

url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page=1&callback=newsloadercallback&_=1528843179787'
res = requests.get(url)

jd = json.loads(res.text.lstrip(' newsloadercallback(').rstrip(');'))

for ent in jd['result']['data']:
    print(ent['url'])
# print(jd)

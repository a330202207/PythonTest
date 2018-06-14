import requests
import json
import re
import pandas
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime


# res = requests.get('http://news.sina.com.cn/c/2018-06-12/doc-ihcwpcmp6666006.shtml')
# res.encoding = 'utf-8'
# soup = BeautifulSoup(res.text, 'html.parser')
# soup.select('.main-title')[0].text
#
# timesource = soup.select('.date')[0].text
#
# # dt = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
# # dt.strftime('%Y-%m-%d')
#
# fromsource = soup.select('.source')[0].text
#
# article = []
# for p in soup.select('#article p')[:-1]:
#     article.append(p.text.strip())
#
# ' '.join([p.text.strip() for p in soup.select('#article p')[:-1]])
# editor = soup.select('.show_author')[0].text.lstrip('责任编辑：')
# num = soup.select('.tool-cmt .num')
# print(editor,num)

commentUrl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-{}&\
                   group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&\
                   thread=1'

def getNewsDetail(newsUrl):
    result = {}
    res = requests.get(newsUrl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # 标题
    result['title'] = soup.select('.main-title')[0].text
    # 来源
    result['newssource'] = soup.select('.source')[0].text

    # 时间
    result['dt'] = soup.select('.date')[0].text

    # 文章
    result['article'] = ' '.join([p.text.strip() for p in soup.select('#article p')[:-1]])

    # 编辑者
    result['editor'] = soup.select('.show_author')[0].text.lstrip('责任编辑：')

    # 评论
    result['comments'] = getCommentCounts(newsUrl)
    return result

def getCommentCounts(newsurl):
    m = re.search('doc-i(.+).shtml', newsurl)
    newsid = m.group(1)
    coumments = requests.get(commentUrl.format(newsid))

    jd = json.loads(coumments.text)
    return jd['result']['count']['total']

def parseListLinks(url):
    newsdetails = []
    res = requests.get(url)
    jd = json.loads(res.text.lstrip(' newsloadercallback(').rstrip(');'))
    for ent in jd['result']['data']:
        newsdetails.append(getNewsDetail(ent['url']))
    return newsdetails

# res = getNewsDetail('http://news.sina.com.cn/c/2018-06-12/doc-ihcwpcmp6666006.shtml')
# print(res)
url = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}'
news_toal = []
for i in range(1, 3):
    newsurl = url.format(i)
    newsary = parseListLinks(newsurl)
    news_toal.extend(newsary)
res = parseListLinks(url)

df = pandas.DataFrame(news_toal)
# with sqlite3.connect('news.sqlite') as db:
#     df.to_sql('news', con = db)

# with sqlite3.connect('news.sqlite') as db:
#     df2 = pandas.read_sql_query('SELECT * FROM news', con = db)
df.to_excel('news.xlsx')
# print(news_toal)
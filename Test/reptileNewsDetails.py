import requests
import json
import re
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
    # result['comments'] = getCommentCounts(newsUrl)
    return result

res = getNewsDetail('http://news.sina.com.cn/c/2018-06-12/doc-ihcwpcmp6666006.shtml')
print(res)
# def getCommentCounts(newsurl):
#     m = re.search('doc-i(.+).shtml', newsurl)
#     newsid = m.group(1)
#     coumments = requests.get(commentUrl.format(newsid))
#
#     jd = json.loads(coumments.text)
#     return jd['result']['count']['total']

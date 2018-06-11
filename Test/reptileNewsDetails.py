import requests
from bs4 import BeautifulSoup
from datetime import datetime

res = requests.get('http://news.sina.com.cn/c/nd/2018-06-12/doc-ihcufqih3563019.shtml')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
soup.select('.main-title')[0].text

timesource = soup.select('.date')[0].text

# dt = datetime.strptime(timesource, '%Y年%m月%d日 %H:%M')
# dt.strftime('%Y-%m-%d')

fromsource = soup.select('.source')[0].text

article = []
for p in soup.select('#article p')[:-1]:
    article.append(p.text.strip())

' '.join([p.text.strip() for p in soup.select('#article p')[:-1]])
editor = soup.select('.show_author')[0].text.lstrip('责任编辑：')
print(editor)
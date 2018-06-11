import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/c/2018-04-12/doc-ifyuwqez9837475.shtml')
res.encoding = 'utf-8'
print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
soup.select('.second-title')[0].text
# for news in soup.select('.news-item'):
#     print(news)
#jupyter notebook
#from datetime import datetime
#datetime.strptime(timesource, '%Y年%m月%d日%H:%M')
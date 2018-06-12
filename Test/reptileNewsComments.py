import requests
import json
import re
# commtens = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-hcwpcmp6666006&\
#                    group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&\
#                    thread=1&callback=jsonp_1528810148193&_=1528810148193')
#
# jd = json.loads(commtens.text.strip('jsonp_1528810148193()'))
# jd['result']['count']['total']
#
#

# m = re.search('doc-i(.+).shtml',newsurl)
# newsid = m.group(1)

commentUrl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn' \
             '&newsid=comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1' \
             '&page_size=3&t_size=3&h_size=3&thread=1'

def getCommentCount(newsurl):
    m = re.search('doc-i(.+).shtml',newsurl)
    newsid = m.group(1)
    coumments = requests.get(commentUrl.format(newsid))

    jd = json.loads(coumments.text)
    return jd['result']['count']['total']

newsurl = 'http://news.sina.com.cn/c/2018-06-12/doc-ihcwpcmp6666006.shtml'
num = getCommentCount(newsurl)
print(num)

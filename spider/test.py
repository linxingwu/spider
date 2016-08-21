# coding:utf-8
# import urllib2
#
# from bs4 import BeautifulSoup
#
# response = urllib2.urlopen("https://www.zhihu.com/topic/19730619/top-answers")
# html_doc = response.read().decode("utf-8")
# soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
# node = soup.find("span", class_="copy")
# print node.get_text()

url = "https://www.zhihu.com/question/32040945/answer/70111320"
print '爬取 %d\t:%s' % (1, url)
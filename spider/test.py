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
import re

url = "https://pic2.zhimg.com/c76c897ab037fc0b04c7fa620b165d11_b.jpg"
pattern = re.compile(r'/\w+_b\.jpg')
list = pattern.findall(url)
print type(list[0])

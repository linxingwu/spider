# coding:utf-8
'''
话题列表 <div class="zm-topic-list-container">
答案概要 <div class="feed-item feed-item-hook folding"> <div class="zh-summary summary clearfix"> <a href="/question/46053358/answer/100268713" class="toggle-expand">显示全部</a>
'''
import re
import urllib

from bs4 import BeautifulSoup

class Parser(object):
    def parse(self, new_url, html_doc):
        if new_url is None or html_doc is None:
            return None
        # print html_doc
        soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
        urls = self.getNew_Urls(new_url, soup)
        data = self.getData(new_url, soup)
        self.downloadImg(soup)
        return urls, data

    def getNew_Urls(self, new_url, soup):
        # /question/32040945/answer/56021269
        urls_set = set()
        links = soup.find_all("link", href=re.compile(r"/question/\d+/answer/\d+"))
        for link in links:
            new_urls = "https://www.zhihu.com" + link['href']
            urls_set.add(new_urls)
        return urls_set

    def getData(self, new_url, soup):
        data = {}
        data["url"] = new_url
        # <a class="author-link" data-hovercard="p$b$osborne" target="_blank" href="/people/osborne">Osborne</a>
        data_author = soup.find("a", class_="author-link").get_text()
        data["author"] = data_author
        # class="zm-editable-content clearfix"
        answer = soup.find("div", class_="zm-editable-content clearfix")
        if answer is None:
            answer = soup.find("div", class_="zm-editable-content clearfix")
        data_answer = answer.get_text()
        data["answer"] = data_answer
        question = soup.find("a", href=re.compile(r'/question/\d+')).get_text()
        data["question"] = question
        return data

    def parseurl_list(self, html_doc):
        linklist = []
        soup = BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")
        links = soup.find_all('a', class_="toggle-expand", text="显示全部")
        if links is not None and len(links) > 0:
            for link in links:
                link = "https://www.zhihu.com" + link["href"]
                linklist.append(link)
        return linklist

    def downloadImg(self, soup):
        # origin_image zh-lightbox-thumb lazy
        imgs = soup.find_all("img", class_="origin_image zh-lightbox-thumb lazy")
        count = 1
        for img in imgs:
            urllib.urlretrieve(img["data-original"], "E:/zhihu/spider/"+str(count)+".jpg")
            count += 1


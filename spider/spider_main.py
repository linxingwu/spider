# coding:utf-8
import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.UrlDownloader()
        self.parser = html_parser.Parser()
        self.outputer = html_outputer.Outputer()

    def craw(self, url):
        # 首先根据话题链接，将话题下的精华回答链接保存
        html_doc = self.downloader.download(url)
        urllist = self.parser.parseurl_list(html_doc)
        if urllist is not None and len(urllist) > 0:
            self.urls.add_new_urls(urllist)
        # self.urls.add_new_url(url)
        count = 1
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            try:
                html_doc = self.downloader.download(new_url)
                print u'爬取 %d\t:%s' % (count, new_url)
                new_urls, data = self.parser.parse(new_url, html_doc)
                self.outputer.add_data(data)
                count += 1
                # if len(new_urls) > 0:
                #     self.urls.add_new_urls(new_urls)
                if count > 10:
                    break
            except Exception as e:
                print count
                print e
                print 'craw failed:%s' % new_url
        self.outputer.output_result()


if __name__ == "__main__":
    obj_spider = SpiderMain()
    # 知乎话题：生活
    url = """
    https://www.zhihu.com/topic/19551147/top-answers
    """
    obj_spider.craw(url)

# coding:utf-8
class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        return len(self.new_urls) != 0

    def add_new_url(self, url):
        if url is None or url is None:
            return
        self.new_urls.add(url)

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def add_new_urls(self, new_urls):
        if new_urls is not None and len(new_urls) > 0:
            for url in new_urls:
                self.add_new_url(url)
# coding:utf-8
import cookielib
import urllib2


class UrlDownloader(object):
    def __init__(self):
        pass

    def download(self, new_url):
        try:
            cj = cookielib.CookieJar()
            handler = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(handler)
            urllib2.install_opener(opener)
            requset = urllib2.Request(new_url)
            requset.add_header("User-Agent",
                               """
                               Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
                               """)
            # requset.add_data("account", "1045779714@qq.com")
            # requset.add_data("password", "LOVE0307")
            response = urllib2.urlopen(requset)
            if response.getcode() != 200:
                return
            return response.read().decode("utf-8")
        except Exception as e:
            print e
            raise Exception("craw faild:%s" % new_url)

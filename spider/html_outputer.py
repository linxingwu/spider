# coding:utf-8
class Outputer(object):
    def __init__(self):
        self.data = list()

    def add_data(self, data):
        if data is not None:
            self.data.append(data)

    def output_result(self):
        for d in self.data:
            print d["url"], d["question"], d["author"], d["answer"]
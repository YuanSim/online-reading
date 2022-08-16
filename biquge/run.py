# encoding=utf-8
import biquge_handler
import keyboard
import properties_handler

class Run(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.properties = properties_handler.Properties(fileName)
        self.bqg = biquge_handler.Biquge_handler()

    def read_next(self):
        dictProperties = self.properties.getProperties()
        str_all = dictProperties['biquge']
        url = str_all['nowurl']
        nexturl = self.bqg.get_next_url(url)
        print(nexturl)
        old_str = 'biquge.nowurl'
        self.properties.update_perties(old_str, nexturl)

    def read_index(self, baseurl):
        n = int(input('请输入要跳往的章节：'))
        indexurl = self.bqg.get_chapter_num(baseurl, n)
        # print(indexurl)
        old_str = 'biquge.nowurl'
        self.properties.update_perties(old_str, indexurl)


if __name__ == '__main__':
    fileName = "application-biquge.properties"
    properties = properties_handler.Properties(fileName)
    dictProperties = properties.getProperties()
    str_all = dictProperties['biquge']
    baseurl = str_all['baseurl']
    # print(baseurl)
    bqg = biquge_handler.Biquge_handler()
    url = str_all['nowurl']
    # print(url)
    bqg.get_next_url(url)
    # print(url)
    run = Run(fileName)

    keyboard.add_hotkey('right', run.read_next)
    keyboard.add_hotkey('ctrl', run.read_index, args=(baseurl,))
    keyboard.wait('esc')
    print('已退出')

    # while True:
    #     bqg.split_txt(url)
    #     n = 1
    #     if not m:
    #         n = input('请选择章节:')
    #         url = bqg.get_chapter_num(baseurl, int(n))
    #     else:
    #         url = bqg.get_next_url(url)
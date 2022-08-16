# encoding=utf-8
# 导包,发起请求使用urllib库的request请求模块
import keyboard
import requests


class Biquge_handler():
    # def __init__(self, txt_url):
    #     self.txt_url = txt_url

    # 读取html内容
    def read_html(self, txt_url):
        """
        根据网址返回html内容
        :param txt_url: 网址
        :return: html内容
        """
        res = requests.get(txt_url)
        txt = res.text
        # print(txt)
        # txt = txt.encode('utf-8')
        txt = txt.encode('ISO-8859-1').decode('utf-8')
        # print(txt)
        return txt

    # 输出小说章节内容
    def split_txt(self, txt_url):
        txt = self.read_html(txt_url)
        j = '&nbsp;&nbsp;&nbsp;&nbsp;'
        t = txt.split(j)
        # print(len(t))
        # print(t)
        it = '<br/><br/>'
        for l in t:
            # print(l)
            if it in l:
                print(l.split(it)[0])

    # 获取固定章节地址
    def get_chapter_num(self, base_url, num):
        global i
        txt = self.read_html(base_url)
        # print(txt)
        h = '<dd><a href="'
        chapternum = txt.split(h)
        del chapternum[0]
        for l in range(len(chapternum)):
            # print(chapternum[l])
            i = '.html'
            if i in chapternum[l]:
                chapternum[l] = chapternum[l].split(i)[0]
        if 0 < num < len(chapternum):
            url = base_url + chapternum[num] + i
            self.split_txt(url)
            return url
        else:
            return False

    # 获取下一章网址
    def get_next_url(self, txt_url):
        txt_url = self.read_html(txt_url)
        # print(txt)
        h = '章节列表'
        j = '">下一章'
        k = 'href="'
        if h in txt_url:
            txt_url = txt_url.split(h)[1]
        else:
            return False
        # print(url)
        if j in txt_url:
            txt_url = txt_url.split(j)[0]
        else:
            return False
        # print(url)
        if k in txt_url:
            txt_url = txt_url.split(k)[1]
        else:
            return False
        # print(url)
        self.split_txt(txt_url)
        return txt_url


if __name__ == '__main__':
    # 书香小说网
    # url = 'https://www.xbiquge.la/'
    # 笔趣阁
    # url = 'https://www.xbiquwx.la/'
    # 书趣阁
    # url = 'https://www.shuquge.com/'
    # url = 'https://www.xbiquge.la/'
    baseurl = 'https://www.xbiquwx.la/'
    txtnum = '112_112946'  # 万界竞技，开局我选张三丰
    # txtnum = input('请输入小说代码:')
    baseurl = baseurl + txtnum + '/'
    # print(baseurl)
    # print(chapternum)
    n = 190
    # n = input('请选择章节:')
    bqg = Biquge_handler()
    url = bqg.get_chapter_num(baseurl, int(n))
    # bqg.split_txt(url)
    print(url)

    # url = bqg.get_next_url(url)
    keyboard.add_hotkey('right', bqg.get_next_url, args=(url,))
    keyboard.add_hotkey('ctrl', bqg.get_chapter_num, args=(baseurl, int(input('请选择章节:'))))
    keyboard.wait()
    # print(url)
    # while True:
    #     bqg.split_txt(url)
    #     n = input('请选择章节:')
    #     if n == '':
    #         url = bqg.get_next_url(url)
    #     else:
    #         url = bqg.get_chapter_num(baseurl, int(n))
    #     if not url:
    #         print('输入章节有误')
    #         break
    #     if n == 'e':
    #         print('退出')
    #         break

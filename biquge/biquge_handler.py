# encoding=utf-8
# 导包,发起请求使用urllib库的request请求模块
# import keyboard
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
        headers = {
            'Host': 'www.xbiquwx.la',
            'Connection': 'keep - alive',
            'Cache - Control': 'max - age = 0',
            'Accept - Encoding': 'gzip, deflate, br',
            'Accept - Language': 'zh - CN, zh;'
        }
        res = requests.get(txt_url, headers)
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
        print(t)
        it = '<br/><br/>'
        t1 = '<title>'
        # t2 = '</title>'
        for l in t:
            # print(l)
            if t1 in l:
                print(l.split(t1)[1].split('_')[0])
            if it in l:
                lin = l.split(it)[0]
                length = len(lin)
                # print(length)
                n = int(length/30)+1
                # print(n)
                for i in range(n):
                    # print(i)
                    if i+1 == n:
                        print(lin[i * 30:len(lin)])
                    else:
                        print(lin[i * 30:(i+1)*30])

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
    bqg = Biquge_handler()
    bqg.split_txt('https://www.xbiquwx.la/112_112946/28207415.html')

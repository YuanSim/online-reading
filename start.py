
#导包,发起请求使用urllib库的request请求模块
# from io import BytesIO
# import urllib.request
# import gzip
import requests

# 读取html内容
def readhtml(url):
    res = requests.get(url)
    txt = res.text
    txt = txt.encode('ISO-8859-1').decode('utf-8')
    # print(txt)
    return txt

# 输出小说章节内容
def splittxt(url):
    txt = readhtml(url)
    j = '&nbsp;&nbsp;&nbsp;&nbsp;'
    t = txt.split(j)
    # print(len(t))
    # print(t)
    i = '<br/><br/>'
    for l in t:
        # print(l)
        if i in l:
            print(l.split(i)[0])


# 获取固定章节地址
def getchapternum(baseurl, n):
    txt = readhtml(baseurl)
    # print(txt)
    h = '<dd><a href="'
    chapternum = txt.split(h)
    del chapternum[0]
    for l in range(len(chapternum)):
        # print(chapternum[l])
        i = '.html'
        if i in chapternum[l]:
            chapternum[l] = chapternum[l].split(i)[0]
    if n > 0 and n < len(chapternum):
        return baseurl + chapternum[n] + i
    else:
        return False

# 获取下一章网址
def getnexturl(url):
    url = readhtml(url)
    # print(txt)
    h = '章节列表'
    j = '">下一章'
    k = 'href="'
    if h in url:
        url = url.split(h)[1]
    else:
        return False
    # print(url)
    if j in url:
        url = url.split(j)[0]
    else:
        return False
    # print(url)
    if k in url:
        url = url.split(k)[1]
    else:
        return False
    # print(url)
    return url

if __name__ == '__main__':
    # 书香小说网
    # url = 'https://www.xbiquge.la/'
    # 笔趣阁
    # url = 'https://www.xbiquwx.la/'
    # 书趣阁
    # url = 'https://www.shuquge.com/'
    # url = 'https://www.xbiquge.la/'
    baseurl = 'https://www.xbiquwx.la/'
    txtnum = '112_112946'     # 万界竞技，开局我选张三丰
    # txtnum = input('请输入小说代码:')
    baseurl = baseurl + txtnum + '/'
    # print(baseurl)
    # print(chapternum)
    i = 1
    n = 184
    # n = input('请选择章节:')
    url = getchapternum(baseurl, int(n))
    while i == 1:
        splittxt(url)
        n = input('请选择章节:')
        if n == '':
            url = getnexturl(url)
        else:
            url = getchapternum(baseurl, int(n))
        if url == False:
            print('输入章节有误')
            break
        if n == 'e':
            print('退出')
            break
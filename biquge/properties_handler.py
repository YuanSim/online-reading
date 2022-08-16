# encoding=utf-8


"""
脚本名称：properties_handler.py
脚本功能：解析.properties配置文件
编写人：  pangtaishi
编写日期：2021-02-28
"""


class Properties(object):
    def __init__(self, fileName):
        self.fileName = fileName
        self.properties = {}

    def __getDict(self, strName, dictName, value):
        if (strName.find('.') > 0):
            k = strName.split('.')[0]
            dictName.setdefault(k, {})
            return self.__getDict(strName[len(k) + 1:], dictName[k], value)
        else:
            dictName[strName] = value
            return

    # 获取配置文件元素
    def getProperties(self):
        try:
            pro_file = open(self.fileName, 'Ur')
            for line in pro_file.readlines():
                line = line.strip().replace('\n', '')
                if line.find("#") != -1:
                    line = line[0:line.find('#')]
                if line.find('=') > 0:
                    strs = line.split('=')
                    strs[1] = line[len(strs[0]) + 1:]
                    self.__getDict(strs[0].strip(), self.properties, strs[1].strip())
        # except Exception, e:
        except Exception:
            #   raise e
            print('获取元素异常！')
        else:
            pro_file.close()
        return self.properties


    def update_perties(self, old_str, url):
        new_str = old_str + "=" + url
        f1 = open(self.fileName, 'r')
        lines = f1.readlines()
        f1.close()
        f1 = open(self.fileName, 'w')
        for lin in lines:
            if old_str in lin:
                lin = new_str
            f1.write(lin)
        f1.close()

if __name__ == '__main__':
    # 读取配置文件
    fileName = "config-biquge.properties"
    # fileName = "application-biquge.properties"
    old_str = 'biquge.nowurl'
    url = 'https://www.xbiquwx.la/112_112946/205.html'
    new_str = old_str + "=" + url
    properties = Properties(fileName)

    properties.update_perties(old_str, url)
    dictProperties = properties.getProperties()
    str_all = dictProperties['biquge']
    name = str_all['baseurl']
    ip = str_all['novelnum']
    port = str_all['chapternum']
    username = str_all['nowurl']

    print(str_all)
    print(name)
    print(ip)
    print(port)
    print(username)

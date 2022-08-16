# online-reading
在线阅读，阅读插件，摸鱼

### 基础介绍
- python 版本3.6.8

### 目录介绍
- biquge 笔趣阁
  - [笔趣阁配置文件](biquge/application-biquge.properties)
  - [笔趣阁小说内容处理脚本](biquge/biquge_handler.py)
  - [存档和读取配置文件脚本](biquge/properties_handler.py)
  - [笔趣阁在线阅读启动文件](biquge/run.py)


# v1.0 
    - step1
        + 手动输入小说地址
    - step2
        + 输入空格键切换下一章

# v2.0
    - step1
        + 配置文件配置对应小说和章节地址
    - step2
        + 运行后，点击右键输出下一章
        + 点击ctrl键，输入章节数，点击enter，输出对应章节内容
        + 点击esc键退出
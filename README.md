这是一个解析OFD文件的工具，OFD（国家版式文档格式）使用的标准是	GB/T 33190-2016，Wiki百科的定义如下所示https://zh.wikipedia.org/wiki/%E5%9B%BD%E5%AE%B6%E7%89%88%E5%BC%8F%E6%96%87%E6%A1%A3%E6%A0%BC%E5%BC%8F
GB/T 33190-2016 本人是从CSDN上面下载的，暂时不附在文件中
ofd_class.py 用于存放ofd的各种格式类型
ofd_parse.py 用于分析ofd文件
ofd_main.py 和 ofd_window 是一个简易的界面用来打开ofd文件

目前处于初步开发阶段，主要用到的开发库是lxml，所用的ofd文件通过 永中进行文档转换为ofd http://www.yozodcs.com/page/example.html

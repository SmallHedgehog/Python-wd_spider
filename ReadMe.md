## Python2.7爬取网贷网上的数据

### 获取数据时，是通过寻找API接口来获取数据的

数据平台地址：http://shuju.wdzj.com/

main.py 模块是程序的入口函数，支持命令行参数，使用方式：Python main.py <选项>，选项支持：
- -h, --help	show this help message and exit
- -d D			import data into database, default "data.sqlite"
- -f F			write data into file, default "data.txt"

dist/main.exe是可执行程序，运行时会在当前目录下生成data.sqlite和data.txt文件来存储我们爬取下来的数据。
db.py 是配置sqlite3数据库模块
log.py	是出错处理模块，如果requests请求失败，会在当前目录下生成log.txt文件来记录出错信息。
main.py 是程序入口函数，支持命令行参数
parsing.py 是构造requests请求和解析数据模块
writing.py 是将数据写入到文件中
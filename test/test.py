from flask import Flask, current_app

app = Flask(__name__)
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequsetContext

# ctx = app.app_context()
# ctx.push()
# a = current_app
#
# d = current_app.config['DEBUG']
# ctx.pop()

with app.app_context():  ##上下文表达式
    a = current_app
    d = current_app.config['DEBUG']

# # 文件读写：
# try:
#     f = open(r'D:\t.txt')
#     print(f.read())
# finally:
#     f.close()
#
# with open(r'') as f:
#     print(f.read())
#
#
#
#
# 1.连接数据库
# 2.sql
# 3.释放资源

# 实现了上下文协议的对象使用with
# 上下文管理器
# __enter__ __exit__
# 上下文表达式必须要返回一个上下文管理器
# with

class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self,exc_type, exc_value, tb):
        if tb:
            print('process exception') ## 处理异常
        else：
            print('no exception') ##不处理
        print('close resource connection')
        return True or False## 返回True代表在__exit__里已经处理了异常，请python在外部不要再抛出异常
                            ## 返回False，会在内部的异常再抛出到外部，让excep捕捉到异常
                            ## 如果没有返回值，会返回None，其实也是False，还是会抛异常到外部

    def query(self):
        print('query data')

try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass
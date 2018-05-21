# 原理 字典 保存数据
# 操作数据
# werkzeug local local 字典
# Localstack Local 字典
# Local使用字典的方式实现的线程隔离
# 线程隔离的栈结构
# 封装 如果一次封装解决不了问题，那么就再来一次


import threading
import time

from werkzeug.local import Local

my_obj = Local() ##线程隔离对象

my_obj.b = 1

def worker():
    my_obj.b = 2
    print('in new thread b is :' + str(my_obj.b))

new_t = threading.Thread(target=worker, name='fuck you')
new_t.start()

time.sleep(1)

print("in main thread b is :" + str(my_obj.b))


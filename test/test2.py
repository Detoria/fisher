import threading
import time


def worker():
    print('hello')
    t = threading.current_thread()
    time.sleep(5)
    print(t.getName())

new_t = threading.Thread(target=worker, name='fuck') ## name 定义线程名字
new_t.start()

## 如果直接使用 work() 注释掉11 12行，会卡在time.sleep 因为是单线程执行，并不是多线程

# 多线程编程更加充分的利用CPU的资源性能优势
# 异步编程

t = threading.current_thread()

print(t.getName())


from werkzeug.local import LocalStack
import threading
import time


my_stack = LocalStack()
my_stack.push(1)

print('main thread after push, value is :' + str(my_stack.top))

def worker():
    print('new thread before push, value is :' + str(my_stack.top))
    my_stack.push(2)
    print('new thread after push, value is :' + str(my_stack.top))

new_t = threading.Thread(target=worker, name='fuck you')
new_t.start()
time.sleep(1)

print('main thread now value is :' + str(my_stack.top))
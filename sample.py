import threading
from threading import Thread


# create a subclass of Thread
class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    # override run()
    def run(self):
        for i in range(1, 6):
            print(i, threading.currentThread().getName())


print('Welcome')
print(threading.currentThread().getName())
# create first child thread => born state
t1 = MyThread()
# change the name of t1 thread
t1.setName('First')
# change t1's born state to ready state
t1.start()
# create second thread
t2 = MyThread()
# change t2's name
t2.setName('Second')
# change t2's born state into ready state
t2.start()

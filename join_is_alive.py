from threading import Thread
import threading
import time


class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(1, 6):
            print(str(i)+':'+threading.currentThread().getName())
            time.sleep(0.5)


if __name__ == '__main__':
    print('Welcome from '+threading.currentThread().getName())
    # create first child thread
    t1 = MyThread()
    # change t1's state to ready state
    t1.start()
    print('*status of t1?', t1.is_alive())
    t1.join() # calling thread - main thread ll be blocked until t1 is finished
    print('status of t1?', t1.is_alive())
    for i in range(11, 16):
        print(str(i)+':'+threading.currentThread().getName())

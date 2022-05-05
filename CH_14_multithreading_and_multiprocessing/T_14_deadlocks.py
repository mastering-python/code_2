import time
import threading


a = threading.Lock()
b = threading.Lock()


def thread_0():
    print('thread 0 locking a')
    with a:
        time.sleep(0.1)
        print('thread 0 locking b')
        with b:
            print('thread 0 everything locked')


def thread_1():
    print('thread 1 locking b')
    with b:
        time.sleep(0.1)
        print('thread 1 locking a')
        with a:
            print('thread 1 everything locked')


threading.Thread(target=thread_0).start()
threading.Thread(target=thread_1).start()

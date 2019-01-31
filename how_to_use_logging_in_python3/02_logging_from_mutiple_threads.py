#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/31 13:49
import logging
import threading
import time


def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info, ))
    thread.start()
    try:
        logging.debug('Hi from main')
        time.sleep(0.75)
    except KeyboardInterrupt:
        info['stop'] = True
    thread.join()


if __name__ == "__main__":
    main()

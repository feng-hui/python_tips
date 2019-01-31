#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/31 14:48
import logging.config
import time
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

# logging.config.fileConfig('logging.conf')

t = logging.config.listen(9999)
t.start()

logger = logging.getLogger('simpleExample')

try:
    while True:
        logging.debug('debug message')
        logging.info('info message')
        logging.error('error message')
        logging.warning('warning message')
        logging.critical('critical message')
        time.sleep(5)
except KeyboardInterrupt:
    logging.config.stopListening()
    t.join()

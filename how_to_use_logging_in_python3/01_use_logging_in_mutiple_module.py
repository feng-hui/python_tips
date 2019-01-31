#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/31 16:13
import logging
from how_to_use_logging_in_python3.auxiliary_module.auxiliary import Auxiliary, some_function
logger = logging.getLogger('spam_application')
logger.setLevel('DEBUG')

fh = logging.FileHandler('spam.log')
fh.setLevel('DEBUG')

ch = logging.StreamHandler()
ch.setLevel('ERROR')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info('creating an instance of auxiliary_module.Auxiliary')
a = Auxiliary()
logger.info('created an instance of auxiliary_module.Auxiliary')
logger.info('calling auxiliary_module.Auxiliary.do_something')
a.do_something()
logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
some_function()
logger.info('done with auxiliary_module.some_function()')
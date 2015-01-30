#!/usr/bin/env python
# -*-coding: utf-8 -*-
__author__ = 'livvy'

import logging
import logging.config
import os
import os.path
import datetime

LOGDIR = os.path.join("",'log')
LOGFILE = datetime.datetime.now().strftime('%Y-%m-%d')+'.log'
logging.basicConfig(level=logging.DEBUG,
                    format='',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename = os.path.join(LOGDIR,LOGFILE),
                    filemode='a'
                    )
logging.config.fileConfig("logging.ini")

fileLog = logging.FileHandler(os.path.join(LOGDIR,LOGFILE),'a+')
formatter = logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s')
fileLog.setFormatter(formatter)

logging.getLogger('site').addHandler(fileLog)
logging.getLogger('site').setLevel(logging.DEBUG)
# -*- coding: utf-8 -*-
'''
Created on 2016-10-20

@author: hustcc
'''

# for sqlite
#DATABASE_URI = 'sqlite:///git_webhook.db'
# for mysql
DATABASE_URI = 'mysql+pymysql://username:password@localhost/webhook'

CELERY_BROKER_URL = 'redis://:@127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://:@127.0.0.1:6379/0'

SOCKET_MESSAGE_QUEUE = 'redis://:@127.0.0.1:6379/0'

GITHUB_CLIENT_ID = 'b6e751cc48d664240467'
GITHUB_CLIENT_SECRET = '6a9e0cbeee1bf89a1e1a25958f35b9dc6b36c996'

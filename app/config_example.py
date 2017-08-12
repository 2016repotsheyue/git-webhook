# -*- coding: utf-8 -*-
'''
Created on 2016-10-20

@author: hustcc
'''

# for sqlite
#DATABASE_URI = 'sqlite:///git_webhook.db'
# for mysql
DATABASE_URI = 'mysql+pymysql://root:TK.xiaohang16@120.26.55.227/webhook'

CELERY_BROKER_URL = 'redis://:rbai@127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://:rbai@127.0.0.1:6379/0'

SOCKET_MESSAGE_QUEUE = 'redis://:rbai@127.0.0.1:6379/0'

GITHUB_CLIENT_ID = 'b6e751cc48d664240467'
GITHUB_CLIENT_SECRET = '6a9e0cbeee1bf89a1e1a25958f35b9dc6b36c996'

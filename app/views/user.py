# -*- coding: utf-8 -*-
'''
Created on 2017-8-13

@author: rbai
'''
from app import app, v
from app.utils import ResponseUtil, RequestUtil, SshUtil
from app.database.model import User

@app.route('/api/reginster', methods=['POST'])
def reginster():
    username = request.json.get('úsername')
    password = request.json.get('password')
    user = User(username = username)
    user.hash_password(password)
    user.save()
    return ResponseUtil.standard_response(1, user.dict(with_pkey=True))
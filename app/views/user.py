# -*- coding: utf-8 -*-
'''
Created on 2017-8-13

@author: rbai
'''
from app import app, v
from app.utils import ResponseUtil, RequestUtil, SshUtil, DateUtil
from app.database.model import User

@app.route('/api/register', methods=['POST'])
@v.param({
    'username': v.str(),
    'password': v.str(),
    'email': v.str()
})
def register(username, password, email):
    # username = request.json.get('úsername')
    # password = request.json.get('password')
    # email = request.json.get('email')
    if User.query.filter_by(username = username).first() is not None:
        return ResponseUtil.standard_response(0, 'user is exist')
    user = User(username= username, email= email)
    user.hash_password(password)
    user.save()
    return ResponseUtil.standard_response(1, user.dict())


@app.route('/api/login', methods=['POST'])
@v.param({
    'username': v.str(),
    'password': v.str()
})
def loginApi(username, password):
    user = User.query.filter_by(username= username).first()
    if not user or not user.verify_password(password):
        return ResponseUtil.standard_response(0, '用户名不存在或密码错误')
    user.last_login = DateUtil.now_datetime()
    user.save()
    RequestUtil.login_user(user.dict())
    return ResponseUtil.standard_response(1, user.dict())
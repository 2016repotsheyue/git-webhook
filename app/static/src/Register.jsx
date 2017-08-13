import React from 'react';

import OnFireMixin from './mixins/onFireMixin.jsx';
import TipShowMixin from './mixins/tipShowMixin.jsx';
import RequestsMixin from './mixins/xhrRequestsMixin.jsx';

const Register = React.createClass({
    __ONFIRE__: 'Reginster',
    mixins: [RequestsMixin, OnFireMixin, TipShowMixin],  // 引入 mixin    
    getInitialState: function(){
        return {
            username: '',
            password: '',
            email: '',
            registerBtn: '注册'
        }
    },
    render: function(){
        const {registerBtn, username, password, loading, email} = this.state;
        const loadingClass = loading ? 'loading' : '';
        return(
            <div className="user-register">
                <div className="ui medium header">用户注册</div>
                <form className="ui form">
                    <div className="field">
                        <label>用户名</label>
                        <input type="text" name="username" value={username} onChange={e=>{this.setState({username: e.target.value})}} placeholder="请输入用户名" />
                    </div>
                    <div className="field">
                        <label>密码</label>
                        <input type="password" name="password" value={password} onChange={e=>{this.setState({password: e.target.value})}} placeholder="请输入密码" />
                    </div>
                    <div className="field">
                        <label>email</label>
                        <input type="text" name="email" value={email} onChange={e=>{this.setState({email: e.target.value})}} placeholder="请输入邮箱" />
                    </div>
                    <button className={`ui primary button ${loadingClass}`} type="button" onClick={this.onClick.bind(this)}>{registerBtn}</button>
                </form>
            </div>
        );
    },

    onClick: function(){
        const {username, password, loading, email} = this.state;
        if(loading) return;
        this.setState({loading: true});
        this.post('/api/register', {
            username,
            password,
            email
        }, function(r){
            this.setState({loading: false})
            r = r.json();
            if(r.success === 1){
                this.showSuccess('注册成功')
            }else{
                this.showError(r.data)
            }
        }.bind(this));
        console.log(username, password)
    }
});

export default Register;
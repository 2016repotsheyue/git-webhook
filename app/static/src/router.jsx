import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, hashHistory } from 'react-router';

import MainComponent from './common/main.jsx';

import WebHook from './webHook.jsx';
import Server from './server.jsx';
import Collaborator from './collaborator.jsx';
import HistoryList from './historyList.jsx';
import Document from './document.jsx';
import Login from './Login.jsx';
import Register from './Register.jsx';


ReactDOM.render((
  <Router history={hashHistory}>
    <Route path="/" component={MainComponent}>
      <Route path="/loginusername" component={Login} />
      <Route path="/webhook" component={WebHook} />
      <Route path="/register" component={Register} />
      <Route path="/server" component={Server} />
      // collaborator
      <Route path="/collaborator/:webhook_id" component={Collaborator} />
      // hostroy
      <Route path="/history/:webhook_id" component={HistoryList} />
      <Route path="/history/:webhook_id/:page" component={HistoryList} />
      // doc
      <Route path="/doc" component={Document} />
      <Route path="/doc/:subject" component={Document} />
    </Route>
  </Router>),
  document.querySelector('#wrapper')
);
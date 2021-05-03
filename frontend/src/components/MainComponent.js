import React, { Component } from 'react';
import {Switch, Route, Redirect} from "react-router-dom";
import Navigator from './NavComponent';


function Main(props) {
  return (
    <div>
      <Navigator />
      <Switch>
          
        <Route path='/subject/:subId' />
        <Route path='/'
      </Switch>
    </div>
  )
}

export default Main;

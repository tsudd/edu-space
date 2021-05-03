import React, { Component } from 'react';
import { BrowserRouter } from "react-router-dom";
import AccountsList from './components/AccountsListComponent';
import Main from './components/MainComponent'

class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <div className="app">
          <Main />
        </div>
      </BrowserRouter>
    )
  }
}

export default App;

// const container = document.getElementById("app");
// render(<App />, container);

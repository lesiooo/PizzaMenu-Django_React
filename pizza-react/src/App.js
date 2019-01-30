import React, { Component } from 'react';
import logo from './logo.svg';
import routes from './routes.js';
import './App.css';
import {Link} from 'react-router-dom';

class App extends Component {
  render() {
    return (
     <div>
       <h1>Pizza Leszka</h1>

        {routes}
     </div>
    );
  }
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from './components/navbar';
import Home from './components/pages/home';
import About from './components/pages/about'
import Copyright from './components/cprt';
import Contributors from './components/pages/contributors';
import './App.css';
import Downloads from './components/pages/downloads';


function App() {
  return (
    <div className="App">
      <Router>
        <NavBar />
        <Switch>
          <Route path="/" exact component={() => <Home />} />
          <Route path="/about" exact component={() => <About />} />
          <Route path="/contributors" exact component={() => <Contributors />} />
          <Route path="/downloads" exact component={() => <Downloads />} />
        </Switch>
        <Copyright />
      </Router>
    </div>
  );
}

export default App;

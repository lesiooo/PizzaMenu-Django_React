import React from 'react';
import {BrowserRouter as Router, Route, Link } from 'react-router-dom';
import App from './App';
import PizzaList from './components/PizzaList';
import IngredientList from './components/IngredientList';
import PizzaDetail from './components/PizzaDetail';
import IngredientDetail from './components/IngredientDetail';
import CreatePizza from './components/CreatePizza';

export default (
    <Router>
        <div>
            <ul>
                <li><Link to="/pizza">Menu</Link></li>
                <li><Link to="/ingredients">Skladniki</Link></li>
                <li><Link to="/create-pizza">Stwórz pizze</Link></li>
            </ul>
            <Route exact path="/" component={App}/>
            <Route name="pizza" path="/pizza" component={PizzaList}/>
            <Route name="ingredients" path="/ingredients" component={IngredientList}/>
            <Route name="pizza-detail" path="/pizza-detail" component={PizzaDetail}/>
            <Route name="ingredient-detail" path="/ingredient-detail" component={IngredientDetail} />
            <Route name="create-pizza" path="/create-pizza" component={CreatePizza} />
        </div>
    </Router>
)

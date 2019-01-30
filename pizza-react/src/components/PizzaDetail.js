import React from 'react';
import Pizza from './Pizza.js'
import axios from 'axios';
import { Redirect } from 'react-router-dom'

class PizzaDetail extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            pizza: [],
            ingredients: [],
            redirect: false
        };
        this.handleDeleteEvent = this.handleDeleteEvent.bind(this);
    }
    componentDidMount(){
        console.log('Pizza Detail');
        console.log(this.props.location.state.props);
        fetch('http://127.0.0.1:8000/pizza/' + this.props.location.state.props)
            .then(response => response.json())
            .then(response => this.setState({pizza: response}));

        fetch('http://127.0.0.1:8000/ingredient/ingredient2pizza/' + this.props.location.state.props)
            .then(response => response.json())
            .then(response => this.setState({ingredients: response}));
    }

    handleDeleteEvent(event) {
        event.preventDefault();

        axios({
            method: 'delete',
            baseURL: 'http://127.0.0.1:8000/pizza/',
            url:  this.props.location.state.props + '/',
            xsrfHeaderName: "X-CSRFToken"
        })
            .then(response => console.log(response))
            .then(response =>
                this.setState({redirect: true})

        )
            .catch(function(error){
                console.log(error);
            })
    }


    render() {
        const display_pizza = (
        <div>
                <Pizza
                    pizza_id={this.state.pizza.pizza_id}
                    name={this.state.pizza.name}
                    price={this.state.pizza.price}
                    crust={this.state.pizza.crust}/>
        </div>
    );


    const display_ingredients = (
        <div>
            {this.state.ingredients.map((ingredient, key) =>{
                return <li>{ingredient.ingredient_name} </li>
            })}
        </div>
    );

    const delete_pizza = (
        <div>

            <button  onClick={(e) => { if (window.confirm('Czy rzeczywiście chcesz usunąć podaną pizzę?')) this.handleDeleteEvent(e) } }>
              Usun Pizze
            </button>
        </div>
    );

        if (this.state.redirect){
            return <Redirect to="/pizza"/>
        }
        return (
            <div>
                <h1>Pizza Detail</h1>
                {display_pizza}
                {delete_pizza}
                <p>Użyte składniki {display_ingredients}</p>
            </div>
        )
    }
}

export default PizzaDetail;
import React from 'react';
import Ingredient from './Ingredient.js'
import axios from 'axios';
import { Redirect } from 'react-router-dom'

class IngredientDetail extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ingredient: [],
            redirect: false
        };
        this.handleDeleteEvent = this.handleDeleteEvent.bind(this);

    }

    componentDidMount(){
        console.log('Pizza Detail');
        console.log(this.props.location.state.props);
        fetch('http://127.0.0.1:8000/ingredient/i/' + this.props.location.state.props)
            .then(response => response.json())
            .then(response => this.setState({ingredient: response}));
    }

    handleDeleteEvent(event) {
        event.preventDefault();

        axios({
            method: 'delete',
            baseURL: 'http://127.0.0.1:8000/ingredient/i/',
            url:  this.props.location.state.props + '/',
            xsrfHeaderName: "X-CSRFToken"
        })
            .then(response => console.log(response))
            .then(response =>
                this.setState({redirect: true})

        )
            .catch(function(error){
                if (error.response.status == 304) {
                    alert('Składnik jest używany z jakąś pizzą.');
                }
                console.log(error);
            })
    }


    render() {
        const display_ingredient = (
            <div>
                    <Ingredient
                        ingredient_id={this.state.ingredient.ingredient_id}
                        name={this.state.ingredient.name}
                        cost={this.state.ingredient.cost} />
            </div>
        );

        const delete_ingredient = (
            <div>

                <button  onClick={(e) => { if (window.confirm('Czy rzeczywiście chcesz usunąć podany składnik?')) this.handleDeleteEvent(e) } }>
                  Usun Składnik
                </button>
            </div>
        );


        if (this.state.redirect){
                return <Redirect to="/ingredients"/>
            }

        return (
            <div>
                <h1> Składnik </h1>
                {display_ingredient}
                {delete_ingredient}
            </div>
        )
    }
}

export default IngredientDetail;
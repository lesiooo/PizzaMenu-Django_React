import React, {Component} from 'react';
import Ingredient from './Ingredient';
import axios from 'axios';
import {Redirect} from 'react-router-dom';

class IngredientList extends Component {
    constructor() {
        super();
        this.state = {
            'ingredients': [],
            redirect: false
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    componentDidMount() {
        console.log('pobieram');
        fetch('http://127.0.0.1:8000/ingredient/i/')
            .then(response => response.json())
            .then(response => this.setState({'ingredients': response}));

    }

        handleSubmit(event) {
        event.preventDefault();
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/ingredient/i/',
            data: {
                name: event.target.name.value,
                cost: event.target.cost.value
            },
            xsrfHeaderName: "X-CSRFToken"
        })
            .then(response => console.log(response.data.ingredient_id))
            .then(response => this.componentDidMount())
            .catch(function(error){
                if (error.response.status == 400) {
                    alert('Nazwa składnika jest już używana');
                }


            })
    }
      renderList() {
        return (
            <div className="IngredientList">
                <h2>Skladniki</h2>
                {this.state.ingredients.map((ingredient, key) => {
                    return <div>
                        <Ingredient
                            ingredient_id={ingredient.ingredient_id}
                            name={ingredient.name}
                            cost={ingredient.cost}
                            hide={ingredient.ingredient_id}/>
                    </div>
                })}

            </div>
        );
    }



    render(){
        const create_form = (
        <div>
            <form  onSubmit={this.handleSubmit}>
                <label> Nazwa składnika: <input name="name" type="text"/></label> <br/>
                <label> Cena składnika: <input name="cost" type="number"/></label> <br/>
                <button type="submit"> Zapisz skladnik </button>
            </form>
        </div>
    );
        if (this.state.redirect){
                return <Redirect to="/ingredients"/>
            }
        return(
            <div>
                {create_form}
                {this.renderList()}
            </div>
        )
    }
}

export default IngredientList;

import React from 'react';
import axios from 'axios';


class CreatePizza extends React.Component {
    constructor(){
        super();
        this.state = {
            ingredients: [],
            selected_ingredients: [],
            price: 12.00,
            pizza_id: ''
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
         }

    componentDidMount() {
        let initialIngredients =[];
        console.log('pobieram');
        fetch('http://127.0.0.1:8000/ingredient/i/')
            .then(response =>  response.json())
            .then(response => this.setState({ingredients: response}));
    }

    handleSubmit(event) {
        event.preventDefault();
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/pizza/',
            data: {
            name: event.target.name.value,
            price: event.target.price.value,
            crust: event.target.crust.value
        },
            xsrfHeaderName: "X-CSRFToken"
        })
            .then(response => this.setState({pizza_id: response.data.pizza_id}))
            .then(response => this.addIngredientsToPizza())
            .catch(function(error){
                if (error.response.status == 400) {
                    alert('Nazwa Pizzy jest już używana');
                }else{
                    console.log(error);
                }

            });
    };
    addIngredientsToPizza() {
        for (let item of this.state.selected_ingredients) {
            console.log(item);
            axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/ingredient/ingredient2pizza/',
                data: {
                    ingredient2pizza: item,
                    pizza2ingredient: this.state.pizza_id
                },
                xsrfHeaderName: "X-CSRFToken"
            })
                .then(response => console.log(response))
                .catch(error => console.log(error));

        }
    };
    handleChange(event){
        console.log(event.target.name);
        console.log(event.target.value);
        console.log(event.target.checked);

        if (event.target.checked){
            this.setState({selected_ingredients:  this.state.selected_ingredients.concat(event.target.name),
            price: this.state.price + parseFloat(event.target.value)});
        }

    };

    render() {

        const create_pizza = (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>Nazwa:<input name="name" type="text" required="True"/></label><br/>
                    <label>Cena:<input name="price" type="text" value={this.state.price}/></label> <br/>
                    <label>Ciasto:<input name="crust" type="text" required="True"/></label>< br/>
                    <button type="submit"> Tworz pizze </button>
                </form>
            </div>
        );
        const get_ingredients = (
            <div>
                {this.state.ingredients.map((ingredient, key) => {
                    return <div>
                        <input name={ingredient.ingredient_id} type="checkbox" onChange={this.handleChange} value={ingredient.cost}/>
                        <label name="lab" >{ingredient.name}</label>
                    </div>
                })}
            </div>
        );


        return(
            <div>

                {create_pizza}
                {get_ingredients}
            </div>
    )
    }
}
export default(CreatePizza);
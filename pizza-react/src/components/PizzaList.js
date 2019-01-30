import React from 'react';
import Pizza from './Pizza.js';
import axios from 'axios';

class PizzaList extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            pizzas: [],
            searchString: ''
        };
        this.handleSearch = this.handleSearch.bind(this);
    }
    componentDidMount() {
        console.log('pobieram');
        fetch('http://127.0.0.1:8000/pizza/')
            .then(response => response.json())
            .then(response => this.setState({pizzas: response}));
    }
    handleSearch(e){
        this.setState({
            searchString: e.target.value
        })
  };

    render() {
        let pizzas = this.state.pizzas;
        let search = this.state.searchString.trim().toLowerCase();
        if (search.length > 0) {
            pizzas = pizzas.filter(function(pizza) {
            return pizza.name.toLowerCase().match(search);
            });
        }

        const renderList = (

            <div className="Lista-pizz">
                <h2>Menu</h2>
                {pizzas.map((pizza, key) => {
                    return <div>
                        <Pizza
                            pizza_id={pizza.pizza_id}
                            name={pizza.name}
                            price={pizza.price}
                            crust={pizza.crust}
                            hide={pizza.pizza_id}/>
                    </div>
                })}
            </div>

    );
        const search_form = (
            <div>
                <form onChange={this.handleSearch}>
                   <input name="search" type="text" placeholder="szukaj" value={this.state.searchString}/>
                </form>
            </div>
        );

        return(
            <div>
                {search_form}
                {renderList}
            </div>
        )
    }
}

export default (PizzaList)
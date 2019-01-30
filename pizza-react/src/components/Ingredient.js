import React from 'react';
import '../css/ingredient.css';
import { Link } from 'react-router-dom';

const ingredient = (props) => {
    return (

        <div className="Ingredient">
        <p>Nazwa: {props.name}</p>
        <p>Cena: {props.cost}</p>
            {props.hide ? <Link to={{
            pathname: "/ingredient-detail",
            state: {props: props.ingredient_id}
        }}>
            <button type="submit" value="Detail"> Detail</button>
        </Link>: null}
        </div>
    )
};

export default ingredient;
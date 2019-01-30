import React from 'react';
import '../css/Pizza.css';
import { Link } from 'react-router-dom';

const pizza = (props) => {
    return (

        <div className="Pizza">
        <p>Nazwa: {props.name}</p>
        <p>Cena:{props.price}</p>
        <p>Ciasto: {props.crust}</p>
            {props.hide ? <Link to={{
            pathname: "/pizza-detail",
            state: {props: props.pizza_id}
        }}>
            <button type="submit" value="Detail"> Detail</button>
        </Link>: null}
        </div>
    )
};

export default pizza;
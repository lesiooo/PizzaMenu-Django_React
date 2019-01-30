import React from 'react';

class Ing extends React.Component {
    constructor() {
        super();
    }

    render () {
        let ingredients = this.props.state.ingredients;
        let optionItems = ingredients.map((ingredient) =>
                <option key={ingredient.name}>{ingredient.name}</option>
            );

        return (
         <div>
             <select>
                {optionItems}
             </select>
         </div>
        )
    }
}

export default Ing;
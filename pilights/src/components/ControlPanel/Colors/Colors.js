import React, { useState } from 'react';

// import Dropdown from 'react-bootstrap/Dropdown';
// import DropdownButton from 'react-bootstrap/DropdownButton';
// import ButtonGroup from 'react-bootstrap/ButtonGroup';
// // import 'bootstrap/dist/css/bootstrap.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

async function postColor(url = 'http://192.168.1.214:5000/changecolor', colorList = {}){


  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(colorList) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}

function Colors(props){

    //COLOR DEFENITIONS RGB
    const off = [0, 0, 0];
    const green = [[0, 255, 0], 'green'];
    const red = [[255, 0, 0], 'red'];
    const blue = [[0, 0, 255], 'blue'];


    const orange = [[55, 128, 0], 'orange'];
    const yellow = [[255, 255, 0], 'yellow'];
    const lightGreen = [[128, 255, 0], 'light green'];
    const powderBlue = [[0, 255, 255], 'powder blue'];
    const purple = [[127, 0, 255], 'purple'];
    const pink = [[255, 0, 255], 'pink'];

    const [color, setColor] = useState({});

;

    const payload = {
        color: red,
        effect: 'fullOn'
    }



    return(
        <div>
            <button onClick={function(){postColor('http://192.168.1.214:5000/changecolor', payload); props.getData(props.setLightData)}}>Turn Lights on Red</button>
 
        </div>
    );

}

export default Colors;
import React, { useState } from 'react';
import './lights.scss';
// import Dropdown from 'react-bootstrap/Dropdown';
// import DropdownButton from 'react-bootstrap/DropdownButton';
// import ButtonGroup from 'react-bootstrap/ButtonGroup';
// // import 'bootstrap/dist/css/bootstrap.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';

function setColor(color) {
    var url = `http://192.168.1.214:5000/${color}`

    const hello = fetch(url)
      .then(res => res.json()).then((response) => console.log(response));

    console.log(url);
}

function lightPower(onOrOff) {
    var url = `http://192.168.1.214:5000/${onOrOff}`
    const hello = fetch(url)
      .then(res => res.json()).then(response => console.log(response));
  
    console.log(url);
}

function Colors(props){
    let root = document.documentElement;

    const [evensColor, setEvensColor] = useState('rgb(0, 0, 0)');
    const [oddsColor, setOddsColor] = useState('rgb(0, 0, 0)');
    const [active, setActive] = useState(true);

    function fullColor(color){
        setEvensColor(color);
        setOddsColor(color);
        console.log(evensColor, oddsColor);
      }
  
    
    if(active){
      root.style.setProperty('--evensColor', evensColor);
      root.style.setProperty('--oddsColor', oddsColor);
      
    }else{
      root.style.setProperty('--evensColor', 'rgb(0, 0, 0)');
      root.style.setProperty('--oddsColor', 'rgb(0, 0, 0)');
      
    }


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

    //const [color, setColor] = useState({});

    console.log(props.data);


    return(
        <div>
            
        <ul class="lightrope">
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>

        <button className='lightbtn' onClick={function(){setActive(true); lightPower('on');}}>Turn on</button>
        <button className='offbtn' onClick={function(){setActive(false); lightPower('off'); }}>Turn Off</button>

            <button onClick={function(){setColor('red'); fullColor(`rgb(${red[0][0]}, ${red[0][1]}, ${red[0][2]})`);}}>Turn Lights on Red</button>
 
        </div>
    );

}

export default Colors;
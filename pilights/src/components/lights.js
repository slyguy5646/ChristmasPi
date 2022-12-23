import React, { useState } from 'react';
import './lights.scss';
// import Dropdown from 'react-bootstrap/Dropdown';
// import DropdownButton from 'react-bootstrap/DropdownButton';
// import ButtonGroup from 'react-bootstrap/ButtonGroup';
// // import 'bootstrap/dist/css/bootstrap.css';
import Select from 'react-select';

/* FORMAT FOR LIGHT DATA
{
  color: 'red',      OPTIONS: 'red', 'green', 'blue', etc (check color.py/colorObj for all options)
  effect: 'fullOn', OPTIONS: 'fullOn', 'ledOff' (FOR NOW)
  status: 'ON' OPTIONS: 'ON', 'OFF' (FOR NOW)
}
*/

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









function Lights(props){
  const [lightDataToSend, setLightDataToSend] = useState({
    color: 'off',
    effect: 'ledOff',
    status: 'OFF'
  })
  
  
  const [colorToSend, setColorToSend] = useState('Select a Color');
  const [effectToSend, setEffectToSend] = useState('ledOff');
  const [statusToSend, setStatusToSend] = useState('OFF');
  
  
  function updateLightDataToSend(object){
    setLightDataToSend(object)
  }

  async function postLightData(){

    const lightData = lightDataToSend;
      const response = await fetch('http://192.168.1.214:5000/lights', {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'no-cors',
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(lightDataToSend) // body data type must match "Content-Type" header
    });
    
    // console.log('sent');
    // console.log(response.json());
    //return response.json(); // parses JSON response into native JavaScript objects
    
  }


  let root = document.documentElement;

  const [evensColor, setEvensColor] = useState('rgb(255, 0, 255)');
  const [oddsColor, setOddsColor] = useState('rgb(255, 255, 255)');
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




    //const [color, setColor] = useState({});

    console.log(props.data);

    const colorDropdownOptions = [

      { value: 'off', label: 'Off'},
      { value: 'red', label: 'Red'},
      { value: 'green', label: 'Green'},
      { value: 'blue', label: 'Blue'},
      { value: 'orange', label: 'Orange'},
      { value: 'yellow', label: 'Yellow'},
      { value: 'lightGreen', label: 'Light Green'},
      { value: 'powderBlue', label: 'Cyan'},
      { value: 'purple', label: 'Purple'},
      { value: 'pink', label: 'Pink'},
    ]
    
    const effectDropdownOptions = [
      { value: 'ledOff', label: 'Off'},
      { value: 'fullOn', label: 'On'}
    ]

    async function sendTest(){
      setLightDataToSend({...lightDataToSend, effect: 'fullOn'});
      
            await fetch('http://192.168.1.214:5000/lights', {
            method: 'POST', // *GET, POST, PUT, DELETE, etc.
            mode: 'no-cors',
            headers: {
              'Content-Type': 'application/json'
              // 'Content-Type': 'application/x-www-form-urlencoded',
            },
            redirect: 'follow', // manual, *follow, error
            referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
            body: JSON.stringify(lightDataToSend) // body data type must match "Content-Type" header
          });
    }

    return(
        <div>
            
        <ul className={"lightrope"}>
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

        <h4>Color: {colorToSend}</h4>
        <h4>Effect: {effectToSend}</h4>
        <h4>Status: {statusToSend}</h4>

        <h3>{lightDataToSend?.color}</h3>
        <h3>{lightDataToSend?.effect}</h3>
        <h3>{lightDataToSend?.status}</h3>
        
        <div className='dropdowns'>
          <Select
            className={'colorDropdown'}
            placeholder={colorToSend}
            defaultValue={colorToSend}
            onChange={function(event){setColorToSend(event.label); setLightDataToSend({...lightDataToSend, color: event.value}); }}
            options={colorDropdownOptions}
            value={colorToSend}
          />
          <Select
            className={'colorDropdown'}
            placeholder={'Select an Effect'}
            defaultValue={effectToSend}
            onChange={function(event){ setLightDataToSend({...lightDataToSend, effect: event.value});}}
            options={effectDropdownOptions}
          />
        </div>

        {/* <h1>{colorToSend}</h1> */}
        {/* <button onClick={function(){setColorToSend('red');}}>Set Color Red</button> */}
        <button onClick={async function(){sendTest();}}>Turn On</button>
        <button onClick={async function(){setLightDataToSend({...lightDataToSend, color: 'off', effect: 'ledOff'}); postLightData(); setColorToSend('off')}}>Turn Off</button>
        <button onClick={function(){setLightDataToSend({...lightDataToSend}); postLightData(); console.log(lightDataToSend);}}>Apply</button>
        </div>

    );

}

export default Lights;
import React, { useState, useEffect } from 'react';
import styles from './data.css';


function DataPanel(props) {

    // const payload = {
    //     color: [255, 0, 255],
    //     effect: "fullOn"
    // }

    // async function postData(url = '', data = {}) {
    //     // Default options are marked with *
    //     const response = await fetch(url, {
    //       method: 'POST', // *GET, POST, PUT, DELETE, etc.
    //       headers: {
    //         'Content-Type': 'application/json'
    //         // 'Content-Type': 'application/x-www-form-urlencoded',
    //       },
    //       redirect: 'follow', // manual, *follow, error
    //       referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    //       body: JSON.stringify(data) // body data type must match "Content-Type" header
    //     });
    //     return response.json(); // parses JSON response into native JavaScript objects
    // }

    

    return ( 
        <div className='data'>
            <h1>Color: {props.data ? props.data.color : "no color data"}</h1>
            {/* <button onClick={function(){postData('http://192.168.1.214:5000/changecolor', payload); props.getData(props.setLightData)}}>Turn Lights on Red</button> */}
        </div>
    );
}

export default DataPanel;

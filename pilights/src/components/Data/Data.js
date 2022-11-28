import React, { useState, useEffect } from 'react';
import styles from './data.css';

function DataPanel(props) {
    return ( 
        <div>
            <h1>Color: {props.data ? props.data.color : "no color data"}</h1>
        </div>
    );
}

export default DataPanel;

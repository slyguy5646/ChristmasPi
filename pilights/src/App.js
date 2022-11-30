import React, { useEffect, useState } from 'react';
import Lights from './components/lights';


function App() {

  const [lightData, setLightData] = useState({});


  console.log(lightData);

  function getData(setFunc) {
    const hello = fetch('http://192.168.1.214:5000/lightdata')
      .then(res => res.json()).then(response => setFunc(response))
  }


  return (
    <div>
      <h1>{lightData.color}</h1>

      <Lights />

    </div>
  );
}

export default App;
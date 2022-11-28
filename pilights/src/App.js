import React, { useEffect, useState } from 'react';
import DataPanel from './components/Data/Data';
import Lights from './components/Lights/lights';
import Colors from './components/ControlPanel/Colors/Colors';

function App() {

  const [lightData, setLightData] = useState({});


  console.log(lightData);

  function getData(setFunc) {
    const hello = fetch('http://192.168.1.214:5000/lightdata')
      .then(res => res.json()).then(response => setFunc(response))
  }


  return (
    <div>

      <DataPanel data={lightData} setData={setLightData} getData={getData} />
      <Colors data={lightData} setData={setLightData} getData={getData}/>
      <Lights />

    </div>
  );
}

export default App;
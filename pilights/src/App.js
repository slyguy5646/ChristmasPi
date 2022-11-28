import React, { useEffect, useState } from 'react';
import DataPanel from './components/Data/Data';
import Lights from './components/Lights/lights';
import Colors from './components/ControlPanel/Colors/Colors';

function App(){

  const [lightData, setLightData] = useState({});

   useEffect(() => {
      const hello = fetch('http://192.168.1.214:5000/lightdata')
         .then(res => res.json()).then(response => setLightData(response))

   }, []);

   console.log(lightData);




  return(
    <div>

      <DataPanel data={lightData}/>
      <Lights/>

      <Colors/>
    </div>
  );
}

export default App;
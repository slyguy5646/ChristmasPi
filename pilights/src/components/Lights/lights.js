import React, { useState, useEffect } from 'react';
import './lights.scss';


function Lights() {

  const [active, setActive] = useState(true);

  const root = document.documentElement;
  root?.style.setProperty('--evensColor', active ? 'rgba(0,255,255,1)' : "white");
    return ( 
      <div className='lightsDiv'>

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

        <button className='lightbtn' onClick={function(){setActive(!active)}}>Toggle Lights</button>
      </div>
     );
}

export default Lights;

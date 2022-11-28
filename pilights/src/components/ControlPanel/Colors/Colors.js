import React, { useState } from 'react';

// import Dropdown from 'react-bootstrap/Dropdown';
// import DropdownButton from 'react-bootstrap/DropdownButton';
// import ButtonGroup from 'react-bootstrap/ButtonGroup';
// // import 'bootstrap/dist/css/bootstrap.css';
import Dropdown from 'react-dropdown';
import 'react-dropdown/style.css';


function Colors(){

    //COLOR DEFENITIONS RGB
    const off = (0, 0, 0);
    const green = [(0, 255, 0), 'green'];
    const red = [(255, 0, 0), 'red'];
    const blue = [(0, 0, 255), 'blue'];


    const orange = [(255, 128, 0), 'orange'];
    const yellow = [(255, 255, 0), 'yellow'];
    const lightGreen = [(128, 255, 0), 'light green'];
    const powderBlue = [(0, 255, 255), 'powder blue'];
    const purple = [(127, 0, 255), 'purple'];
    const pink = [(255, 0, 255), 'pink'];

    const [color, setColor] = useState({});


    const options = [
        'one', 'two', 'three'
      ];
      const defaultOption = options[0];


    return(
        <div>

            <div class="col">
      
                <div class="dropdown-container dropdown-solid">
                    <div class="dropdown-toggle click-dropdown">
                        DropDown Menu
                    </div>
                    <div class="dropdown-menu">
                        <ul>
                            <li><a href="#" onClick={function(){setColor({"color": green[0]})}}>DropDown Menu Item 1</a></li>
                            <li><a href="#">DropDown Menu Item 2</a></li>
                            <li><a href="#">DropDown Menu Item 3</a></li>
                            <li><a href="#">DropDown Menu Item 4</a></li>
                        </ul>
                          
                    </div>
                </div>
            </div>
        </div>
    );

}

export default Colors;
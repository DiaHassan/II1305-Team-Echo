import React, { useRef, useState } from "react";
import axios from 'axios';


export default function Controlpanel() {
    const [date,setDate] = useState("2023-08-07")
    const [db,setDb] = useState("2023-08-06")

    const handleDate = () => {
        
        axios.post('https://rusty-quince-umuv-main-csa3pvckba-lz.a.run.app/rd', {test: date})
            .catch(error => console.log(error));
    };

    const handleTest = () => {
        
        axios.post('https://rusty-quince-umuv-main-csa3pvckba-lz.a.run.app/test', {test: 10})
            .catch(error => console.log(error));
    };
    const handleDb = () => {
        
        axios.post('https://rusty-quince-umuv-main-csa3pvckba-lz.a.run.app/sd', {test: 1})
            .then(response => setDb(response.data.number))
            .catch(error => console.log(error));
    };
  return (
    <>
      <div>
        
        <button onClick={handleTest} className='forlistbutton'> Test </button>
        <button onClick={handleDb} className='forlistbutton'> Get all </button>
        <button onClick={handleDate} className='forlistbutton'> Date Remover </button>

        {console.log(db)}
      </div>

    </>
  )
}
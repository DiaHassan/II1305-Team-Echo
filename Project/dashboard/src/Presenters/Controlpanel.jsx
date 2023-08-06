import React, { useRef, useState } from "react";
import axios from 'axios';


export default function Controlpanel() {
    const [date,setDate] = useState("2023-08-06")

    const handleDate = () => {
        
        axios.post('http://127.0.0.1:8888/rd', {test: date})
            .catch(error => console.log(error));
    };

    const handleTest = () => {
        
        axios.post('http://127.0.0.1:8888/test', {test: 10})
            .catch(error => console.log(error));
    };
    const handleDb = () => {
        
        axios.post('http://127.0.0.1:8888/sd', {test: 1})
            .catch(error => console.log(error));
    };
  return (
    <>
      <div>
        <button onClick={handleTest} className='forlistbutton'> Test </button>
        <button onClick={handleDb} className='forlistbutton'> Get all </button>
        <button onClick={handleDate} className='forlistbutton'> Date Remover </button>
      </div>

    </>
  )
}
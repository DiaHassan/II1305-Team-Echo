import React, { useRef, useState } from "react";
import axios from 'axios';
import Schedual from "./Schedualed";
import listToDic from "./Tabletest"

export default function Controlpanel() {
    const [date,setDate] = useState("2023-08-08")
    const [db,setDb] = useState("2023-08-06")

    const handleDate = () => {
        
        axios.post('https://rusty-quince-umuv-main-csa3pvckba-lz.a.run.app/rd', {test: date})
            .catch(error => console.log(error));
    };

    const handleTest = () => {
        
        axios.post('https://rusty-quince-umuv-main-csa3pvckba-lz.a.run.app/test', {test: 5})
            .catch(error => console.log(error));
    };
    const handleDb = () => {
        
        axios.post('https://rusty-quince-umuv-main-csa3pvckba-lz.a.run.app/sd', {test: 1})
            .then(response => setDb(response.data.number))
            .catch(error => console.log(error));
    };
    function toArray(db){
      const list = [];
      for (let i = 0; i < db.length; i++){
        list[i] = db[i]
      }
      return list
    }
    const downloadTxtFile = () => {
      const list = toArray(db)
      console.log(list)
      const element = document.createElement('a');
      const text = list.join('\n');
      const file = new Blob([text], { type: 'text/plain' });
      element.href = URL.createObjectURL(file);
      element.download = 'db.txt';
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);
    };
  return (
    <>
      <div>
        
        <button onClick={handleTest} className='forlistbutton'> Test </button>
        <button onClick={handleDb} className='forlistbutton'> Get all </button>
        <button onClick={handleDate} className='forlistbutton'> Date Remover </button>

        {typeof db}
        <div className="App">
          <button onClick={downloadTxtFile}>Download List as TXT</button>
        </div>
        {/* <Schedual/> */}
      </div>

    </>
  )
}
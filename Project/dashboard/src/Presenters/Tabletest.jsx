import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

export default function Tabletest() {

    const data = [
        {name: 'Blekinge län', value: 0},
        {name: 'Dalarnas län', value: 5},
        {name: 'Gotlands län', value:0},
        {name: 'Gävleborgs län', value:1000},
        {name: 'Hallands län', value:0},
        {name: 'Jämtlands län', value: 0},
        {name: 'Jönköpings län', value: 0},
        {name: 'Kalmar län', value:0},
        {name: 'Kronobergs län', value: 0},
        {name: 'Norrbottens län', value: 0},
        {name: 'Skåne län', value: 0},
        {name: 'Stockholms län', value: 0},
        {name: 'Södermanlands län', value: 0},
        {name: 'Uppsala län', value: 0},
        {name: 'Värmlands län', value: 0},
        {name: 'Västerbottens län', value: 0},
        {name: 'Västernorrlands län', value: 0},
        {name: 'Västmanlands län', value: 0},
        {name: 'Västra Götalands län', value: 0},
        {name: 'Örebro län', value: 0},
        {name: 'Östergötlands län', value: 0}
      ];
      
    const [result, setResult] = useState(data);
    const [job, setJob] = useState('')


    const handleChange = (event) => {
        setJob(event.target.value);
    }

    function convertList(originalList) {
        const newList = [];
        for (let i = 0; i < originalList.length; i++) {
          const name = originalList[i][0];
          const value = Math.round(originalList[i][1]);
          newList.push({ name: name, value: value });
        }
        return newList;
      }
      
    const handleClick = () => {
      axios.post('http://localhost:5000/why',{job:job})
        .then(response => setResult(convertList(response.data.number)))
        .catch(error => console.log(error));
        console.log((result));
    };
 

    return (
        <div className='fortableandlist'>
            <BarChart width={1000} height={600} data={result}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" height={150}  interval={0} angle={-45} textAnchor="end"/>
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="value" fill="#8884d8" />
            </BarChart>
            
            <div className='forlist'>
                <form onSubmit={handleClick} className='forlistlist'>
                    <label>
                        Select an option:
                        <select value={job} onChange={handleChange}>
                        <option value="">Choose an option</option>
                        <option value="Kock">Kock</option>
                        <option value="Städare">Städare</option>
                        <option value="Utvecklare">Utvecklare</option>
                        <option value="Sjuksköterska">Sjuksköterska</option>
                        <option value="Läkare">Läkare</option>
                        <option value="Lärare">Lärare</option>
                        <option value="Operatör">Operatör</option>
                        <option value="Personlig assistent">Personlig assistent</option>
                        <option value="Mekaniker">Mekaniker</option>
                        <option value="Butikssäljare">Butikssäljare</option>
                        <option value="Civilingenjör">Civilingenjör</option>
                        <option value="Projektledare">Projektledare</option>
                        </select>
                    </label>
                </form>
                <button onClick={handleClick} className='forlistbutton'>Run Python function</button>
            </div>
        </div>
    );
}
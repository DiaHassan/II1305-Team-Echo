import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
// import {} from '@material-ui/core'; //test
import { makeStyles } from '@material-ui/core/styles';
import { FormControl,Checkbox, FormLabel, RadioGroup, Radio, FormControlLabel, Select, MenuItem } from '@material-ui/core';


export default function Tabletest() {

    const data = [
        {name: 'Blekinge län', value: 0},
        {name: 'Dalarnas län', value: 0},
        {name: 'Gotlands län', value:0},
        {name: 'Gävleborgs län', value:0},
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
    
    // Setting varibles and useStates
    const [result, setResult] = useState(data);
    const [job, setJob] = useState('')
    const [showLegend, setShowLegend] = useState(true); //test


    const initialJobList = ["Ingenjör","Utvecklare","Läkare","Sjuksköterska","Lärare","Operatör","Tekniker","Elektriker","Projektledare","Logistiker"]
    const allCounties = ["Västmanlands län","Västernorrlands län","Västerbottens län","Värmlands län","Uppsala län","Södermanlands län","Stockholms län","Skåne län","Örebro län","Norrbottens län","Kalmar län","Jönköpings län","Jämtlands län","Hallands län","Gävleborgs län","Gotlands län","Dalarnas län","Blekinge län","Västra Götalands län","Östergötlands län","Kronobergs län"]

    const [activeList , setActivelist] = useState([false,false,false,false,false,false,false,false,false])
    const [joblist, setJobList] = useState(initialJobList)  
    const [linkedinCB, setLinkedinCB] = React.useState(true);
    const [platsbankenCB, setPlatsbankenCB] = React.useState(true);
    const [ledigaCB, SetLedigaCB] = React.useState(true);
    // Handlers both onClick and onChange
    const handleChange = (event) => {
        setJob(event.target.value);
    }
    const handleCheckboxliChange = (event) => {
        setLinkedinCB(event.target.checked)      
        console.log(linkedinCB)  
    };
    const handleCheckboxpbChange = (event) => {
        setPlatsbankenCB(event.target.checked)
        console.log(platsbankenCB)        
    };
    const handleCheckboxljChange = (event) => {
        SetLedigaCB(event.target.checked)        
    };

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

    // Styling exists here
    // const useStyles = makeStyles((theme) => ({
    //     root: {
    //         display: 'flex',
    //         flexDirection: 'row',
    //         justifyContent: 'space-between',
    //         alignItems: 'center'
    //     },
    //     formControl: {
    //         margin: theme.spacing(1),
    //         minWidth: 120,
    //     },
    // }));
    // const classes = useStyles();
     //className={classes.root}
     //className={classes.formControl}
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
                        
            <div >
                {/* Div containing 3 checkboxes */}
                <FormControl component="fieldset">
                    <FormLabel component="legend">Select an option:</FormLabel>
                    <Checkbox
                    label="Linked In"
                    checked={linkedinCB}
                    onChange={handleCheckboxliChange}
                    // inputProps={{ 'aria-label': 'controlled' }}
                    color= 'primary'

                    />
                    <Checkbox
                    checked={platsbankenCB}
                    onChange={handleCheckboxpbChange}
                    color='primary'
                    /> 
                    <Checkbox
                    checked={ledigaCB}
                    onChange={handleCheckboxljChange}
                    color='primary'
                    /> 
                </FormControl>

    
                
                {/* Div containing 2 drop-down lists */}
                <div>
                    <FormControl >
                    <Select value="value1">
                        <MenuItem value="value1">Value 1</MenuItem>
                        <MenuItem value="value2">Value 2</MenuItem>
                        <MenuItem value="value3">Value 3</MenuItem>
                    </Select>
                    </FormControl>
                    <FormControl >
                    <Select value="value4">
                        <MenuItem value="value4">Value 4</MenuItem>
                        <MenuItem value="value5">Value 5</MenuItem>
                    </Select>
                    </FormControl>
                </div>

                {/* Div containing 3 horizontal radio buttons */}
                <FormControl component="fieldset">
                    <FormLabel component="legend">Select an option:</FormLabel>
                    <RadioGroup row aria-label="position" name="position" defaultValue="top">
                    <FormControlLabel value="option1" control={<Radio />} label="Option 1" />
                    <FormControlLabel value="option2" control={<Radio />} label="Option 2" />
                    <FormControlLabel value="option3" control={<Radio />} label="Option 3" />
                    </RadioGroup>
                </FormControl>
                </div>
                <form onSubmit={handleClick} className='forlistlist'>
                    <label>
                        <select value={job} onChange={handleChange} className='select_options'>
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
                <button onClick={handleClick} className='forlistbutton'>Search</button>
            </div>
        </div>
    );
}
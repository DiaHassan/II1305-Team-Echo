import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
// import {} from '@material-ui/core'; //test
import { makeStyles } from '@material-ui/core/styles';

import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Checkbox from '@mui/material/Checkbox';
import FormGroup from '@mui/material/FormGroup';
import FormLabel from '@mui/material/FormLabel';
import FormControlLabel from '@mui/material/FormControlLabel';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';


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
    const [county, setCounty] = useState('')  
    const [linkedinCB, setLinkedinCB] = React.useState(false);
    const [platsbankenCB, setPlatsbankenCB] = React.useState(false);
    const [ledigaCB, SetLedigaCB] = React.useState(false);
    // Handlers both onClick and onChange
    const handleChange = (event) => {
        setJob(event.target.value);
    }
    const handleCheckboxliChange = (event) => {
        setLinkedinCB(event.target.checked)      
        const newList = [...activeList];
        newList[0] = !linkedinCB;
        setActivelist(newList);
        console.log(activeList)
    };
    const handleCheckboxpbChange = (event) => {
        setPlatsbankenCB(event.target.checked)
        const newList = [...activeList];
        newList[1] = !platsbankenCB;
        setActivelist(newList);   
        console.log(activeList)   
    };
    const handleCheckboxljChange = (event) => {
        SetLedigaCB(event.target.checked)  
        const newList = [...activeList];
        newList[2] = !ledigaCB;
        setActivelist(newList);  
        console.log(activeList)    
    };

    const handleChangeCounty = (event) => {
        setCounty(event.target.value);
      };


      const myListElements = allCounties.map((item) => {
        return <MenuItem value={{item}} key={item}>{item}</MenuItem>;
      });

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
                    <FormGroup>
                    <FormControlLabel control={<Checkbox
                    checked={linkedinCB}
                    onChange={handleCheckboxliChange}
                    // inputProps={{ 'aria-label': 'controlled' }}
                    color= 'default'
                    />} label="LinkedIn" />
                    <FormControlLabel control={<Checkbox
                    checked={platsbankenCB}
                    onChange={handleCheckboxpbChange}
                    color='default'
                    /> } label="Platsbanken" />
                    <FormControlLabel control={<Checkbox
                    checked={ledigaCB}
                    onChange={handleCheckboxljChange}
                    color='default'
                    /> } label="Lediga jobb" />
                </FormGroup>
                </FormControl>

    
                
                {/* Div containing 2 drop-down lists */}
                <div>
                <div>
                    <FormControl sx={{ m: 1, minWidth: 80 }}>
                        <InputLabel id="demo-simple-select-autowidth-label">County</InputLabel>
                        <Select
                        labelId="demo-simple-select-autowidth-label"
                        id="demo-simple-select-autowidth"
                        value={county}
                        onChange={handleChangeCounty}
                        autoWidth
                        label="County"
                        >
                            {myListElements}
                        </Select>
                    </FormControl>
                    </div>
                    </div>










                    <div>
                {/* Div containing 3 horizontal radio buttons */}
                    <FormControl component="fieldset">
                    <FormLabel component="legend">Select an option:</FormLabel>
                    <RadioGroup row aria-label="position" name="position" defaultValue="top">
                        
                        <FormControlLabel value="option1" control={<Radio />} label="Seniority" />
                        <FormControlLabel value="option2" control={<Radio />} label="Duration" />
                        <FormControlLabel value="option3" control={<Radio />} label="Years of experience" />
                        <FormControlLabel value="option4" control={<Radio />} label="Drivings license" />
                        <FormControlLabel value="option5" control={<Radio />} label="Prerequirements" />
                        <FormControlLabel value="option6" control={<Radio />} label="Employment type" />
                    

                    </RadioGroup>
                </FormControl>
                </div>

            
                
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
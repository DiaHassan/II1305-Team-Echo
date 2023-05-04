import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend,ResponsiveContainer } from 'recharts';
// import {} from '@material-ui/core'; //test
import { makeStyles } from '@material-ui/core/styles';

// import { MenuProps, useStyles, options } from "./utils";

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
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from "@material-ui/core/ListItemIcon";
import { Grid } from '@mui/material';


export default function Tabletest() {

    const data = [
        { name: 'Blekinge län', value: 0 },
        { name: 'Dalarnas län', value: 0 },
        { name: 'Gotlands län', value: 0 },
        { name: 'Gävleborgs län', value: 0 },
        { name: 'Hallands län', value: 0 },
        { name: 'Jämtlands län', value: 0 },
        { name: 'Jönköpings län', value: 0 },
        { name: 'Kalmar län', value: 0 },
        { name: 'Kronobergs län', value: 0 },
        { name: 'Norrbottens län', value: 0 },
        { name: 'Skåne län', value: 0 },
        { name: 'Stockholms län', value: 0 },
        { name: 'Södermanlands län', value: 0 },
        { name: 'Uppsala län', value: 0 },
        { name: 'Värmlands län', value: 0 },
        { name: 'Västerbottens län', value: 0 },
        { name: 'Västernorrlands län', value: 0 },
        { name: 'Västmanlands län', value: 0 },
        { name: 'Västra Götalands län', value: 0 },
        { name: 'Örebro län', value: 0 },
        { name: 'Östergötlands län', value: 0 }
    ];

    // Setting variables and useStates
    const [result, setResult] = useState(data);
    const [job, setJob] = useState('')
    const [showLegend, setShowLegend] = useState(true); //test, du kan ta bort 


    const initialJobList = ["Ingenjör", "Utvecklare", "Läkare", "Sjuksköterska", "Lärare", "Operatör", "Tekniker", "Elektriker", "Projektledare", "Logistiker"]
    const allCounties = ["Västmanlands län", "Västernorrlands län", "Västerbottens län", "Värmlands län", "Uppsala län", "Södermanlands län", "Stockholms län", "Skåne län", "Örebro län", "Norrbottens län", "Kalmar län", "Jönköpings län", "Jämtlands län", "Hallands län", "Gävleborgs län", "Gotlands län", "Dalarnas län", "Blekinge län", "Västra Götalands län", "Östergötlands län", "Kronobergs län"]

    const [activeList, setActivelist] = useState([false, false, false, false, false, false, false, false, false])
    const [joblist, setJobList] = useState(initialJobList)
    const [county, setCounty] = useState('Västmanlands län')
    //Checkboxes
    const [linkedinCB, setLinkedinCB] = React.useState(false);
    const [platsbankenCB, setPlatsbankenCB] = React.useState(false);
    const [ledigaCB, SetLedigaCB] = React.useState(false);
    //Radiobuttons
    const [option1, setOption1] = React.useState(false);
    const [option2, setOption2] = React.useState(false);
    const [option3, setOption3] = React.useState(false);
    const [option4, setOption4] = React.useState(false);
    const [option5, setOption5] = React.useState(false);
    const [option6, setOption6] = React.useState(false);

    // Handlers both onClick and onChange
    const handleChange = (event) => {
        setJob(event.target.value);
    }
    const handleCheckboxliChange = (event) => {
        handleSource(event);
        setLinkedinCB(event.target.checked)
        const newList = [...activeList];
        newList[0] = !linkedinCB;
        setActivelist(newList);
        console.log(activeList)
    };
    const handleCheckboxpbChange = (event) => {
        handleSource(event);
        setPlatsbankenCB(event.target.checked)
        const newList = [...activeList];
        newList[1] = !platsbankenCB;
        setActivelist(newList);
        console.log(activeList)
    };
    const handleCheckboxljChange = (event) => {
        handleSource(event);
        SetLedigaCB(event.target.checked)
        const newList = [...activeList];
        newList[2] = !ledigaCB;
        setActivelist(newList);
        console.log(activeList)
    };

    const handleChangeCounty = (event) => {
        setCounty(event.target.value);
    };

    const handleChangeJob = (event) => {
        setJobList(event.target.value);
    };


    const myListElements = allCounties.map((item) => {
        return <MenuItem value={item} key={item}>{item}</MenuItem>;
    });

    const myListElementJobs = joblist.map((item) => {
        return <MenuItem value={item} key={item}> <Checkbox checked={job.indexOf(item) > -1} /><ListItemText primary={item} /></MenuItem>
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

      function listToDict(list) {
        const dict = [];
        for (let i = 0; i < list.length; i++) {
          const row = list[i];
          const entry = {name: row[0]};
          for (let j = 1; j < row.length; j++) {
            const category = row[j][0];
            for (let k = 1; k < row[j].length; k++) {
              const [subcat, value] = row[j][k];
              const key = `${category}-${subcat}`;
              entry[key] = value;
            }
          }
          dict.push(entry);
        }
        return dict;
      }
    const handleClick = () => {
        const srcs = []
        if (activeList[0]){
            srcs.push('linkedin')
        }
        if (activeList[1]) {
            srcs.push('platsbanken')
        }
        if (activeList[2]) {
            srcs.push('ledigajobb')
        }
        const queryTbs = []
        queryTbs.push(srcs)
        queryTbs.push(county)
        queryTbs.push(joblist)
        queryTbs.push('employment_type')
        console.log(queryTbs)
        axios.post('http://localhost:8888/why',{job:queryTbs})
            .then(response => setResult(listToDict(response.data.number)))
            .catch(error => console.log(error));
        console.log((result));
    };
    function transformList(list) {
        const result = [];

        list.forEach((item) => {
            const obj = {
                name: item[0],
                ledigajobb: item[1][1][0],
                platsbanken: item[2][1][0]
            };
            result.push(obj);
        });
        return result;
    }

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


    const options = [
        "Oliver Hansen",
        "Van Henry",
        "April Tucker",
        "Ralph Hubbard",
        "Omar Alexander",
        "Carlos Abbott",
        "Miriam Wagner",
        "Bradley Wilkerson",
        "Virginia Andrews",
        "Kelly Snyder"
    ];

    const handleChanges = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setJobList(joblist.length === initialJobList.length ? [] : initialJobList);
            return;
        }
        setJobList(value);
        console.log(value)
    };


    //   --------------- Handle 'Gray out' functionlity:
    //insert all default values for buttons:
    const defaultValue = {
        employment_type: true,
        seniority: true,
        years_of_experience: true,
        duration: true,
        prerequirements: true,
        drivers_license: true,
        active: false
    };

    //insert all sources. Format 'sourcename': defaultValue
    const [inputs, setInputs] = useState({ platsbanken: defaultValue, linkedin: defaultValue,  ledigajobb:defaultValue});

    // Handles any changes to the source buttons
    const handleSource = (event) => {
        const name = event.target.name;
        // Due to the form only returning strings we need to parse it into correct format
        const value = splitKey(event.target.value);
        // Updates the values 
        setInputs(inputs => (
            {
                ...inputs,
                [name]: (event.target.checked ?
                    handleKeys(value) : defaultValue)
            }

        ));
        console.log(inputs);
    }

    // Parses the input paramater into correct format
    const splitKey = (s) => {
        const returnKeyValue = {};
        var x = s.replace(/[{}"']+/g, '').split(',');
        for (var i = 0; i < x.length; i++) {
            var split = x[i].split(':');
            returnKeyValue[split[0].trim()] = (split[1].trim() === 'true');
        }

        return returnKeyValue;
    }

    // Creates a key-value list filled with all changed and unchanged values
    const handleKeys = (value) => {
        const template = { ...defaultValue };
        for (let item of Object.keys(value)) {
            template[item] = value[item];
        }
        template.active = true;
        return template;
    }

    const getPropertyName = (obj, expression) => {
        var res = {};
        Object.keys(obj).map(k => { res[k] = () => k; });
        return expression(res)();
    }

    // --------




    return (
        <div className='fortableandlist'>
            
        {/* <ResponsiveContainer > */}
        <BarChart width={1000} height={600} data={result}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" height={150}  interval={0} angle={-45} textAnchor="end"/>
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="linkedin-deltid" stackId="a"  fill="#82ca9d" />
        <Bar dataKey="linkedin-heltid" stackId="a"  fill="#ffc658" />
        <Bar dataKey="ledigajobb-deltid" stackId="b"  fill="#ffc658" />
        <Bar dataKey="ledigajobb-heltid" stackId="b"  fill="#8284d8" />
        </BarChart>
        {/* </ResponsiveContainer> */}
        
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
                        <div>
                            <FormControl className="">
                                <InputLabel id="mutiple-select-label">Multiple Select</InputLabel>
                                <Select
                                    labelId="mutiple-select-label"
                                    multiple
                                    value={joblist}
                                    onChange={handleChanges}
                                    renderValue={(joblist) => joblist.join(", ")}
                                    // MenuProps={MenuProps}
                                    maxwidth="100"
                                >
                                    <MenuItem
                                        value="all"
                                    // classes={{
                                    //     root: isAllSelected ? classes.selectedAll : ""
                                    // }}
                                    ></MenuItem>
                                    {initialJobList.map((option) => (
                                        <MenuItem key={option} value={option}>
                                            <ListItemIcon>
                                                <Checkbox checked={joblist.indexOf(option) > -1} />
                                            </ListItemIcon>
                                            <ListItemText primary={option} />
                                        </MenuItem>
                                    ))}
                                </Select>
                            </FormControl>
                        </div>

                    </div>


                    <div className="radio">
                        {/* Div containing 3 horizontal radio buttons */}
                        <RadioGroup aria-label="position" name="position" defaultValue="top">
                            <FormControl component="fieldset">

                                <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="option1" control={<Radio size="small" />} label="Employment type" 
                                        disabled={inputs.platsbanken.employment_type && inputs.linkedin.employment_type && inputs.ledigajobb.employment_type ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="option2" control={<Radio size="small" />} label="Duration"
                                        disabled={inputs.platsbanken.duration && inputs.linkedin.duration && inputs.ledigajobb.duration ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="option3" control={<Radio size="small" />} label="Seniority"
                                        disabled={inputs.platsbanken.seniority && inputs.linkedin.seniority && inputs.ledigajobb.seniority ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="option4" control={<Radio size="small" />} label="Prerequirements"
                                        disabled={inputs.platsbanken.prerequirements && inputs.linkedin.prerequirements && inputs.ledigajobb.prerequirements ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="option5" control={<Radio size="small" />} label="Years of experience"
                                        disabled={inputs.platsbanken.years_of_experience && inputs.linkedin.years_of_experience && inputs.ledigajobb.years_of_experience ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="option6" control={<Radio size="small" />} label="Driver's license"
                                        disabled={inputs.platsbanken.drivers_license && inputs.linkedin.drivers_license && inputs.ledigajobb.drivers_license ? false : true} />
                                    </Grid>
                                </Grid>
                            </FormControl>

                        </RadioGroup>

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
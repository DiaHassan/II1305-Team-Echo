import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
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
        { name: 'Östergötlands län', value: 0 },
    ];

    const data2 = [
        { name: 'Läkare', 'Linkedin-None': 159, 'ledigajobb-0': 445, 'ledigajobb-1': 7, 'ledigajobb-2': 157 },
        { name: 'Lärare', 'Linkedin-None': 186, 'ledigajobb-0': 677, 'ledigajobb-2': 21, 'ledigajobb-3': 62 },
        { name: 'Operatör', 'Linkedin-None': 62, 'ledigajobb-0': 58, 'ledigajobb-2': 2, 'ledigajobb-3': 2 },
        { name: 'Projektledare', 'Linkedin-None': 95, 'ledigajobb-0': 500, 'ledigajobb-2': 1, 'ledigajobb-3': 4 },
        { name: 'Sjuksköterska', 'Linkedin-None': 186, 'ledigajobb-0': 870, 'ledigajobb-1': 8, 'ledigajobb-2': 268 },
        { name: 'Utvecklare', 'Linkedin-None': 54, 'ledigajobb-0': 324, 'ledigajobb-6': 35 }
    ];

    // Setting variables and useStates
    const [result, setResult] = useState(data2);
    const [job, setJob] = useState('')
    const [showLegend, setShowLegend] = useState(true); //test, du kan ta bort 

    const initialJobList = ["Elektriker", "Ingenjör", "Logistiker", "Läkare", "Lärare", "Operatör", "Projektledare", "Sjuksköterska", "Tekniker", "Utvecklare"]
    const allCounties = ["Alla valda", "Blekinge län", "Dalarnas län", "Gotlands län", "Gävleborgs län", "Hallands län", "Jämtlands län", "Jönköpings län", "Kalmar län", "Kronobergs län", "Norrbottens län", "Skåne län", "Stockholms län", "Södermanlands län", "Uppsala län", "Värmlands län", "Västerbottens län", "Västernorrlands län", "Västmanlands län", "Västra Götalands län", "Örebro län", "Östergötlands län"]

    const [activeList, setActivelist] = useState([false, false, false, false, false, false, false, false, false])
    const [joblist, setJobList] = useState(initialJobList)
    const [county, setCounty] = useState('Alla valda')
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

    const [optionRadio, setOptionRadio] = React.useState(null);

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

    const handleParams = (event) => {
        setOptionRadio(event.target.value);
    }


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
            const entry = { name: row[0] };
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

    function dictToColumns(dict) {
        const columns = {};
        for (let i = 0; i < dict.length; i++) {
            for (const [key, value] of Object.entries(dict[i])) {
                const parts = key.split("-");
                if (parts[0] != "name") {
                    if (!(parts[0] in columns)) {
                        columns[parts[0]] = {};
                    }
                    columns[parts[0]][key] = true;
                }

            }
        }
        return columns;
    }

    const handleClick = () => {
        const srcs = []
        if (activeList[0]) {
            srcs.push('Linkedin')
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
        queryTbs.push(optionRadio)
        console.log(queryTbs)
        axios.post('http://localhost:8888/why', { job: queryTbs })
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


    const getBars = (InputColumns) => {
        const bars = [];
        if (InputColumns != undefined) {
            for (const [source, col] of Object.entries(InputColumns)) {
                for (const [barName, trueValue] of Object.entries(col)) {
                    bars.push([barName, source]);
                }
            }
        }
        return bars.map((bar) => <Bar dataKey={bar[0]} stackId={bar[1]}  fill="#82ca9d" />);
    }


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
    const [inputs, setInputs] = useState({ platsbanken: defaultValue, linkedin: defaultValue, ledigajobb: defaultValue });

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
                <XAxis dataKey="name" height={150} interval={0} angle={-45} textAnchor="end" />
                <YAxis />
                <Tooltip />
                <Legend />
                {getBars(dictToColumns(result))}
                {/* <Bar dataKey="Linkedin-deltid" stackId="a" fill="#82ca9d" />
                <Bar dataKey="Linkedin-heltid" stackId="a" fill="#308446" />
                <Bar dataKey="ledigajobb-deltid" stackId="b" fill="#ffc658" />
                <Bar dataKey="ledigajobb-heltid" stackId="b" fill="#E55137" /> */}
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
                                color='default'
                                name="linkedin"
                                value={JSON.stringify({
                                    employment_type: false
                                })}
                            />} label="LinkedIn" />
                            <FormControlLabel control={<Checkbox
                                checked={platsbankenCB}
                                onChange={handleCheckboxpbChange}
                                color='default'
                                name="platsbanken"
                                value={JSON.stringify({
                                    seniority: false,
                                    drivers_license: false
                                })}
                            />} label="Platsbanken" />
                            <FormControlLabel control={<Checkbox
                                checked={ledigaCB}
                                onChange={handleCheckboxljChange}
                                color='default'
                                name="ledigajobb"
                                value={JSON.stringify({
                                    prerequirements: false,
                                    employment_type: false
                                })}
                            />} label="Lediga jobb" />
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
                            <FormControl component="fieldset" >

                                <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="employment_type" control={<Radio size="small" />} label="Employment type" onChange={handleParams}
                                            disabled={inputs.platsbanken.employment_type && inputs.linkedin.employment_type && inputs.ledigajobb.employment_type ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="duration" control={<Radio size="small" />} label="Duration" onChange={handleParams}
                                            disabled={inputs.platsbanken.duration && inputs.linkedin.duration && inputs.ledigajobb.duration ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="seniority" control={<Radio size="small" />} label="Seniority" onChange={handleParams}
                                            disabled={inputs.platsbanken.seniority && inputs.linkedin.seniority && inputs.ledigajobb.seniority ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="requirement" control={<Radio size="small" />} label="Prerequirements" onChange={handleParams}
                                            disabled={inputs.platsbanken.prerequirements && inputs.linkedin.prerequirements && inputs.ledigajobb.prerequirements ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="years_of_experience" control={<Radio size="small" />} label="Years of experience" onChange={handleParams}
                                            disabled={inputs.platsbanken.years_of_experience && inputs.linkedin.years_of_experience && inputs.ledigajobb.years_of_experience ? false : true} />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="null" control={<Radio size="small" />} label="Driver's license" onChange={handleParams}
                                            disabled={inputs.platsbanken.drivers_license && inputs.linkedin.drivers_license && inputs.ledigajobb.drivers_license ? false : true} />
                                    </Grid>
                                </Grid>
                            </FormControl>

                        </RadioGroup>

                    </div>
                </div>
                <button onClick={handleClick} className='forlistbutton'>Search</button>
            </div>
        </div>
    );
}
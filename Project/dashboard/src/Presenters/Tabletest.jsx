import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import "../style.css";

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

    // const data = [
    //     { name: 'Blekinge län', value: 0 },
    //     { name: 'Dalarnas län', value: 0 },
    //     { name: 'Gotlands län', value: 0 },
    //     { name: 'Gävleborgs län', value: 0 },
    //     { name: 'Hallands län', value: 0 },
    //     { name: 'Jämtlands län', value: 0 },
    //     { name: 'Jönköpings län', value: 0 },
    //     { name: 'Kalmar län', value: 0 },
    //     { name: 'Kronobergs län', value: 0 },
    //     { name: 'Norrbottens län', value: 0 },
    //     { name: 'Skåne län', value: 0 },
    //     { name: 'Stockholms län', value: 0 },
    //     { name: 'Södermanlands län', value: 0 },
    //     { name: 'Uppsala län', value: 0 },
    //     { name: 'Värmlands län', value: 0 },
    //     { name: 'Västerbottens län', value: 0 },
    //     { name: 'Västernorrlands län', value: 0 },
    //     { name: 'Västmanlands län', value: 0 },
    //     { name: 'Västra Götalands län', value: 0 },
    //     { name: 'Örebro län', value: 0 },
    //     { name: 'Östergötlands län', value: 0 },
    // ];

    const data2 = [
        { name: 'Elektriker' },
        { name: 'Ingenjör' },
        { name: 'Logistiker' },
        { name: 'Läkare' },
        { name: 'Lärare' },
        { name: 'Operatör' },
        { name: 'Projektledare' },
        { name: 'Sjuksköterska' },
        { name: 'Tekniker' },
        { name: 'Utvecklare' }
    ];

    // Setting variables and useStates
    const [result, setResult] = useState(data2);


    //  TODO: call function to automatically create lists
    const initialJobList = ["Elektriker", "Ingenjör", "Logistiker", "Läkare", "Lärare", "Operatör", "Projektledare", "Sjuksköterska", "Tekniker", "Utvecklare"]
    const allCounties = ["Blekinge län", "Dalarnas län", "Gotlands län", "Gävleborgs län", "Hallands län", "Jämtlands län", "Jönköpings län", "Kalmar län", "Kronobergs län", "Norrbottens län", "Skåne län", "Stockholms län", "Södermanlands län", "Uppsala län", "Värmlands län", "Västerbottens län", "Västernorrlands län", "Västmanlands län", "Västra Götalands län", "Örebro län", "Östergötlands län"]

    const [job, setJob] = useState("Elektriker")
    const [joblist, setJobList] = useState(initialJobList)
    const [county, setCounty] = useState("Blekinge län")
    const [countyList, setCountyList] = useState(allCounties)
    const [graphtitle, setGraphtitle] = useState('Län')
    const [profession, setProfession] = useState('Yrke')
    const [select, setSelect] = useState(true);
    const [optionRadio, setOptionRadio] = React.useState(null);

    const handleChangeCounty = (event) => {
        setCounty(event.target.value);
    };

    const handleChangeJob = (event) => {
        setJobList(event.target.value);
    };

    const handleChangesJob = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setJobList(joblist.length === initialJobList.length ? [] : initialJobList);
            return;
        }
        setJobList(value);
        console.log(value)
    };

    const handleChangesCounty = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setCountyList(countyList.length === allCounties.length ? [] : allCounties);
            return;
        }
        setCountyList(value);
        console.log(value)
    };

    const handleParams = (event) => {
        setOptionRadio(event.target.value);
    }

    const countyListElements = allCounties.map((item) => {
        return <MenuItem value={item} key={item}>{item}</MenuItem>;
    });

    const jobListElements = initialJobList.map((item) => {
        return <MenuItem value={item} key={item}>{item}</MenuItem>;
    });


    function listToDict(list) {
        const dict = [];
        for (let i = 0; i < list.length; i++) {
            const row = list[i];
            const entry = { name: row[0] };
            for (let j = 1; j < row.length; j++) {
                const category = row[j][0];
                for (let k = 1; k < row[j].length; k++) {
                    const [subcat, value] = row[j][k];
                    let key = "";
                    if(optionRadio == "null"){
                        key = `${category}`;
                        entry[key] = subcat;
                    } else {
                        key = `${category}-${subcat}`;
                        entry[key] = value;
                    }
                    
                }
            }
            dict.push(entry);
        }
        return dict;
    }

    function dictToColumns(dict) {
        const columns = {};
        for (let i = 0; i < dict.length; i++) {
            for (const [key, _] of Object.entries(dict[i])) {
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

        setGraphtitle(countyTitle());
        
        /* TODO: Add once Klara is done with her part and the branches are merged
        if(state){ 
        setGraphtitle(countyTitle());
        } else {
            setGraphtitle(professionTitle());
        }  */

        for (let item of Object.keys(inputs)) {
            if (inputs[item].active) {
                srcs.push(item)
            }
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

    const colors = {
        "Linkedin": [
            "#1abc9c",
            "#3498db",
            "#a569bd",
            "#85c1e9",
            "#6c3483",
            "#58d68d"
        ]
        ,
        "platsbanken": [
            "#6c3483",
            "#d35400",
            "#b7950b",
            "#a04000",
            "#1e8449",
            "#2e86c1"
        ],
        "ledigajobb": [
            "#f5b7b1",
            "#f9e79f",
            "#76d7c4",
            "#a2d9ce",
            "#d0ece7",
            "#d2b4de"
        ]
    }

    const getBars = (InputColumns) => {
        const bars = [];

        const count = { Linkedin: 0, ledigajobb: 0, platsbanken: 0 };

        if (InputColumns != undefined) {
            for (const [source, col] of Object.entries(InputColumns)) {
                for (const [barName, trueValue] of Object.entries(col)) {

                    bars.push([barName, source, colors[source][count[source]]]);
                    count[source] = count[source] + 1;
                }

            }
        }
        return bars.map((bar) => <Bar dataKey={bar[0]} stackId={bar[1]} fill={bar[2]} />);
    }


    //   --------------- Handle 'Gray out' functionlity:
    //insert all default values for buttons:
    const defaultValue = {
        employment_type: true,
        seniority: true,
        years_of_experience: true,
        duration: true,
        prerequirements: true,
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

    // const getPropertyName = (obj, expression) => {
    //     var res = {};
    //     Object.keys(obj).map(k => { res[k] = () => k; });
    //     return expression(res)();
    // }

    // --------

    //Creates textshadow
    const textShadow = {
        textShadow: '2px 2px 4px #000000',
        transition: 'text-shadow 0.5s ease'
    };
    const textShadowHover = {
        textShadow: '4px 4px 8px #000000',
    };

    const standard = {
        cursor: 'default'

    };

    //County title above graph
    function countyTitle() {
       
            if (county === 'Alla valda') {
                return 'Län';
            } else {
                return county;
            }
}
/* Profession title above graph */
function professionTitle(){
    if(profession == 'Yrke'){
        return 'Yrke'
    } else {
        return profession
    }
}

    // Testing date
    const multiValue = [ {year: 2016, month: 7}, {year: 2016, month: 11}, {year: 2017, month: 3}, {year: 2019, month: 5}, ];
    let pickMulti = React.createRef();
    const pickerLang = {
        months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        from: 'From', to: 'To',
    }
    const makeText = m => {
        if (m && m.year && m.month) return (pickerLang.months[m.month-1] + '. ' + m.year)
        return '?'
    }

    return (
        <div>
            <FormLabel id='graphtitle'>
                <p>{graphtitle}</p>
            </FormLabel>

            <div className='fortableandlist'>
                <div>
                    <FormLabel component="legend"></FormLabel>
                </div>

                {/* <ResponsiveContainer > */}
                <BarChart width={1000} height={600} data={result}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" height={150} interval={0} angle={-45} textAnchor="end" />
                    <YAxis />
                    <Tooltip contentStyle={{ textShadow: '1px 1px 1px #000000' }} labelStyle={{ color: 'black' }} />
                    <Legend />
                    {getBars(dictToColumns(result))}
                </BarChart>
                {/* </ResponsiveContainer> */}

                <div className='forlist'>
                    <div >
                        {/* Div containing 3 checkboxes */}
                        <FormControl component="fieldset">
                            <FormLabel component="legend">Välj plattform:</FormLabel>
                            <FormGroup>
                                <span style={standard} onMouseOver={e => e.target.style.textShadow = '6px 6px 8px #000000'} onMouseOut={e => e.target.style.textShadow = '0px 0px 0px #000000'}>
                                    <FormControlLabel control={<Checkbox
                                        // checked={linkedinCB}
                                        onChange={handleSource}
                                        color='default'
                                        name="linkedin"
                                        value={JSON.stringify({
                                            years_of_experience: false,
                                            duration: false,
                                            prerequirements: false,
                                            drivers_license: false
                                        })}
                                    />} label="LinkedIn"/>
                                </span>
                                <span style={standard} onMouseOver={e => e.target.style.textShadow = '6px 6px 8px #000000'} onMouseOut={e => e.target.style.textShadow = '0px 0px 0px #000000'}>
                                    <FormControlLabel control={<Checkbox
                                        onChange={handleSource}
                                        color='default'
                                        name="platsbanken"
                                        value={JSON.stringify({
                                            drivers_license: false,
                                            seniority: false
                                        })}

                                    />} label="Platsbanken" />
                                </span>
                                <span style={standard} onMouseOver={e => e.target.style.textShadow = '6px 6px 8px #000000'} onMouseOut={e => e.target.style.textShadow = '0px 0px 0px #000000'}>
                                    <FormControlLabel control={<Checkbox
                                        onChange={handleSource}
                                        color='default'
                                        name="ledigajobb"
                                        value={JSON.stringify({
                                            duration: false,
                                            drivers_license: false
                                        })}
                                    />} label="Lediga jobb" />
                                </span>
                            </FormGroup>
                        </FormControl>

                           {/* Div containing 2 drop-down lists */}
                           <div>
                        <table className='toggleTable'>
                            <th align='left'>Ett län <br/>Flera yrken</th>
                            <th>
                                <label className="toggleSwitch">
                                    <input type="checkbox" onClick={() => setSelect((prev) => !prev)}/>
                                    <span class="slider"></span>
                                </label>
                            </th>
                            <th align='left' id='fyel'>Flera yrken <br/>Ett län</th>
                        </table>

                        {/* Switch state 1 */}
                        { select && <div className='County'>
                            <FormControl sx={{ m: 1, width: 200 }}>
                                <InputLabel id="demo-simple-select-autowidth-label">Län</InputLabel>
                                <Select
                                    labelId="demo-simple-select-autowidth-label"
                                    id="demo-simple-select-autowidth"
                                    value={county}
                                    onChange={handleChangeCounty}
                                    autoWidth
                                    label="Län1"
                                >
                                    {countyListElements}
                                </Select>
                            </FormControl>
                        </div> }
                        { select && <div className='Multiple Select'>
                            <FormControl sx={{ m: 1, width: 200 }}>
                                <InputLabel id="mutiple-select-autowidth-label">Yrken</InputLabel>
                                <Select
                                    labelId="mutiple-select-autowidth-label"
                                    id="multiple-select-autowidth"
                                    multiple
                                    value={joblist}
                                    onChange={handleChangesJob}
                                    renderValue={(joblist) => joblist.join(", ")}
                                    autoWidth
                                    label="Yrke1"
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
                        </div>}

                        {/* Switch state 2 */}
                        { !select && <div className='Multiple Select'>
                            <FormControl sx={{ m: 1, width: 200 }}>
                                <InputLabel id="mutiple-select-autowidth-label">Län</InputLabel>
                                <Select
                                    labelId="mutiple-select-autowidth-label"
                                    id="multiple-select-autowidth"
                                    multiple
                                    value={countyList}
                                    onChange={handleChangesCounty}
                                    renderValue={(countyList) => countyList.join(", ")}
                                    autoWidth
                                    label="Län2"
                                >
                                    <MenuItem
                                        value="all"
                                    // classes={{
                                    //     root: isAllSelected ? classes.selectedAll : ""
                                    // }}
                                    ></MenuItem>
                                    {allCounties.map((option) => (
                                        <MenuItem key={option} value={option}>
                                            <ListItemIcon>
                                                <Checkbox checked={countyList.indexOf(option) > -1} />
                                            </ListItemIcon>
                                            <ListItemText primary={option} />
                                        </MenuItem>
                                    ))}
                                </Select>
                            </FormControl>
                        </div>}

                        { !select && <div className='County'>
                            <FormControl sx={{ m: 1, width: 200 }}>
                                <InputLabel id="demo-simple-select-autowidth-label">Yrke</InputLabel>
                                <Select
                                    labelId="demo-simple-select-autowidth-label"
                                    id="demo-simple-select-autowidth"
                                    value={job}
                                    onChange={handleChangeJob}
                                    autoWidth
                                    label="Yrke2"
                                >
                                    {jobListElements}
                                </Select>
                            </FormControl>
                        </div> }

                            {<div className='Date'>
                                <FormControl sx={{ m: 1, width: 200 }}>
                                    <label><b>Pick Several Month</b><span>(Available months from Feb.2016 to Apr.2020)</span></label>
                                    <div className="edit">
                                     {/*   <Picker
                                            ref={this.pickMulti}
                                            years={{ min: { year: 2016, month: 2 }, max: { year: 2020, month: 4 } }}
                                            value={multiValue}
                                            lang={pickerLang.months}
                                            theme="dark"
                                            onChange={this.handleMultiChange}
                                            onDismiss={this.handleMultiDissmis}
                                        >
                                            <MonthBox value={multiValue.map(v => makeText(v)).join(' | ')} onClick={this.handleClickMultiBox} />
                                        </Picker>*/}
                                        
                                    </div>
                                    {/* <InputLabel id="mutiple-select-autowidth-label">Datum</InputLabel>
                                    <Select
                                        labelId="mutiple-select-autowidth-label"
                                        id="multiple-select-autowidth"
                                        multiple
                                        value={joblist}
                                        onChange={handleChanges}
                                        //renderValue={(joblist) => joblist.join(", ")}
                                        autoWidth
                                        label="Datum"
                                    >
                                        <MenuItem
                                            value="all"
                                        // classes={{
                                        //     root: isAllSelected ? classes.selectedAll : ""
                                        // }}
                                        ></MenuItem>
                                    </Select> */}
                                </FormControl>
                            </div>

                            }
                        </div>
                        <div className="radio">
                            {/* Div containing 3 horizontal radio buttons */}
                            <RadioGroup aria-label="position" name="position" defaultValue="top">
                                <FormControl component="fieldset">
                             {/*       <span onMouseOver={e => e.target.style.textShadow = '6px 6px 8px #000000'} onMouseOut={e => e.target.style.textShadow = '0px 0px 0px #000000'} className={{}}>*/}

                                        <Grid container rowSpacing={1} columnSpacing={{ xs: 1, sm: 2, md: 3 }}>
                                            <Grid item xs={6}>
                                                <FormControlLabel value="employment_type" control={<Radio size="small" />} label="Anställningsform" onChange={handleParams}
                                                    disabled={inputs.platsbanken.employment_type && inputs.linkedin.employment_type && inputs.ledigajobb.employment_type ? false : true} />
                                            </Grid>
                                            <Grid item xs={6}>
                                                <FormControlLabel value="duration" control={<Radio size="small" />} label="Varaktighet" onChange={handleParams}
                                                    disabled={inputs.platsbanken.duration && inputs.linkedin.duration && inputs.ledigajobb.duration ? false : true} />
                                            </Grid>
                                            <Grid item xs={6}>
                                                <FormControlLabel value="seniority" control={<Radio size="small" />} label="Senioritet" onChange={handleParams}
                                                    disabled={inputs.platsbanken.seniority && inputs.linkedin.seniority && inputs.ledigajobb.seniority ? false : true} />
                                            </Grid>
                                            <Grid item xs={6}>
                                                <FormControlLabel value="requirement" control={<Radio size="small" />} label="Villkor/Krav" onChange={handleParams}
                                                    disabled={inputs.platsbanken.prerequirements && inputs.linkedin.prerequirements && inputs.ledigajobb.prerequirements ? false : true} />
                                            </Grid>
                                            <Grid item xs={6}>
                                                <FormControlLabel value="years_of_experience" control={<Radio size="small" />} label="Års erfarenhet" onChange={handleParams}
                                                    disabled={inputs.platsbanken.years_of_experience && inputs.linkedin.years_of_experience && inputs.ledigajobb.years_of_experience ? false : true} />
                                            </Grid>
                                            <Grid item xs={6}>
                                                <FormControlLabel style={standard} value="null" control={<Radio size="small" />} label="Inget val" onChange={handleParams} />
                                            </Grid>
                                        </Grid>
                                 {/*</span>*/}
                                </FormControl>
                            </RadioGroup>
                        </div>
                    </div>
                    <button onClick={handleClick} className='forlistbutton'> Visa resultat</button>
                </div>
            </div>
        </div>
    );
}
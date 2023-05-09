import React, { useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
// import {} from '@material-ui/core'; //test
import { StylesProvider, makeStyles } from '@material-ui/core/styles';

import "../style.css";

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
    const allCounties = ["Alla valda", "Blekinge län", "Dalarnas län", "Gotlands län", "Gävleborgs län", "Hallands län", "Jämtlands län", "Jönköpings län", "Kalmar län", "Kronobergs län", "Norrbottens län", "Skåne län", "Stockholms län", "Södermanlands län", "Uppsala län", "Värmlands län", "Västerbottens län", "Västernorrlands län", "Västmanlands län", "Västra Götalands län", "Örebro län", "Östergötlands län"]

    const [joblist, setJobList] = useState(initialJobList)
    const [county, setCounty] = useState('Alla valda')
    const [graphtitle, setGraphtitle] = useState('Län')
    const [profession, setProfession] = useState('Yrke')

    const [optionRadio, setOptionRadio] = React.useState(null);

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

    // const myListElementJobs = joblist.map((item) => {
    //     return <MenuItem value={item} key={item}> <Checkbox checked={job.indexOf(item) > -1} /><ListItemText primary={item} /></MenuItem>
    // });

    function listToDict(list) {
        //TODO: Decide where to place the calling of groupExperience.
        //Is it supposed to be called inside listToDict or outside at the calling of listToDict.
        list = groupExperience(list);
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

    //A function that groups years of experience into intervals instead of sorting by specific
    //years. If the param is not years of experience then it returns the array unchanged. 
    function groupExperience (list){
        //Debugging. TODO Delete the two rows below.
        console.log("Group Experience: ")
        console.log(list)
        // ---------------------------------------
        if(optionRadio != "years_of_experience"){
            return list;
        }
        const group1 = []; //0-2 years of experience
        const group2 = []; //3-5 years of experience
        const group3 = []; //6-8 years of experience
        const group4 = []; //8+ years of experience
        //Starts at index 1 because the name of the source/profession is the first element
        // of the arrays.
        for(const x of list) {
            for(let i = 1; i < x.length; i++){
                const group1 = ["0-2", 0]; //0-2 years of experience
                const group2 = ["3-5", 0]; //3-5 years of experience
                const group3 = ["6-8", 0]; //6-8 years of experience
                const group4 = ["8+", 0]; //8+ years of experience
                for(let y = 1; y < x[i].length; y++){
                    //Here, finally, we are inside results
                    const elem = (x[i])[y];
                    const label = elem[0]
                    if(label <= 2){
                       group1[1] += elem[1]; 
                    } else if (label <= 5){
                        group2[1] += elem[1];
                    } else if (label <= 8){
                        group3[1] += elem[1];
                    } else if (label > 8){
                        group4[1] += elem[1];
                    }
                }
                x[i] = [(x[i])[0], group1, group2, group3, group4];
            }
        }
        return list;
        /* for (let i = 0; i < list.length; i++) {
            
            const element = list[i]
            //const year = list[[][][][i]];
            switch(year) {
                case (year[i] < 2):
                    group1[i]=list[i];
                case (year < 5):
                    group2.push(list[i])

                case(year < 8):
                group3.push(i)
            }
            if (year < 2) {
                group[i]=list[i];
            } else if( year < 5){

            } 

        } */
        
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
            .then(response => setResult(listToDict(response.data.number))) /* Returned extract info from fortabletest */
            .catch(error => console.log(error));

        console.log((result));
    };

    const handleChanges = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setJobList(joblist.length === initialJobList.length ? [] : initialJobList);
            return;
        }
        setJobList(value);
        console.log(value)
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

    const getPropertyName = (obj, expression) => {
        var res = {};
        Object.keys(obj).map(k => { res[k] = () => k; });
        return expression(res)();
    }

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
    let changeSelect = true;
    let changeTitle = false;



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
                            {changeSelect && <div className='County'>
                                <FormControl sx={{ m: 1, width: 200 }}>
                                    <InputLabel id="demo-simple-select-autowidth-label">Län</InputLabel>
                                    <Select
                                        labelId="demo-simple-select-autowidth-label"
                                        id="demo-simple-select-autowidth"
                                        value={county}
                                        onChange={handleChangeCounty}
                                        autoWidth
                                        label="Län"
                                    >
                                        {myListElements}
                                    </Select>
                                </FormControl>
                            </div>}

                            {changeSelect && <div className='Multiple Select'>
                                <FormControl sx={{ m: 1, width: 200 }}>
                                    <InputLabel id="mutiple-select-autowidth-label">Yrken</InputLabel>
                                    <Select
                                        labelId="mutiple-select-autowidth-label"
                                        id="multiple-select-autowidth"
                                        multiple
                                        value={joblist}
                                        onChange={handleChanges}
                                        renderValue={(joblist) => joblist.join(", ")}
                                        autoWidth
                                        label="Yrken"
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

                            {changeSelect && <div className='Date'>
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
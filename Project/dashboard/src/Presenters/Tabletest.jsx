import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
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
    const data = [
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

    //Colors for the different sources
    const colors = {
        "linkedin": [
            // green
            "#A2D9CE",
            "#73C6B6",
            "#45B39D",
            "#16A085",
            "#117A65",
            "#0E6655"
        ],

        "platsbanken": [
            // orange
            "#F0B27A",
            "#EB984E",
            "#E67E22",
            "#CA6F1E",
            "#AF601A",
            "#935116"
        ],

        "ledigajobb": [
            // purple
            "#D7BDE2",
            "#C39BD3",
            "#AF7AC5",
            "#9B59B6",
            "#76448A",
            "#512E5F"
        ]
    }

    // Specifes the first month were data was gathered:
    const startDate = 'May 2023';
    const thisMonth = new Date().getMonth() + 1;
    const checkToday = new Date().getFullYear() + '-' + (thisMonth < 10 ? '0' + thisMonth : thisMonth);

    // Setting variables and useStates
    const [result, setResult] = useState(data);

    const seniorityNull = "ej applicerbart";
    const employmentNull = "ospecifierat";
    const reqNull = "ospecifierat";


    /**
     * Every entry in this list should have the first letters of each word capitalized
     */
    const initialJobList = ["Elektriker", "Ingenjör", "Logistiker", "Läkare", "Lärare", "Operatör", "Projektledare", "Sjuksköterska", "Tekniker", "Utvecklare"]
    /**
     * Every entry in this list should have the first letters of each word capitalized
     */
    const allCounties = ["Blekinge Län", "Dalarnas Län", "Gotlands Län", "Gävleborgs Län", "Hallands Län", "Jämtlands Län", "Jönköpings Län", "Kalmar Län", "Kronobergs Län", "Norrbottens Län", "Skåne Län", "Stockholms Län", "Södermanlands Län", "Uppsala Län", "Värmlands Län", "Västerbottens Län", "Västernorrlands Län", "Västmanlands Län", "Västra Götalands Län", "Örebro Län", "Östergötlands Län"]

    //insert all default values for filtering buttons:
    const defaultValue = {
        employment_type: true,
        seniority: true,
        years_of_experience: true,
        duration: true,
        prerequirements: true,
        active: false
    };


    //insert all sources. Format 'sourcename' (lowercase): defaultValue
    const [inputs, setInputs] = useState({ platsbanken: defaultValue, linkedin: defaultValue, ledigajobb: defaultValue });


    const [job, setJob] = useState("Sjuksköterska")
    const [joblist, setJobList] = useState(initialJobList)
    const [county, setCounty] = useState("Blekinge Län")
    const [countyList, setCountyList] = useState(allCounties)
    const [graphtitle, setGraphtitle] = useState("Blekinge Län")
    const [select, setSelect] = useState(true);
    const [date, setDate] = useState(checkToday);
    const [optionRadio, setOptionRadio] = useState("null");
    const [selectRadio, setSelectRadio] = useState(false);
    const [foundData, setFoundData] = useState(true);

    /**
     * Used to change which county is selected, used for "one county, many jobs" scenario.
     * @param {onChange} event 
     */
    const handleChangeCounty = (event) => {
        setCounty(event.target.value);
    };

    /**
     * Used to change which job is selected, used for "many counties, one job" scenario.
     * @param {onChange} event 
     */
    const handleChangeJob = (event) => {
        setJob(event.target.value);
    };

    /**
     * Used to change which jobs are selected, used for "one county, many jobs" scenario.
     * @param {onChange} event 
     */
    const handleChangesJob = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setJobList(joblist.length === initialJobList.length ? [] : initialJobList);
            return;
        }
        setJobList(value);
        // console.log(value)
    };

    /**
     * Used to change which counties are selected, used for "many counties, one job" scenario.
     * @param {onChange} event 
     */
    const handleChangesCounty = (event) => {
        const value = event.target.value;
        if (value[value.length - 1] === "all") {
            setCountyList(countyList.length === allCounties.length ? [] : allCounties);
            return;
        }
        setCountyList(value);
        // console.log(value)
    };

    /**
     * Changes the selected parameter for filtering
     * @param {onChange} event 
     */
    const handleParams = (event) => {
        setOptionRadio(event.target.value);
    }

    /**
     * Changes the selected date for filtering
     * @param {onChange} event 
     */
    const handleDate = (event) => {
        setDate(event.target.value);
    }

    //Creates the select lists
    const countyListElements = allCounties.map((item) => {
        return <MenuItem value={item} key={item}>{item}</MenuItem>;
    });

    const jobListElements = initialJobList.map((item) => {
        return <MenuItem value={item} key={item}>{item}</MenuItem>;
    });


    /**
     * Converts the data from the database into the correct format for the graph
     * @param {[[name:string, [source:string, [param:string, count:int], ...[]], ...[]], ...[]]} list
     */
    function listToDict(list) {
        console.log(list)
        list = groupExperience(list);
        const dict = [];
        if (list.length === 0){
            setGraphtitle("Ingen tillgänglig data");
        } else if (select) {
            setGraphtitle(countyTitle());
        } else {
            setGraphtitle(jobTitle());
        }

        for (let i = 0; i < list.length; i++) {
            const row = list[i];
            var partStr = row[0].toLowerCase().split(' ');
            for (let i = 0; i < partStr.length; i++) {
                partStr[i] = partStr[i].charAt(0).toUpperCase() + partStr[i].substring(1);
            }
            const entry = { name: partStr.join(' ') };
            for (let j = 1; j < row.length; j++) {
                const category = row[j][0];
                for (let k = 1; k < row[j].length; k++) {
                    const [subcat, value] = row[j][k];
                    let key = "";
                    if (optionRadio === "null") {
                        key = `${category}`;
                        entry[key] = subcat;
                    } else {
                        if (subcat === "null") {
                            switch (optionRadio) {
                                case "seniority":
                                    key = `${category}-${seniorityNull}`;
                                    break;
                                case "employment_type":
                                    key = `${category}-${employmentNull}`;
                                    break;
                                case "requirement":
                                    key = `${category}-${reqNull}`;
                                    break;
                                default:
                                    key = `${category}-${subcat}`;
                                    break;
                            }
                        } else {
                            key = `${category}-${subcat}`;
                        }
                        entry[key] = value;
                    }
                }
            }
            dict.push(entry);
        }
        return dict;
    }

    /**
     * Takes the output from listToDict() and returns a list of all columns needed to display that data
     * @param {*} dict 
     * @returns list of columns
     */
    function dictToColumns(dict) {
        const columns = {};
        for (let i = 0; i < dict.length; i++) {
            for (const [key] of Object.entries(dict[i])) {
                const parts = key.split("-");
                if (parts[0] !== "name") {
                    if (!(parts[0] in columns)) {
                        columns[parts[0]] = {};
                    }
                    columns[parts[0]][key] = true;
                }

            }
        }
        return columns;
    }
    /**
     * A function that groups years of experience into intervals instead of sorting by specific
     * years. If the param is not years of experience then it returns the array unchanged. 
     */
    function groupExperience(list) {
        if (optionRadio !== "years_of_experience") {
            return list;
        }
        //Starts at index 1 because the name of the source/profession is the first element
        // of the arrays.
        for (const x of list) {
            for (let i = 1; i < x.length; i++) {
                const group0 = ["Ingen erfarenhet", 0]; //0 years of experience
                const group1 = ["1-2", 0]; //1-2 years of experience
                const group2 = ["3-5", 0]; //3-5 years of experience
                const group3 = ["6-8", 0]; //6-8 years of experience
                const group4 = ["8+", 0]; //8+ years of experience
                for (let y = 1; y < x[i].length; y++) {
                    //Here, finally, we are inside results
                    const elem = (x[i])[y];
                    const label = elem[0]
                    if (label === 0) {
                        group0[1] += elem[1];
                    } else if (label <= 2) {
                        group1[1] += elem[1];
                    } else if (label <= 5) {
                        group2[1] += elem[1];
                    } else if (label <= 8) {
                        group3[1] += elem[1];
                    } else if (label > 8) {
                        group4[1] += elem[1];
                    }
                }
                x[i] = [(x[i])[0], group0, group1, group2, group3, group4];
            }
        }
        return list;
    }

    /**
     * Function for requesting data from the database, takes the selected paramaters and sets the result of the query.
     */
    const handleClick = () => {
        const srcs = []
        if(!foundData){
            console.log("Ingen tillgänglig data!")
            setGraphtitle("Ingen tillgänglig data");
        } else if (select) {
            setGraphtitle(countyTitle());
        } else {
            setGraphtitle(jobTitle());
        }

        for (let item of Object.keys(inputs)) {
            if (inputs[item].active) {
                srcs.push(item)
            }
        }

        const queryTbs = []
        queryTbs.push(srcs)
        if (select) {
            queryTbs.push(county.toLowerCase())
            queryTbs.push(joblist.map(word => word.toLowerCase()));
        }
        else {
            queryTbs.push(countyList.map(word => word.toLowerCase()));
            queryTbs.push(job.toLowerCase())
        }
        queryTbs.push(optionRadio)
        queryTbs.push(date)
        console.log(queryTbs)
        axios.post('http://localhost:8888/why', { job: queryTbs })
            .then(response => setResult(listToDict(response.data.number))) /* Returned extract info from fortabletest */
            .catch(error => console.log(error));

        console.log((result));
    };

    useEffect(() => {
        handleClick()
    }, [select]);


    /**
     * Takes the result list and adds missing empty data fields
     * @param {*} resultChange 
     * @returns list of data
     */
    function displayAll(resultChange) {

        let compare = (select ? joblist.slice() : countyList.slice());

        for (let index = 0; index < resultChange.length; index++) {
            const element = resultChange[index];
            const compareIndex = compare.indexOf(element.name);
            compare.splice(compareIndex, 1);
        }
        for (let index = 0; index < compare.length; index++) {

            resultChange.push({ name: compare[index] })
        }

        resultChange = resultChange.sort(function (a, b) {
            return (a.name < b.name) ? -1 : (a.name > b.name) ? 1 : 0;
        });

        return resultChange;
    }

    /**
     * Takes the return list from dictToColumns() and supplements columns if data was not found.
     * @param {*} InputColumns 
     * @returns List of all columns that should have a place in the chart
     */
    const getBars = (InputColumns) => {
        const bars = [];

        const count = { linkedin: 0, ledigajobb: 0, platsbanken: 0 };

        if (InputColumns !== undefined) {
            for (const [source, col] of Object.entries(InputColumns)) {
                for (const [barName] of Object.entries(col)) {

                    bars.push([barName, source, colors[source][count[source]]]);
                    count[source] = count[source] + 1;
                }

            }
        }
        return bars.map((bar) => <Bar dataKey={bar[0]} stackId={bar[1]} fill={bar[2]} />);
    }

    /**
     * Handles any changes to the source buttons
     * @param {*} event 
     */
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
    }

    /**
     * Parses the input paramater into correct format for "handleKeys()"
     * @param {*} s 
     * @returns 
     */
    const splitKey = (s) => {
        const returnKeyValue = {};
        var x = s.replace(/[{}"']+/g, '').split(',');
        for (var i = 0; i < x.length; i++) {
            var split = x[i].split(':');
            returnKeyValue[split[0].trim()] = (split[1].trim() === 'true');
        }

        return returnKeyValue;
    }

    /**
     * Creates a key-value list filled with all changed and unchanged values for "inputs"
     * @param {*} value 
     * @returns 
     */
    const handleKeys = (value) => {
        const template = { ...defaultValue };
        for (let item of Object.keys(value)) {
            template[item] = value[item];
        }
        template.active = true;
        return template;
    }

    // --------
    /**
     * County title above graph
     * @returns county
     */
    function countyTitle() {
        return county;
    }

    /**
     * Profession title above graph
     * @returns profession
     */
    function jobTitle() {
        return job;
    }

    /**
     * Get all months from startDate to today
     * @returns a list of html options
     */
    function getMonths() {
        var totalMonths = {};
        const startPoint = new Date(new Date().getFullYear(), new Date().getMonth(), 1);
        const endPoint = new Date(startDate.replace(" ", " ,1 "));
        while (endPoint <= startPoint) {
            let currentYear = startPoint.getFullYear();
            let months = [];

            while (startPoint.getFullYear() === currentYear && endPoint <= startPoint) {
                let currentMonth = startPoint.getMonth() + 1;
                if (currentMonth < 10) {
                    currentMonth = '0' + currentMonth;
                }
                months.push([currentYear + '-' + currentMonth, startPoint.toLocaleString('sv-SE', { month: 'long' })]);
                startPoint.setMonth(startPoint.getMonth() - 1);
            }
            totalMonths[currentYear] = months;
        }
        const returnList = [];
        for (var year_value in totalMonths) {
            returnList.push([year_value, totalMonths[year_value]])
        }

        returnList.sort(function (a, b) { return b[0].localeCompare(a[0]); });

        return returnList.map((item) => (
            <optgroup label={item[0]}>
                {item[1].map((m =>
                    <option value={m[0]}>{m[1]}</option>
                ))
                }
            </optgroup>));
    }


    return (
        <div>
            <div className='fortableandlist'>
                <div className='flex-row'>

                    
                        <FormLabel id='graphtitle'>
                            <p>{graphtitle}</p>
                        </FormLabel>
                    
                    <div>
                        <div className='tableandtitle'>
                            {/* <p id="nodatalabel"> Ingen data tillgänglig </p> */}
                            {/* <div>
                                <FormLabel component="legend"></FormLabel>
                            </div> */}

                            {/* <ResponsiveContainer > */}
                            <BarChart width={1000} height={600} data={displayAll(result)}>
                                <CartesianGrid strokeDasharray="3 3" />
                                <XAxis  tick={{ fontSize: '0.9em' }} dataKey="name" height={150} interval={0} angle={-45} textAnchor="end" />
                                <YAxis />
                                <Tooltip contentStyle={{ textShadow: '1px 1px 1px #000000' }} labelStyle={{ color: 'black' , textShadow: '0px 0px 0px #000000'}} />
                                <Legend />
                                {getBars(dictToColumns(result))}
                            </BarChart>
                    </div>
                    {/* </ResponsiveContainer> */}
                </div>
            </div>

                <div className='forlist'>
                    <div className="questionmark-container">
                        <div className="hover-element">
                            !
                            <div class="warning-text">Hemsidan avstår från allt ansvar relaterat till felaktiga data analyser.</div>
                           {/* <div class="warning-text">Sanningsavvikande data kan bero på urval av annonser</div>*/}
                        </div>
                    </div>
                    <div >
                        {/* Div containing 3 checkboxes */}
                        <FormControl component="fieldset" defaultValue={"linkedin"}>
                            <FormLabel component="legend">Välj plattform:</FormLabel>
                            <FormGroup>
                                <FormControlLabel control={<Checkbox
                                    // checked={linkedinCB}
                                    onChange={handleSource}
                                    color='default'
                                    name="linkedin"
                                    value={JSON.stringify({
                                        years_of_experience: false,
                                        duration: false,
                                    })}
                                />} label="LinkedIn" />
                                <FormControlLabel control={<Checkbox
                                    onChange={handleSource}
                                    color='default'
                                    name="platsbanken"
                                    value={JSON.stringify({
                                        seniority: false
                                    })}

                                />} label="Platsbanken" />
                                <FormControlLabel control={<Checkbox
                                    onChange={handleSource}
                                    color='default'
                                    name="ledigajobb"
                                    value={JSON.stringify({
                                        duration: false
                                    })}
                                />} label="Lediga jobb" />
                            </FormGroup>
                        </FormControl>

                        {/* Div containing 2 drop-down lists */}
                        <div>
                            <table className='toggleTable'>
                                <th align='left' width="75px">Ett län <br />Flera yrken</th>
                                <th align='left' width="60px">
                                    <label className="toggleSwitch" id="sc">
                                        <input type="checkbox" onClick={() => setSelect((prev) => !prev)} />
                                        <span className="slider"></span>
                                    </label>
                                </th>
                                <th align='left' width="75px">Flera län <br />Ett yrke</th>
                            </table>

                            {/* Switch state 1 */}
                            {select && <div className='County'>
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
                            </div>}
                            {select && <div className='Multiple Select'>
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
                            {!select && <div className='Multiple Select'>
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

                            {!select && <div className='County'>
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
                            </div>}

                            {<div className='Date'>
                                <FormControl sx={{ m: 1, width: 200 }}>
                                    <InputLabel htmlFor="grouped-date">Datum</InputLabel>
                                    <Select
                                        native defaultValue={checkToday}
                                        id="grouped-date"
                                        label="Datum"
                                        onChange={handleDate}>
                                        {getMonths()}
                                    </Select>
                                </FormControl>
                            </div>

                            }
                        </div>
                        <table className='toggleTable'>
                            <th align='left' width="75px">Filtrera val</th>
                            <th align='left' width="60px">
                                <label className="toggleSwitch">
                                    <input type="checkbox" value="null" onClick={() => setSelectRadio((prev) => !prev)} onChange={handleParams} />
                                    <span className="slider"></span>
                                </label>
                            </th>
                            <th align='left' width="75px"></th>
                        </table>

                        {selectRadio && <div className="radio">
                            {/* Div containing 3 horizontal radio buttons */}
                            <RadioGroup aria-label="position" name="position" defaultValue="top">
                                <FormControl component="fieldset">
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
                                            <FormControlLabel value="requirement" control={<Radio size="small" />} label="Utbildning" onChange={handleParams}
                                                disabled={inputs.platsbanken.prerequirements && inputs.linkedin.prerequirements && inputs.ledigajobb.prerequirements ? false : true} />
                                        </Grid>
                                        <Grid item xs={6}>
                                            <FormControlLabel value="years_of_experience" control={<Radio size="small" />} label="Erfarenhet (år)" onChange={handleParams}
                                                disabled={inputs.platsbanken.years_of_experience && inputs.linkedin.years_of_experience && inputs.ledigajobb.years_of_experience ? false : true} />
                                        </Grid>
                                        {/* <Grid item xs={6}>
                                            <FormControlLabel style={standard} value="null" control={<Radio size="small" />} label="Inget val" onChange={handleParams} />
                                        </Grid> */}
                                    </Grid>
                                </FormControl>
                            </RadioGroup>
                        </div>}
                    </div>
                    <button onClick={handleClick} className='forlistbutton'> Visa resultat</button>
                </div>
            </div>
        </div>
    );
}
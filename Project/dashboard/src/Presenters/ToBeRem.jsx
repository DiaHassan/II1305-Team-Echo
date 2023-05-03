import React, { useRef, useState } from "react";
// import {FormControl,InputLabel,Select,MenuItem} from '@material-ui/';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';


export default function Toberem() {
    const [age,setAge] = useState(10)
    const tempref = useRef(null)
    const handleChange = (event) => {
        setAge(event.target.value);
    }
  return (
    <>
      <div>
      <FormControl fullWidth ref={tempref}>
        <InputLabel id="demo-simple-select-label">Age</InputLabel>
        <Select
            ref={tempref}
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={age}
            label="Age"
            onChange={handleChange}
        >
            <MenuItem value={10} ref={tempref}>Ten</MenuItem>
            <MenuItem value={20} ref={tempref}>Twenty</MenuItem>
            <MenuItem value={30} ref={tempref}>Thirty</MenuItem>
        </Select>
        </FormControl>
      </div>

    </>
  )
}
import * as React from "react";
import { useId, useState } from "react";
// import Navbar from "./navbar";
// import Footer from "./footer";
import "../style.css";



/*
Notes for future:

To add another parameter:
    - Add ['param name': true] to defaultValue

To add another Source:
    - Add ['source name': defaultValue] to use state

To configure a source:
    - Add [name='source name']
    - Add [value={JSON.stringify({'param name 1': false, 'param name 2': false, ...})}]
    - Add [onChange={handleSource}]
    - To the button you wish to configure. 
    - You only need to put params you want to set as false into the value field.
*/



export default function Sandbox(props) {

    //insert all default values for buttons:
    const defaultValue = {
        county: true,
        seniority: true,
        job: true
    };

    //insert all sources. Format 'sourcename': defaultValue
    const [inputs, setInputs] = useState({ src1: defaultValue, src2: defaultValue });

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
        // console.log(inputs);
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
        return template;
    }

    const handleSubmit = (event) => {

    }

    return (
        <>
            <form onSubmit={handleSubmit}>
                <label>
                    <input
                        type="checkbox"
                        name="src1"
                        value={JSON.stringify({
                            job: false
                        })}
                        onChange={handleSource}
                    />
                    110
                </label>
                <label>
                    <input
                        type="checkbox"
                        name="src2"
                        value={JSON.stringify({
                            seniority: false
                        })}
                        onChange={handleSource}
                    />
                    101
                </label>
                <input type="submit" />
            </form>


            <p>{inputs.src1.county && inputs.src1.county ? '+' : '-'} county</p>
            <p>{inputs.src1.seniority && inputs.src2.seniority ? '+' : '-'} Seniority</p>
            <p>{inputs.src1.job && inputs.src2.job ? '+' : '-'} Job</p>

        </>
    )


}
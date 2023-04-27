import React, { useState } from 'react';
import axios from 'axios';

export default function Tabletest() {

    const [result, setResult] = useState(null);
    const [job, setJob] = useState('')


    const handleChange = (event) => {
        setJob(event.target.value);
    }

    const handleClick = () => {
      axios.post('http://localhost:5000/why',{job:job})
        .then(response => setResult(response.data.number))
        .catch(error => console.log(error));
    };

    return (
        <div>
            <form onSubmit={handleClick}>
                <label>
                    Select an option:
                    <select value={job} onChange={handleChange}>
                    <option value="">Choose an option</option>
                    <option value="Kock">Kock</option>
                    <option value="Städare">Städare</option>
                    <option value="Utvecklare">Utvecklare</option>
                    </select>
                </label>
                {/* <button type="submit">Run Python function</button> */}
            </form>
            <button onClick={handleClick}>Run Python function</button>
            {result && <p>Result: {result}</p>}
            {/* {console.log(result)} */}
        </div>
    );
}
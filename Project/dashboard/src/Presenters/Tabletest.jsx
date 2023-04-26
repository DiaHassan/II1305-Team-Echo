import React, { useState } from 'react';
import axios from 'axios';

export default function Tabletest() {

    const [result, setResult] = useState(null);

    const handleClick = () => {
      axios.post('http://localhost:5000/why',{nb:3})
        .then(response => setResult(response.data.number))
        .catch(error => console.log(error));
    };

    return (
        <div>
            <button onClick={handleClick}>Run Python function</button>
            {result && <p>Result: {result}</p>}
            {/* {console.log(result)} */}
        </div>
    );
}
import { FormControlLabel } from '@material-ui/core';
import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';


function Chart({ xAxisName, yAxisName, chartData }) {
  return (
    <FormControl component="fieldset">
    <FormLabel component="legend">län</FormLabel>
    <LineChart width={600} height={300} data={chartData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
      <XAxis dataKey="name" label={{ value: xAxisName, position: 'insideBottomRight', dy: 10 }} />
      <YAxis label={{ value: yAxisName, angle: -90, position: 'insideLeft' }} />
      <CartesianGrid strokeDasharray="3 3" />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="value" stroke="#8884d8" activeDot={{ r: 8 }} />
    </LineChart>
</FormControl> 
  );
}

export default Chart;

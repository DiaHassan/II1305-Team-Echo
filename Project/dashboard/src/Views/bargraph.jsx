import React from 'react';
import './rotate.css';

function BarGraph({ xAxisLabel, yAxisLabel, data }) {
    // get maximum data point to calculate the scale of the graph


    let values = Array(data.length).fill(0);
    let labels = Array(data.length).fill("null");

    console.log(data)

    for (let i = 0; i < data.length; i++) {
        console.log(data[i])
        console.log(data[i]['value'])
    values[i] = (data[i])['value']
    console.log("values: " + values[i])
    }
    for (let i = 0; i < data.length; i++) {
        console.log(data[i])
        console.log(data[i]['label'])
    labels[i] = (data[i])['label']
    console.log("labels: " + labels[i])
    }

    const maxDataPoint = Math.max(...values);
    console.log(values)
  console.log("maxDatapoint: " + maxDataPoint)


  return (
    <div>
      <h2>{xAxisLabel} vs {yAxisLabel}</h2>
      <svg width="400" height="300">
        {/* draw x-axis */}
        <line x1="50" y1="250" x2="350" y2="250" stroke="black" strokeWidth="2" />
        {/* draw y-axis */}
        <line x1="50" y1="250" x2="50" y2="50" stroke="black" strokeWidth="2" />
        {/* draw x-axis label */}
        <text x="200" y="290" textAnchor="middle">{xAxisLabel}</text>
        {/* draw y-axis label */}
        <text x="20" y="150" textAnchor="middle" transform="rotate(-90, 20, 150)">{yAxisLabel}</text>
        {/* draw bars */}
        <rect x = {0} y = {0} width ="40" height = "100" fill = "red"/>
        console.log(data);
        {data.map((dataPoint, index) => (
          <rect
            x={50 + (index * 50)}
            y={250 - (dataPoint['value'] / maxDataPoint) * 200}
            width="40"
            height={(dataPoint['value'] / maxDataPoint) * 200}
            fill="blue"
          />
        ))}
        {data.map((dataPoint, index) => (

          <text x={90 + (index *50)} y="260" textAnchor="end" transform="rotate(-45,90,260)">{dataPoint['label']}</text>
        ))}
      {data.map((dataPoint, index) => (
        console.log(dataPoint['value'])
      ))
      }
      </svg>
    </div>
  );
}
//</div><text x={90 + (index *50)} y="260" textAnchor="end" transform="rotate(-45, " + (50 + (index *50)) + ", " + (260) + ")">{dataPoint['label']}</text>
export default BarGraph;


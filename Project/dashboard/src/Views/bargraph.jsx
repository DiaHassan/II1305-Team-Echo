import React from 'react';
import { Color } from 'three';

function BarGraph({ xAxisLabel, yAxisLabel, data, width, height}) {
    // get maximum data point to calculate the scale of the graph
    let values = Array(data.length).fill(0);
    let labels = Array(data.length).fill("null");
    let x1 = `${width*0.025}`
    let x2 = `${width*0.9}`
    let x3 = `${width*0.95}`
    let y1 = `${height*0.1}`
    let y2 = `${height*0.8}`
    let y3 = `${height*0.805}`
    let bargap = `${width*0.04}`
    let barwidth = `${width*0.025}`
    let labely = `${height*0.82}`
    

    console.log(data)

    for (let i = 0; i < data.length; i++) {
        console.log(data[i])
        console.log(data[i][1])
    values[i] = (data[i])[1]
    console.log("values: " + values[i])
    }
    for (let i = 0; i < data.length; i++) {
        console.log(data[i])
        console.log(data[i][0])
    labels[i] = (data[i])[0]
    console.log("labels: " + labels[i])
    }

    const maxDataPoint = Math.max(...values);
    console.log(values)
  console.log("maxDatapoint: " + maxDataPoint)


  return (
    <div>
      <h2>{xAxisLabel} vs {yAxisLabel}</h2>
      
     {/* by = parseInt(y1) {/* string to int 

      bar_refx= //width
      
      width = widthx.toString(); {/* int to string 
      const variablenamn = 
      <svg width={`${variablenamn}`} height="1000">*/}

      {/* building the coordinate-system*/}
      <svg width={`${width}`} height={`${height}`}>
        {/* draw x-axis */}
        <line x1={`${x1}`} y1={`${height*0.8}`} x2={`${x2}`} y2={`${height*0.8}`} stroke="black" strokeWidth="2" />
        {/* draw y-axis */}
        <line x1={`${x1}`} y1={`${height*0.8}`} x2={`${x1}`} y2={`${height*0.1}`} stroke="black" strokeWidth="2" />
        {/* draw x-axis label */}
        <text x={`${x2*1.05}`} y={`${height*0.805}`} textAnchor="middle">{xAxisLabel}</text>
        {/* draw y-axis label */}
        <text x={`${x1}`} y={`${width*0.05}`} textAnchor="middle">{yAxisLabel}</text>

        {/* draw bars */}
        console.log(data);
        {data.map((dataPoint, index) => (
          <rect
            x={width*0.025 + (index * bargap)}
            y={height*0.8 - (dataPoint[1] / maxDataPoint) * (y2-y1)}
            width="20"
            height={(dataPoint[1] / maxDataPoint) * (y2-y1)}
            fill="blue"
          />
        ))}
    
        {data.map((dataPoint, index) => (
          <text x={width*0.05 + (index * width*0.04)} y={labely} textAnchor="end" transform={`rotate(-45, ${width*0.05 + (index * width*0.04)}, ${labely})`}>{dataPoint[0]}</text>
        ))}
      {data.map((dataPoint, index) => (
        console.log(dataPoint[0])
      ))
      }

      {/* Draw "milestones" */}
      
      {Array.from({ length: 11 }).map((_, index) => (
          <text
            key={index}
            x={x1-5}
            y={y2 - ((y2-y1)/10 * index)}
            textAnchor="end"
            dominantBaseline="middle"
          >
            {((maxDataPoint / 10) * index).toFixed(0)}
          </text>
        ))}
      

      </svg>
    </div>
  );
}
//</div><text x={90 + (index *50)} y="260" textAnchor="end" transform="rotate(-45, " + (50 + (index *50)) + ", " + (260) + ")">{dataPoint['label']}</text>
export default BarGraph;


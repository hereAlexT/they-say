import React from 'react';
import ReactWordcloud from 'react-wordcloud';
import Button from '@mui/material/Button';

import 'tippy.js/dist/tippy.css';
import 'tippy.js/animations/scale.css';

const words = [
    {
        text: 'told',
        value: 64,
    },
    {
        text: 'mistake',
        value: 11,
    },
    {
        text: 'thought',
        value: 16,
    },
    {
        text: 'bad',
        value: 17,
    },
]

interface Data {
    text: string;
    value: number;
}

function createData(
    text: string,
    value: number,
): Data {
    return { text, value };
}

/* only support for text word now 22/09/22*/
export default function SimpleWordcloud(props: { data: any }) {

    // console.log(props.data)
    let w_array_format = []
    let w_array = props.data.word.slice(0, 200);
    for (var i = 0; i < w_array.length; i++) {
        w_array_format.push(createData(w_array[i][0], w_array[i][1]))
    }
    // console.log(w_array_format)

    const options: any = {
        colors: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"],
        enableTooltip: true,
        deterministic: false,
        fontFamily: "impact",
        fontSizes: [5, 60],
        fontStyle: "normal",
        fontWeight: "normal",
        padding: 1,
        rotations: 3,
        rotationAngles: [0, 90],
        scale: "sqrt",
        spiral: "archimedean",
        transitionDuration: 1000
    };

    const maxWords = 200

    return <div>
        <ReactWordcloud
            words={w_array_format}
            options={options}
            maxWords={maxWords} />


    </div>

}
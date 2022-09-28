import * as React from 'react';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Autocomplete from '@mui/material/Autocomplete';
import DataPicker from './DataPicker'
import { useState, useEffect } from 'react'
import axios from 'axios'
import MaterialUIPickers from './DataPicker';
import Grid from '@mui/material/Unstable_Grid2';
import Button from '@mui/material/Button';


export type search_keywords_type = {
    "keywords": string,
    "starttime": string,
    "endtime": string
}



export default function FreeSolo(props: any) {
    const [search_box_content, set_search_box_content] = useState(
        [{
            "username": "Loading",
            "id": -1,
            "name": "Loading"
        }]
    )
    const [search_keywords, set_search_keywords] = useState<search_keywords_type>({ keywords: "", starttime: "", endtime: "" })

    const get_search_auto_complete_data = { "arg": "get_search_auto_complete" }

    useEffect(() => {
        axios.post('https://api.theysay.tech/basic',
            get_search_auto_complete_data)
            .then(res => {
                set_search_box_content(res['data']['data']);
            })
            .catch(err => console.log(err))
    }, [])

    function startTimeHandler(isotime: string) {
        set_search_keywords({ ...search_keywords, starttime: isotime })
        console.log(search_keywords)

    }
    function endTimeHandler(isotime: string) {
        set_search_keywords({ ...search_keywords, endtime: isotime })
        console.log(search_keywords)

    }

    function searchButtonOnClick() {
        props.searchHandler(search_keywords)
    }


    return (
        <>
            <Autocomplete
                freeSolo
                id="free-solo-2-demo"
                disableClearable
                options={search_box_content.map(res => res['username'])}
                onChange={(e: any, v: string) => {set_search_keywords({ ...search_keywords, keywords: v });}}
                renderInput={(params) => (
                    <TextField
                        {...params}
                        label="Search input"
                        InputProps={{
                            ...params.InputProps,
                            type: 'search',
                        }}
                    />
                )}
            />
            <Grid container spacing={6}>
                <Grid>
                    <MaterialUIPickers title="Start Time" callback={startTimeHandler} />
                </Grid>
                <Grid>
                    <MaterialUIPickers title="End Time" callback={endTimeHandler} />
                </Grid>
                <Grid>

                    <Button variant="contained" onClick={searchButtonOnClick}>Search</Button>

                </Grid>
            </Grid>
        </>




    );
}

import * as React from 'react';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Autocomplete from '@mui/material/Autocomplete';


import { useState, useEffect } from 'react'
import axios from 'axios'


export default function FreeSolo() {

    const [search_box_content, set_search_box_content] = useState(
        [{
            "username": "Loading",
            "id": -1,
            "name": "Loading"
        }]
    )
    const [search_words, set_search_words] = useState()

    const get_search_auto_complete_data = { "arg": "get_search_auto_complete" }

    useEffect(() => {
        axios.post('http://127.0.0.1:5000/api/basic',
            get_search_auto_complete_data)
            .then(res => {
                set_search_box_content(res['data']['data']);
            })
            .catch(err => console.log(err))
    }, [])


    function onChangeHandler(e, newValue) {
        console.log(newValue)
        /* search on the API */
    }


    return (
        <Stack spacing={2} sx={{ width: 300 }}>
            <Autocomplete
                freeSolo
                id="free-solo-2-demo"
                disableClearable
                options={search_box_content.map(res => res['username'])}
                onChange={onChangeHandler}
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
        </Stack>
    );
}



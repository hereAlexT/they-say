import * as React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { useState, useEffect } from 'react'
import axios from 'axios'
import MaterialUIPickers from './DataPicker';
import Grid from '@mui/material/Unstable_Grid2';
import Button from '@mui/material/Button';
import { WordFreqRequestType } from '../..//Funs/GetWordFreq';





export default function FreeSolo(props: { callback: Function }) {
    const [search_box_content, set_search_box_content] = useState(
        [{
            "username": "Loading",
            "id": -1,
            "name": "Loading"
        }]
    )

    const [SearchKeyWords, setSearchKeyWords] = useState<WordFreqRequestType>({
        screen_name: "",
        start_time: "2010-09-28T08:27:35.000Z",
        end_time: "2022-09-28T08:27:35.000Z",
        choice: ["word"]
    }
    )

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
        setSearchKeyWords({ ...SearchKeyWords, start_time: isotime })


    }
    function endTimeHandler(isotime: string) {
        setSearchKeyWords({ ...SearchKeyWords, end_time: isotime })
    }

    function searchButtonOnClick() {
        if (SearchKeyWords.screen_name == "") {
            /*todo promopt user to input keyword*/
            alert("Should fill the keywords!")
            console.log("")
        } else {
            props.callback(SearchKeyWords)
        }
    }


    return (
        <div>
            <Autocomplete
                freeSolo
                id="main-search-box"
                disableClearable
                options={search_box_content.map(res => res['username'])}
                onChange={(e: any, v: string) => { setSearchKeyWords({ ...SearchKeyWords, screen_name: v }); }}
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
        </div>
    );
}

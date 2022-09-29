import { useState, useEffect } from 'react'
import axios from 'axios'
import MaterialUIPickers from './DataPicker';
import DatePicker2 from './DatePicker2';
import Grid from '@mui/material/Unstable_Grid2';
import { Container, Button, Autocomplete, TextField, Stack, Box, Typography } from '@mui/material';
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
            console.log(SearchKeyWords)
        } else {
            console.log(SearchKeyWords)
            props.callback(SearchKeyWords)
        }
    }


    return (
        <Container maxWidth='md' sx={{mx: "auto"}}>

            <Stack spacing={3}>
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
                <Stack direction="row" sx={{ justifyContent: "space-between" }}>

                    <Stack direction="row" spacing={2} alignItems="flex-end">
                        {/* <MaterialUIPickers title="Start Time" callback={startTimeHandler} />
                            <MaterialUIPickers title="Start Time" callback={startTimeHandler} /> */}
                        <DatePicker2 title="Start Time" callback={startTimeHandler} />
                        <DatePicker2 title="End Time" callback={endTimeHandler} />
                        <Box>
                            <Typography sx={{color: "gray"}}>(UTC+0)</Typography>
                        </Box>
                    </Stack>


                    <Button variant="contained" onClick={searchButtonOnClick}>Search</Button>


                </Stack>
            </Stack>

        </Container>
    );
}

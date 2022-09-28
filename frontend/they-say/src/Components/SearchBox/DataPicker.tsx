import * as React from 'react';
import dayjs, { Dayjs } from 'dayjs';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker';
import { MobileDatePicker } from '@mui/x-date-pickers/MobileDatePicker';


type PropTypes = {
    title: string,
    callback: Function
}

function MaterialUIPickers(props: PropTypes) {

    const [value, setValue] = React.useState<Dayjs | null>();



    React.useEffect(
        () => {
            console.log(props.title)
            /*todo: need to get the current date when title is endtime*/
            if (props.title == "Start Time") {
                setValue(dayjs('2010-08-18T21:11:54'))
            } else if (props.title == "End Time") {
            }
        }, []
    )


    function handleChange(newValue: Dayjs | null) {
        setValue(newValue);
        props.callback(newValue?.toISOString());
    }

    return (
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <Stack spacing={3}>
                <DateTimePicker
                    label={props.title}
                    value={value}
                    onChange={handleChange}
                    renderInput={(params) => <TextField {...params} />}
                />
            </Stack>
        </LocalizationProvider>
    );
}

export default MaterialUIPickers
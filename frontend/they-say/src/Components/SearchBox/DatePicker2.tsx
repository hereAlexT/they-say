import * as React from 'react';
import dayjs, { Dayjs } from 'dayjs';
import TextField from '@mui/material/TextField';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker';



type DatePicker2Types = {
  title: string,
  callback: Function
}


export default function DatePicker2(props: DatePicker2Types) {
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
    if (newValue?.isValid() == true){
    setValue(newValue);
    props.callback(newValue?.toISOString());
    }
  }

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>

      <DesktopDatePicker
        label= {props.title}
        inputFormat="MM/DD/YYYY"
        value={value}
        onChange={handleChange}
        onAccept = {handleChange}
        renderInput={(params) => <TextField {...params} />}

      />

    </LocalizationProvider>
  );
}

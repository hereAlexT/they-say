import axios from 'axios'


export type WordFreqRequestType = {
    screen_name: string,
    start_time: string,
    end_time: string
    choice: [string]
}

export async function GetWordFreq(prop: WordFreqRequestType) {
    let w_array:any 

    let res = await axios.post('https://api.theysay.tech/wf',
        prop)
        .then(res => {
            w_array = res.data.data
        })
        .catch(err => console.log(err))

    return w_array
}
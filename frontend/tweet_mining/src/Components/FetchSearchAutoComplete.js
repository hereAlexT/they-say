import { useEffect, useState} from 'react';


function FetchSearchAutoComplete() {
    const data = { "arg": "get_available_users" };

    function LoadAutoComplete() {
        fetch('http://127.0.0.1:5000/api/basic', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },

            body: JSON.stringify(data),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }
    const [activity, setActivity] = useState([]); 
    useEffect(() => { LoadAutoComplete() });

    return <h1>Somehing c sdsd alled</h1>
}

export default etchSearchAutoComplete
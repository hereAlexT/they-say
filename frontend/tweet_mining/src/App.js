import * as React from 'react';
import Button from '@mui/material/Button';
import WordFreqTable from './Components/WordFreqTable';
import UserSearchBox from './Components/UserSearchBox';
import './index.css';




function App() {
  return (
    <div className="App">

      <h1>Tweet Mining</h1>
      <p>Welcome to Tweet Mining, </p>
      <UserSearchBox></UserSearchBox>
      <Button variant="contained">Search</Button>
      <WordFreqTable />

      <button>-</button>
      <span>0</span>
      <button>+</button>

    </div>
  );
}




export default App;

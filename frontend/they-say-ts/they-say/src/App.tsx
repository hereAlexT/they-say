import React from 'react';
import logo from './logo.svg';
import SearchBox from './Components/SearchBox';
import FreqTable from './Components/FreqTable';
import './App.css';
import { useState, useEffect } from 'react'



function App() {
  const [search_words, set_search_words] = useState<string>("")





  /* todo: figure out the type of e */
  function searchHandler(e: any, newValue: string) {
    /* todo: maybe do analyze here, then choose the correct to coll*/
    console.log("Your inpur searching word is '" + newValue + "'")
    set_search_words(newValue)
  }

  function GetFreqTable() {
    const getOrNot = search_words != "";
    if (getOrNot === true) {
      console.log("Yes, we should build a freqtable")
      /* start_time and end_time shoule be defined here */
      return (
        <FreqTable search_words={search_words} />
      )
    }
    else {
      console.log("No, we don't need a freqtable")
    }
    return <div>No Data Loaded</div>
  }


  return (
    <div className="App">
      <h1>TheySay.app</h1>
      <SearchBox searchHandler={searchHandler} />
      <GetFreqTable />

    </div>
  );
}

export default App;

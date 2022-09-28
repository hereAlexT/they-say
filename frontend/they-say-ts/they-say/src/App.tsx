import React from 'react';
import SearchBox from './Components/SearchBox/SearchBox';
import FreqTable from './Components/FreqTable';
import './App.css';
import { useState, useEffect } from 'react'
import Footer from './Components/Footer'
import HeroComponent from './Components/HeroComponent'
import NavBar from './Components/NavBar'
import Container from '@mui/material/Container';


/*todo: alreadly defined in searchbox, no need to define here */
type search_keywords_type = {
  "keywords": string,
  "starttime": string,
  "endtime": string
}


function App() {
  const [search_words, set_search_words] = useState<search_keywords_type>({ keywords: "", starttime: "2010-09-28T08:27:35.000Z", endtime: "2022-09-28T08:27:35.000Z" })

  /* todo: figure out the type of e */
  function searchHandler(e: any) {
    /* todo: maybe do analyze here, then choose the correct to coll*/
    // console.log("Your inpur searching word is '" + newValue + "'")
    // set_search_words(newValue)
    set_search_words(e)
  }

  function GetFreqTable() {
    const getOrNot = search_words.keywords != "" && search_words.starttime != "" && search_words.endtime != "";
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
      <NavBar />
      <HeroComponent />
      <Container>
        <SearchBox searchHandler={searchHandler} />
        <GetFreqTable />
      </Container>
      <Footer />
    </div>
  );
}

export default App;

import React from 'react';
import SearchBox from './Components/SearchBox/SearchBox';
import FreqTable from './Components/FreqTable';
import './App.css';
import { useState, useEffect } from 'react'
import Footer from './Components/Footer'
import HeroComponent from './Components/HeroComponent'
import NavBar from './Components/NavBar'
import Container from '@mui/material/Container';
import { WordFreqRequestType } from './Funs/GetWordFreq';
import { GetWordFreq } from './Funs/GetWordFreq';
import WordCloud from "./Components/WordCloud"





function App() {
  /* todo: should not use any, but I don't know how to solve it wisely */
  const [WordFreqData, setWordFreqData] = useState<any>()

  async function searchHandler(e: WordFreqRequestType) {
    var res: any = await GetWordFreq(e)
    setWordFreqData(res)
    // console.log("searchHandelr")
    // console.log(res)
  }

  function GetFreqTable() {
    const getOrNot = WordFreqData != undefined && WordFreqData != null;
    if (getOrNot === true) {
      console.log("Yes, we should build a freqtable")
      /* start_time and end_time shoule be defined here */
      return (
        <FreqTable data={WordFreqData} />
      )
    }
    else {
      console.log("No, we don't need a freqtable")
    }
    return <div>No Data Loaded</div>
  }

  function GetWordCloud() {
    const getOrNot = WordFreqData != undefined && WordFreqData != null;
    if (getOrNot === true) {
      console.log("Yes, we should build a word cloud")
      /* start_time and end_time shoule be defined here */
      return (
        <WordCloud data={WordFreqData} />
      )
    }
    else {
      console.log("No, we don't need word cloud")
    }
    return <div>No Data Loaded</div>
  }



  return (
    <div className="App">
      <NavBar />
      <HeroComponent />
      <Container>
        <SearchBox callback={searchHandler} />
        <Container maxWidth='md' sx={{mx:"auto", my:2}}>
          <GetFreqTable />
        </Container>
        <Container maxWidth='md' sx={{mx:"auto", mt:3}}>
          <GetWordCloud />
        </Container>
      </Container>
      <Footer />
    </div>
  );
}

export default App;
function setSearchKeyWords(arg0: { start_time: any; data?: [{ screen_name: string; data: []; }] | undefined; }) {
  throw new Error('Function not implemented.');
}


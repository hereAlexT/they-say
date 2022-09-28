import React from 'react';
import logo from './logo.svg';
import SearchBox from './Components/SearchBox';
import './App.css';
import { useState, useEffect } from 'react'


function App() {
  const [search_words, set_search_words] = useState<{search_words: String}>({search_words: ""})





  /* todo: figure out the type of e */
  function searchHandler(e: any, newValue: String) {
    /* todo: maybe do analyze here, then choose the correct to coll*/
    console.log("Your inpur searching word is '" + newValue + "'")
    set_search_words({search_words: newValue})
  }


  return (
    <SearchBox searchHandler={searchHandler} />
  );
}

export default App;

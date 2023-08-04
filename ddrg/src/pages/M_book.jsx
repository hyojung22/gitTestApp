import React, { useState } from 'react'
import './Main.css'
import All from '../etc/all.json'
import Book from '../components/Book.jsx'

const M_book = () => {

  let randomPick = [~~(Math.random()*20)] // 20권 중에
  let [category, setCategory] = useState('종합');

  const bestBook = () =>{
    randomPick=[~~(Math.random()*20)];

    while(randomPick.length<3) { // 3권 추천
      var sum = 0;
      var random = ~~(Math.random()*20)
      randomPick.map((e)=>e==random).map((e)=>sum+=e)
      if(sum/randomPick.length == 0){
        randomPick.push(random)
      }
    }
    console.log('success', randomPick);
  }
  bestBook();

  const cellectHandle = (category) =>{
    setCategory(category)
    bestBook()
  }
  
  // console.log(All.제목[randomPick]);

  return (
    <div className='center'>
      <div>
        <button onClick={()=>cellectHandle('종합')}>종합</button>
        <button onClick={()=>cellectHandle('소설')}>소설</button>
        <button onClick={()=>cellectHandle('에세이')}>에세이</button>
        <button onClick={()=>cellectHandle('인문')}>인문</button>
        <button onClick={()=>cellectHandle('경제')}>경제</button>
        <button onClick={()=>cellectHandle('과학')}>과학</button>
        <button onClick={()=>cellectHandle('자기계발')}>자기계발</button>
      </div>
      <div className='bookCase'>
        <Book All={All} category={category} randomPick={randomPick[0]}></Book>
        <Book All={All} category={category} randomPick={randomPick[1]}></Book>
        <Book All={All} category={category} randomPick={randomPick[2]}></Book>
      </div>
    </div>
  )
}

export default M_book
import React, { useState } from 'react'
import './Main.css'
import All from '../etc/all.json'
import Book from '../components/Book.jsx'

const M_book = () => {

  let randomPick = [~~(Math.random()*20)] // 20권 중에
  let [category, setCategory] = useState('종합');
  let [cateplus, setCateplus] = useState(0);

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

  const cellectHandle = (category,num) =>{
    setCategory(category)
    setCateplus(num)
    bestBook()
  }
  

  return (
    <div className='center'>
      <div>
        <button onClick={()=>cellectHandle('종합',0)}>종합</button>
        <button onClick={()=>cellectHandle('소설',20)}>소설</button>
        <button onClick={()=>cellectHandle('에세이',40)}>에세이</button>
        <button onClick={()=>cellectHandle('인문',60)}>인문</button>
        <button onClick={()=>cellectHandle('경제',80)}>경제</button>
        <button onClick={()=>cellectHandle('과학',100)}>과학</button>
        <button onClick={()=>cellectHandle('자기계발',120)}>자기계발</button>
      </div>
      <div className='bookCase'>
        <Book All={All} category={category} randomPick={randomPick[0]} cateplus={cateplus}></Book>
        <Book All={All} category={category} randomPick={randomPick[1]} cateplus={cateplus}></Book>
        <Book All={All} category={category} randomPick={randomPick[2]} cateplus={cateplus}></Book>
      </div>
    </div>
  )
}

export default M_book
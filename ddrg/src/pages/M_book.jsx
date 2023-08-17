import React, { useEffect, useRef, useState } from 'react'
import All from '../etc/all.json'
import Book from '../components/Book.jsx'

import shape_icon from '../img/도서img/circle.png'
import shape_icon1 from '../img/도서img/Random_img.png'
import bookImgSrc from '../img/도서img/book_bar.png'

const M_book = () => {

  // 점 위치 설정
  const begin = useRef();
  const [shapePosition, setShapePosition] = useState(0); // 도형 위치 변경
  
  useEffect(()=>{
    const begin_position = begin.current.offsetLeft+begin.current.getBoundingClientRect().width/2-2.5;
    setShapePosition(begin_position)
  },[])

  const bookSelect = (e) =>{
    var left = e.target.offsetLeft;
    var half = e.target.getBoundingClientRect().width/2-2.5;
    return left+half
  }


  // 책 고르기
  let randomPick = [~~(Math.random()*20)] // 20권 중에
  let [category, setCategory] = useState('종합');
  let [catePlus, setCatePlus] = useState(0);



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
  }
  bestBook();

  const cellectHandle = (category,num,e) =>{
    setCategory(category)
    setCatePlus(num)
    bestBook()

    setShapePosition(bookSelect(e)) // 해당 카테고리에 맞는 위치로 설정
  }

  useEffect(()=>{
    window.scrollTo(0,0)
  },[])

  return (
    <div className='center'>
      <div className='book_btn_box'>
        <img src={shape_icon} className='book_select' style={{left:shapePosition}}/>
        <div className='book_iconBox'>
          <img src={shape_icon1} className='book_icon'/>
          <strong className='book_title'>오늘의 PICK</strong>
        </div>
        <button onClick={(e)=>cellectHandle('종합',0,e)} ref={begin}>종합</button>
        <button onClick={(e)=>cellectHandle('소설',20,e)}>소설</button>
        <button onClick={(e)=>cellectHandle('에세이',40,e)}>에세이</button>
        <button onClick={(e)=>cellectHandle('인문',60,e)}>인문</button>
        <button onClick={(e)=>cellectHandle('경제',80,e)}>경제</button>
        <button onClick={(e)=>cellectHandle('과학',100,e)}>과학</button>
        <button onClick={(e)=>cellectHandle('자기계발',120,e)}>자기계발</button>
      </div>
      <div className='bookCase'>
        <Book All={All} category={category} randomPick={randomPick[0]} catePlus={catePlus}/>
        <Book All={All} category={category} randomPick={randomPick[1]} catePlus={catePlus}/>
        <Book All={All} category={category} randomPick={randomPick[2]} catePlus={catePlus}/>
        <img src={bookImgSrc} className='bookBar'/>
      </div>
    </div>
  )
}

export default M_book
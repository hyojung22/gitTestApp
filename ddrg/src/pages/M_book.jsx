import React, { useState } from 'react'
import All from '../etc/all.json'
import Book from '../components/Book.jsx'

import shape_icon from '../img/도서img/circle.png'
import shape_icon1 from '../img/도서img/Random_img.png'
import bookImgSrc from '../img/도서img/book_bar.png'

const M_book = () => {

  // const bookImgSrc = require('../img/도서img/book_bar.png') 

  // 점 위치 설정
  const positions = {
    '종합' : 139.5,
    '소설' : 62.5,
    '에세이' : -21.5,
    '인문' : -104.5,
    '경제' : -182.5,
    '과학' : -259.5,
    '자기계발' : -349.5,
  }

  let randomPick = [~~(Math.random()*20)] // 20권 중에
  let [category, setCategory] = useState('종합');
  let [cateplus, setCateplus] = useState(0);

  let [showShape, setShowShape] = useState(false); // 도형 이미지 표시 여부 상태 추가
  let [shapePosition, setShapePosition] = useState(0); // 도형 위치 변경


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

    setShowShape(true) // 도형 이미지 보이게 설정
    setShapePosition(positions[category]) // 해당 카테고리에 맞는 위치로 설정
  }

  return (
    <div className='center'>
      <img src={shape_icon1} alt='말풍선 이미지' className='shape_icon1'/>
      {showShape && <img
                      src={shape_icon} 
                      alt='도형 이미지' 
                      className='shape_icon'
                      style={{ right : shapePosition + 'px'}}
                    />
      }
      <div className='book_btn_box'>
        <span className='title_heading'>오늘의 PICK</span>
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
      <img src={bookImgSrc} className='bookBar'/>
    </div>
  )
}

export default M_book
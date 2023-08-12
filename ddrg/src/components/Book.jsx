import React from 'react'

const book = ({All, randomPick, category, catePlus}) => {


  
  const imageSrc = require(`../books/베스트셀러표지/${category}/${category}${~~(randomPick)+1}.jpg`);

  return (
    <div className='bookInfo'> 
        <a href={All.주소[randomPick+catePlus]}>
          <img src={imageSrc} className='bookCover'/>
        </a>
        <div className='book_cover_blink'/>
        <div className='book_textBox'>
          <strong className='book_content1'>{All.제목[randomPick+catePlus]}</strong>
          <hr/>
          <strong className='book_content2'>{All.저자[randomPick+catePlus]} 지음 | {All.가격[randomPick+catePlus]}</strong>
        </div>
    </div>
  )
}

export default book
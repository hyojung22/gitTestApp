import React from 'react'

const book = ({All, category, randomPick, cateplus}) => {


  
  const imageSrc = require(`../books/베스트셀러표지/${category}/${category}${~~(randomPick)+1}.jpg`);

  return (
    <div className='bookInfo'> 
        <img src={imageSrc} className='bookCover'/>
        <div className='book_cover_blink'/>
        <div className='book_textBox'>
          <strong className='book_content1'>{All.제목[randomPick+cateplus]}</strong>
          <hr/>
          <strong className='book_content2'>{All.저자[randomPick+cateplus]} 지음 | {All.가격[randomPick+cateplus]}</strong>
        </div>
    </div>
  )
}

export default book
import React from 'react'

const book = ({All, category, randomPick, cateplus}) => {

  const imageSrc = require(`../books/베스트셀러표지/${category}/${category}${~~(randomPick)+1}.jpg`);

  console.log(cateplus);
  return (
    <div className='bookInfo'>
      <img src={imageSrc} className='bookCover'/>
      <span>{All.제목[randomPick+cateplus]}</span>
      <span>{All.저자[randomPick+cateplus]} 지음 | {All.가격[randomPick+cateplus]}</span>
    </div>
  )
}

export default book
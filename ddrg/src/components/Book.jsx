import React from 'react'

const book = ({All, category, randomPick}) => {

  const imageSrc = require(`../books/베스트셀러표지/${category}/${category}${~~(randomPick)+1}.jpg`);

  console.log(category);
  return (
    <div className='bookInfo'>
      <img src={imageSrc} className='bookCover'/>
      <span>{All.제목[randomPick]}</span>
      <span>{All.저자[randomPick]} 지음 | {All.가격[randomPick]}</span>
    </div>
  )
}

export default book
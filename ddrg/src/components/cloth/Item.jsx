import React, { useState } from 'react'
import fashionInfo from '../../etc/fashion.json'
import Explain from './Explain';

const Item = ({kinds, explainValue}) => {

  const array = []
  for(let i=1;i<91;i++){
    array.push(i)
  }
  const capArr = array.map((e)=>{
    return require(`../../img/패션img/${kinds}/${kinds}${e}.jpg`)
  })

  const kindNum = {
    '상의':0,
    '하의':90,
    '신발':180,
    '모자':360
  }

  // 상위로 보내는 정보
  const handleDetail = (num) =>{
    const info = [
      fashionInfo.가격[kindNum[kinds]+num],
      fashionInfo.브랜드[kindNum[kinds]+num],
      fashionInfo.옷[kindNum[kinds]+num],
      fashionInfo.주소[kindNum[kinds]+num],
      `../../img/패션img/${kinds}/${kinds}${num}.jpg`
    ]
    explainValue(info)
  }

  return (
    <div style={{
      display:'flex',
      height:'100%'
    }}>
      {capArr.map((e, index)=>
        (<img draggable='false' key={e} src={e} className='fashion_item' onClick={()=>handleDetail(index+1)}/>)
      )}
    </div>
  )
}

export default Item
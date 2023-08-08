import React, { useState } from 'react'
import fashionInfo from '../../etc/fashion.json'
import Explain from './Explain';

const Item = ({kinds}) => {

  const [explain,setExplain] = useState(false);
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
  const handleDetail = (num) =>{
    setExplain(true);
    console.log(fashionInfo.가격[kindNum[kinds]+num]);
  }

  return (
    <div style={{
      display:'flex',
      height:'100%'
    }}>
      {capArr.map((e, index)=>
        (<img draggable='false' key={e} src={e} className='fashion_item' onClick={()=>handleDetail(index+1)}/>)
      )}
      <Explain/>
    </div>
  )
}

export default Item
import React, { useState, useEffect } from 'react';
import axios from 'axios'
// import fashionInfo from '../../etc/fashion.json'


const Item = ({kinds, explainValue, isClick}) => {

  const [data1, setData1] = useState([]);
  
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get("http://127.0.0.1:5021/fashion_list");
        setData1(result.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        // 오류 처리: 사용자에게 오류 메시지를 보여줄 수 있음
      }
    };
    
    fetchData();
  }, []);



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
      // fashionInfo.가격[kindNum[kinds]+num],
      // fashionInfo.브랜드[kindNum[kinds]+num],
      // fashionInfo.옷[kindNum[kinds]+num],
      // fashionInfo.주소[kindNum[kinds]+(num-1)],
      data1[kindNum[kinds]+num]["가격"],
      data1[kindNum[kinds]+num]["브랜드"],
      data1[kindNum[kinds]+num]["옷"],
      data1[kindNum[kinds]+(num-1)]["주소"],
      require(`../../img/패션img/${kinds}/${kinds}${num}.jpg`)
    ]
    explainValue(info)
  }

  return (
    <div style={{
      display:'flex',
      height:'100%'
    }}>
      {capArr.map((e, index)=>
        (<img draggable='false' key={e} src={e} className='fashion_item' onClick={isClick ? ()=>handleDetail(index+1) : null}/>)
      )}
    </div>
  )
}

export default Item
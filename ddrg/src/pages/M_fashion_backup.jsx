import React, {useState, useRef, useEffect } from 'react';
import Item from '../src/components/cloth/Item.jsx';
import Explain from '../src/components/cloth/Explain.jsx';
import imgParts1 from '../img/패션img/parts1.png'
import imgParts2 from '../img/패션img/parts2.png'
import imgParts3 from '../img/패션img/parts3.png'
import imgParts4 from '../img/패션img/parts4.png'
import imgDeco1 from '../img/패션img/img1.png'
import imgDeco2 from '../img/패션img/img2.png'
import imgDeco3 from '../img/패션img/img3.png'
import imgDeco4 from '../img/패션img/shoe.png'

const M_fashion = () => {
  const max_height = window.innerHeight-100
  const piece_height = max_height*0.25

  // Drag 관련 코드

  const [choice,setChoice] = useState(0);
  const [drag,setDrag] = useState(0);
  const [left,setLeft] = useState([0,0,0,0]);
  // const [dragging,setDragging] = useState(false);
  // class에 삼항연산자로 넣어서 드래그할 때 스타일을 따로 넣을 수 있다.
  const dragNode = useRef();
  let Xstart = 0;
  let Xend = 0;

  const handleDragStart = (e, num) =>{
    // console.log('drag starting', e.screenX);
    Xstart = e.screenX;
    // setDragging(true);
    setChoice(num);
    dragNode.current = e.target;
    dragNode.current.addEventListener('dragend',handleDragEnd);
  }
  const handleDragEnd = (e) =>{
    // console.log('drag ending..', e.screenX);
    Xend = e.screenX;
    setDrag(Xend-Xstart);
    // setDragging(false);
    dragNode.current.removeEventListener('dragend', handleDragEnd);
    dragNode.current = null;
  }
  const style1 = {
    height:piece_height,
    left:left[0],
  }
  const style2 = {
    height:piece_height,
    left:left[1],
  }
  const style3 = {
    height:piece_height,
    left:left[2],
  }
  const style4 = {
    height:piece_height,
    left:left[3],
  }
  useEffect(()=>{
    const leftArr = [...left]
    leftArr[choice] = left[choice]+drag
    setLeft(leftArr)
  },[drag])

  // explain

  const [explain,setExplain] = useState(false);
  const [explainInfo,setExplainInfo] = useState([])

  const explainValue = (value) =>{
    setExplain(true);
    setExplainInfo(value);
  }
  const explainEnd = (boolean) =>{
    setExplain(boolean);
  }

  return (
    <div className='center'>
      <div className='fashion_range' style={{
        height:max_height
        }}>
        <div className='fashion_name fashionN1' style={{
          height:piece_height
        }}>
          <img src={imgParts1}/>
        </div>
        <div className='fashion' style={{
          height:piece_height
        }}>
          <div
          className='fashion_drag'
          style={style1}
          draggable 
          onDragStart={(e) => {handleDragStart(e, 0)}} 
          >
            <Item kinds='모자' explainValue={explainValue}/>
          </div>
        </div>
        <div className='fashion' style={{
          height:piece_height
        }}>
          <div
          className='fashion_drag'
          style={style2}
          draggable 
          onDragStart={(e) => {handleDragStart(e, 1)}} 
          >
            <Item kinds='상의' explainValue={explainValue}/>
          </div>
        </div>
        <div className='fashion_name fashionN2' style={{
          height:piece_height
        }}>
          <img src={imgParts2}/>
        </div>
        <div className='fashion_name fashionN3' style={{
          height:piece_height
        }}>
          <img src={imgParts3}/>
        </div>
        <div className='fashion' style={{
          height:piece_height
        }}>
          <div
          className='fashion_drag'
          style={style3}
          draggable 
          onDragStart={(e) => {handleDragStart(e, 2)}} 
          >
            <Item kinds='하의' explainValue={explainValue}/>
          </div>
        </div>
        <div className='fashion' style={{
          height:piece_height
        }}>
          <div
          className='fashion_drag'
          style={style4}
          draggable 
          onDragStart={(e) => {handleDragStart(e, 3)}} 
          >
            <Item kinds='신발' explainValue={explainValue}/>
          </div>
        </div>
        <div className='fashion_name fashionN4' style={{
          height:piece_height
        }}>
          <img src={imgParts4}/>
        </div>
        <img src={imgDeco1} className='fashion_deco1'/>
        <img src={imgDeco2} className='fashion_deco2'/>
        <img src={imgDeco3} className='fashion_deco3'/>
        <img src={imgDeco4} className='fashion_deco4'/>
        {explain && <Explain explainInfo={explainInfo} explainEnd={explainEnd}/>}
      </div>
    </div>
  )
}

export default M_fashion
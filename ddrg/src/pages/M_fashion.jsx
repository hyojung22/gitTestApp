import React, {useState, useRef, useEffect } from 'react';
import Item from '../components/cloth/Item.jsx';
import Explain from '../components/cloth/Explain.jsx';

const M_fashion = () => {
  const max_height = window.innerHeight-100

  const piece_height = max_height*0.25

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



  return (
    <div className='center'>
      <Explain/>
      <div className='fashion_range' style={{
        height:max_height
        }}>
        <div className='fashion_name'>
          모자
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
            <Item kinds='모자'/>
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
            <Item kinds='상의'/>
          </div>
        </div>
        <div className='fashion_name'>상의</div>
        <div className='fashion_name'>하의</div>
        <div className='fashion' style={{
          height:piece_height
        }}>
          <div
          className='fashion_drag'
          style={style3}
          draggable 
          onDragStart={(e) => {handleDragStart(e, 2)}} 
          >
            <Item kinds='하의'/>
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
            <Item kinds='신발'/>
          </div>
        </div>
        <div className='fashion_name'>신발</div>
      </div>
      <Explain/>
    </div>
  )
}

export default M_fashion
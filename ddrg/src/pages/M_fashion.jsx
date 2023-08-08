import React, {useState, useRef, useEffect } from 'react';
import Cap from '../components/cloth/Cap.jsx';
import Top from '../components/cloth/Top.jsx';
import Bottom from '../components/cloth/Bottom.jsx';
import Shoes from '../components/cloth/Shoes.jsx';

const M_fashion = () => {
  const max_height = window.innerHeight-100

  const cap_height = max_height*0.25
  const top_height = max_height*0.25
  const bottom_height = max_height*0.25
  const shoes_height = max_height*0.25

  const [drag,setDrag] = useState(0);
  const [left,setLeft] = useState(0);
  const [dragging,setDragging] = useState(false);
  // class에 삼항연산자로 넣어서 드래그할 때 스타일을 따로 넣을 수 있다.
  const dragItem = useRef();
  const dragNode = useRef();
  let Xstart = 0;
  let Xend = 0;

  const handleDragStart = (e) =>{
    console.log('drag starting', e.screenX);
    Xstart = e.screenX;
    setDragging(true);
    dragNode.current = e.target;
    dragNode.current.addEventListener('dragend',handleDragEnd);

    
  }

  const handleDragEnd = (e) =>{
    console.log('drag ending..', e.screenX);
    Xend = e.screenX;
    setDrag(Xend-Xstart);
    setDragging(false);
    dragNode.current.removeEventListener('dragend', handleDragEnd);
    dragNode.current = null;
  }

  const style = {
    height:cap_height,
    width:'100%',
    position:'relative',
    left:left,
    backgroundColor:'black'
  }

  useEffect(()=>{
    setLeft(left+drag)
  },[drag])



  return (
    <div className='center'>
      <div className='fashion_range' style={{
        height:max_height
        }}>
        <div className='fashion_name'/>
        <div className='fashion' style={{
          height:cap_height
        }}>
          <div
          style={style}
          draggable 
          onDragStart={(e) => {handleDragStart(e)}} 
          >
            <Cap/>
          </div>
        </div>
        <div className='fashion' style={{
          height:top_height
        }}>
          <div
          style={style}
          draggable 
          onDragStart={(e) => {handleDragStart(e)}} 
          >
            <Top/>
          </div>
        </div>
        <div className='fashion_name'/>
        <div className='fashion_name'/>
        <div className='fashion' style={{
          height:bottom_height
        }}>
          <div
          style={style}
          draggable 
          onDragStart={(e) => {handleDragStart(e)}} 
          >
            <Bottom/>
          </div>
        </div>
        <div className='fashion' style={{
          height:shoes_height
        }}>
          <div
          style={style}
          draggable 
          onDragStart={(e) => {handleDragStart(e)}} 
          >
            <Shoes/>
          </div>
        </div>
        <div className='fashion_name'/>
      </div>
    </div>
  )
}

export default M_fashion
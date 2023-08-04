import './firstPage.css'
import React, { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom';

import rat from '../img/짭쥐 표지-15.png';
import cat from '../img/짭쥐 표지-16.png';
import img2 from '../img/짭쥐 표지-17.png';
import img3 from '../img/짭쥐 표지-18.png';
import img4 from '../img/짭쥐 표지-19.png';
import icon1 from '../img/map.png';
import icon2 from '../img/book.png';
import icon3 from '../img/clothes.png';
import icon4 from '../img/cooking.png';
import icon5 from '../img/news.png';

const FirstPage = () => {

  
  // scroll 
  let [imgAlpha, setImgAlpha] = useState(0);
  let [maxScroll, setMaxScroll] = useState(1);
  // 
  const nameTop = useRef(); // 난 너를 사로짭쥐 DOM
  const center = window.innerHeight*1; // 화면 높이
  const [imgShape, setImgShape] = useState(0); // 짭쥐 위치(y축)
  let [topImg, setTopImg] = useState(-1000);
  const [minus, setMinus] = useState(0);

  // maxScroll 설정
  useEffect(()=>{
    window.scrollTo(0,1000);
    setMaxScroll(window.scrollY);
    window.scrollTo(0,0);
    console.log('minus', minus);
  },[])

  // imgAipha, topImg 반환
  const change = () => {
    setImgAlpha(window.scrollY/maxScroll);
    setTopImg((imgShape+minus)*(1-imgAlpha)-minus);
    // console.log(topImg);
  }
  window.addEventListener('scroll', change)

  // topimg 초기화
  useEffect(()=>{
    setTopImg(imgShape);
    setMinus(nameTop.current.height*0.4);
    change();
  },[imgShape])
  // 짭쥐 로드 시, imgshape 초기화 함수
  const handleImgShape = () =>{
    setImgShape(center/2-nameTop.current.height/2);
  }

  // text 위치 변경
  const textScroll = {
    top:topImg
  }
  return (
    <div className='scroll'>
    <div className='startPage'>
        {/* 첫페이지 */}
        <div className='firstPage'> 
          <img className='firstImg' src={img2} style={{opacity:(1-imgAlpha)}}/>
          <img className='firstImg' src={img3} style={textScroll} ref={nameTop} onLoad={handleImgShape}/>
          <img className='firstImg' src={img4} style={{opacity:(1-imgAlpha)}}/>
          <img className='firstImg' src={cat} style={{opacity:(1-imgAlpha)}}/>
          <img className='firstImg' src={rat} style={{opacity:(1-imgAlpha)}}/>
        </div>
        {/* 아이콘 페이지 */}
        <div className='secondPage'style={{
            opacity:imgAlpha
          }}>
            <img className='secondImg' src={icon1}/>
            <img className='secondImg' src={icon2}/>
            <img className='secondImg' src={icon3}/>
            <img className='secondImg' src={icon4}/>
            <img className='secondImg' src={icon5}/>
        </div>
        <Link to={'/main'} className='button'>
          <button className='buttonKid'>
          </button>
          <button className='buttonKid'>
          </button>
          <button className='buttonKid'>
          </button>
          <button className='buttonKid'>
          </button>
          <button className='buttonKid'>
          </button>
        </Link>
        {/* <div className='button'> // backup용
          <Link to={'/Main/traval'} className='buttonKid'/>
          <Link to={'/Main/book'} className='buttonKid' />
          <Link to={'/Main/fashion'} className='buttonKid' />
          <Link to={'/Main/cook'} className='buttonKid' />
          <Link to={'/Main/news'} className='buttonKid' />
        </div> */}

    </div>
    </div>
  )
}

export default FirstPage
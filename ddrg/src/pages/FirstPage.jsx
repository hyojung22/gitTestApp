import './firstPage.css'
import React from 'react'
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

const firstPage = () => {

  // window.addEventListener('scroll', ()=>{
  //   var scroll = window.scrollY;
  //   firstPage.
  // })
  return (
    <div className='startPage'>
        {/* 첫페이지 */}
        <div className='firstPage'> 
          <img className='firstImg' src={img2}/>
          <img className='firstImg' src={img3}/>
          <img className='firstImg' src={img4}/>
          <img className='firstImg' src={cat}/>
          <img className='firstImg' src={rat}/>
        </div>
        {/* 아이콘 페이지 */}
        <div className='secondPage'>
          <img className='secondImg' src={icon1}/>
          <img className='secondImg' src={icon2}/>
          <img className='secondImg' src={icon3}/>
          <img className='secondImg' src={icon4}/>
          <img className='secondImg' src={icon5}/>
        </div>
    </div>
  )
}

export default firstPage
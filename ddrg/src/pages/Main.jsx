import React from 'react'

import icon1 from '../img/map.png';
import icon2 from '../img/book.png';
import icon3 from '../img/clothes.png';
import icon4 from '../img/cooking.png';
import icon5 from '../img/news.png';

import { Link } from 'react-router-dom';

const Main = () => {


  return (
    <div className='center'>
      {/* 아이콘 페이지 */}
      <div className='iconCon'>
        <Link to='/main/traval' className='icon'>
          <img className='iconImg' src={icon1}/>
        </Link>
        <Link to='/main/book' className='icon'>
          <img className='iconImg' src={icon2}/>
        </Link>
        <Link to='/main/fashion' className='icon'>
          <img className='iconImg' src={icon3}/>
        </Link>
        <Link to='/main/cook' className='icon'>
          <img className='iconImg' src={icon4}/>
        </Link>
        <Link to='/main/news' className='icon'>
          <img className='iconImg' src={icon5}/>
        </Link>
      </div>
      <div className='explain'>
        <div>
          <div>map</div>
        </div>
      </div>
    </div>
  )
}

export default Main
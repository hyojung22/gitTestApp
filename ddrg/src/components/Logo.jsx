import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import img from '../img/Logo.png'

const Logo = ({location}) => {

  const menu1 = (location.pathname === '/main/cook')
  const menu2 = (location.pathname === '/main/book')
  const menu3 = (location.pathname === '/main/fashion')
  const menu4 = (location.pathname === '/main/festival')
  const menu5 = (location.pathname === '/main/news')

  const [selectLeft, setSelectLeft] = useState(null);

  const menuMap = [menu1,menu2,menu3,menu4,menu5];
  
  const logoStyle = {
    position:'relative',
    width:'140px', 
    height:'50px',
    top:'5px',
  }
  useEffect(()=>{
    const startLeft = -1;
    if(menu1){
      return setSelectLeft(startLeft)
    }else if(menu2){
      return setSelectLeft(startLeft+70*1)
    }else if(menu3){
      return setSelectLeft(startLeft+70*2)
    }else if(menu4){
      return setSelectLeft(startLeft+70*3)
    }else if(menu5){
      return setSelectLeft(startLeft+70*4)
    }
  },[menuMap])

  return (
    <div className='blankSpace'>
      <div className='header'>
        <div style={{left:'5px'}}>
          <Link to={'/'}>
            <img src={img} style={logoStyle}/>
          </Link>
        </div>
        <div className='logo_buttonBox'>
          <div className='logo_selecter' style={{left:selectLeft}}/>
          <Link to={'/main/cook'}>
            <button className='logo_button'
            style={menu1?{color:'white',fontWeight: 'bolder'}:null}>요리</button>
          </Link>
          <Link to={'/main/book'}>
            <button className='logo_button'
            style={menu2?{color:'white',fontWeight: 'bolder'}:null}>도서</button>
          </Link>
          <Link to={'/main/fashion'}>
            <button className='logo_button'
            style={menu3?{color:'white',fontWeight: 'bolder'}:null}>패션</button>
          </Link>
          <Link to={'/main/festival'}>
            <button className='logo_button'
            style={menu4?{color:'white',fontWeight: 'bolder'}:null}>축제</button>
          </Link>
          <Link to={'/main/news'}>
            <button className='logo_button'
            style={menu5?{color:'white',fontWeight: 'bolder'}:null}>뉴스</button>
          </Link>
        </div>
      </div>
    </div>
  )
}

export default Logo
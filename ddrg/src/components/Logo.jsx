import React from 'react'
import { Link } from 'react-router-dom'
import img from '../img/Logo.png'

const Logo = ({location}) => {

  const menu1 = (location.pathname === '/main/festival')
  const menu2 = (location.pathname === '/main/book')
  const menu3 = (location.pathname === '/main/news')
  const menu4 = (location.pathname === '/main/fashion')
  const menu5 = (location.pathname === '/main/cook')

  console.log(menu1);
  const backgroundStyle = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'end',
    position: 'relative',

    width: '100vw',
    height:'80px',
    backgroundColor:'#3e448b'
  }

  const logoStyle = {
    position:'relative',
    width:'140px', 
    height:'50px',
    right: '20px'
  }

  return (
    <div className='center' style={{position:'relative', justifyContent:'center'}}>
      <div style={backgroundStyle}>
        <Link to={'/'}>
          <img src={img} style={logoStyle}/>
        </Link>
      </div>
      <div style={{position: 'absolute'}}>
        <Link to={'/main/festival'}>
          <button className='logo_button' style={menu1?{backgroundColor:'white',color:'#3e448b'}:null}>축제</button>
        </Link>
        <Link to={'/main/book'}>
          <button className='logo_button' style={menu2?{backgroundColor:'white',color:'#3e448b'}:null}>도서</button>
        </Link>
        <Link to={'/main/news'}>
          <button className='logo_button' style={menu3?{backgroundColor:'white',color:'#3e448b'}:null}>뉴스</button>
        </Link>
        <Link to={'/main/fashion'}>
          <button className='logo_button' style={menu4?{backgroundColor:'white',color:'#3e448b'}:null}>패션</button>
        </Link>
        <Link to={'/main/cook'}>
          <button className='logo_button cook' style={menu5?{backgroundColor:'white',color:'#3e448b'}:null}>요리</button>
        </Link>
      </div>
    </div>
  )
}

export default Logo
import React from 'react'
import img from '../img/Logo.png'

const Logo = () => {

  const backgroundStyle = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    position: 'relative',

    width: '100vw',
    height:'80px',
    backgroundColor:'#3e448b'
  }

  const logoStyle = {
    position:'relative',
    width:'200px', 
    height:'80px',
    right: '20px'
  }

  const button = {
  }

  return (
    <div style={backgroundStyle}>
      <div style={{position:'absolute'}}>
        <button style={button}>축제</button>
        <button style={button}>도서</button>
        <button style={button}>뉴스</button>
        <button style={button}>커뮤니티</button>
        <button style={button}>패션</button>
        <button style={button}>요리</button>
      </div>
      <img src={img} style={logoStyle}/>
    </div>
  )
}

export default Logo
import React from 'react'
import img from '../img/로고.png'

const Logo = () => {
  return (
    <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'end',
        width: '100vw',
        height:'80px',
        backgroundColor:'#3e448b'
    }}>
        <img src={img} style={{
          position:'relative',
          width:'200px', 
          height:'80px',
          right: '20px'}}/>
    </div>
  )
}

export default Logo
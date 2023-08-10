import React from 'react'
import Menu from '../img/LogoMenu.png'

const LogoMenu = ({location}) => {

    const menu1 = (location.pathname === '/main/festival')
    const menu2 = (location.pathname === '/main/book')
    const menu3 = (location.pathname === '/main/news')
    const menu4 = (location.pathname === '/main/fashion')
    const menu5 = (location.pathname === '/main/cook')

    const button = {
        width : '80px',
        height : '80px',
    }
  return (
    <div>
        <div style={button}>
            <img src={Menu}/>
        </div>
    </div>
  )
}

export default LogoMenu
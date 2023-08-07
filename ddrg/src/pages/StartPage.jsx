import React, { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom'
import logo from '../img/짭쥐 표지-18_cut.png'


/*
    class를 두개 설정 
    => 기본, 상위 fixed 

    ref로 변경된 top 값을 감지 후
    본인이 원하는 조건일때 상위 fixed로 class 변경 
*/

const StartPage = () => {

    const festival_img = require(`../img/축제img/${~~(Math.random()*10)+1}.jpg`);
    const book_img = require('../img/bookImg.jpg');
    let logoTop = 45;

    let logoRef = useRef()


    const logoStyle = {
        position:'absolute',
        width:'70%',
        top:`${logoTop}vh`,
        left:'15%'
    }

    useEffect(()=>{
        window.addEventListener('scroll',handleScroll)
        return () =>{
            window.removeEventListener('scroll',handleScroll)
        }
    },[])

    const handleScroll = () =>{        
        var windowY = ~~(document.documentElement.clientHeight);
        var scrollY = ~~(document.documentElement.scrollTop);
        // logoTop = 45-50*scrollY/windowY;

    }
    // logoTop 변수를 이용해서 로고의 위치를 변경하고 싶은데,
    // state를 이용하면 스크롤 할 때마다 랜더링 되면서 이미지가 바뀌고
    // let을 이용하면 logoTop이 안 변함.




  return (
    <div className='mainRange'>
        <div className='firstPage'>
            {/* 표지 이미지 합쳐서 ㅇㅇ 임시로 div */}
            <div className='coverImg'/>

            {document.documentElement.scrollTop > 150 
            ? <img src={logo} style={logoStyle} className="fixed"/>
            : <img src={logo} style={logoStyle} className="original"/>
            }
        </div>
        <div className='link_button_container'>
            <img className='link_button_1' src={festival_img} ref={logoRef}/>
            <div className='link_button_left'>
                <img className='link_button_2' src={book_img}/>
                <img className='link_button_3' />
            </div>
            <img className='link_button_4'/>
            <img className='link_button_5'/>
        </div>
        <div className='link_button_container'>
            <Link to={'/main/festival'} className='link_button_1 link_button'>
                festival
            </Link>
            <div className='link_button_left'>
                <Link to={'/main/book'} className='link_button_2 link_button'>
                    book
                </Link>
                <Link to={'/main/news'} className='link_button_3 link_button'>
                    news
                </Link>
            </div>
            <Link to={'/main/cook'} className='link_button_4 link_button'>
                cooking
            </Link>
            <Link to={'/main/fashion'} className='link_button_5 link_button'>
                fashion
            </Link>
        </div>
    </div>
  )
}

export default StartPage
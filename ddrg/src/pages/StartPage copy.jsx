import React, { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom';
import logo from '../img/Logo.png';
import mainCover from '../img/메인img/mainCover.png'
import img1 from '../img/메인img/1cook.png';
import img2 from '../img/메인img/2fashion.png';
import img3 from '../img/메인img/3news.png';
import img4 from '../img/메인img/4book.png';
import img5 from '../img/메인img/5festival.png';
import text1 from '../img/메인img/1cook_text.png';
import text2 from '../img/메인img/2fashion_text.png';
import text3 from '../img/메인img/3news_text.png';
import text4 from '../img/메인img/4book_text.png';
import text5 from '../img/메인img/5festival_text.png';



/*
    class를 두개 설정 
    => 기본, 상위 fixed 

    ref로 변경된 top 값을 감지 후
    본인이 원하는 조건일때 상위 fixed로 class 변경 
*/

const StartPage = () => {

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
            <img className='coverImg'src={mainCover}/>

            {document.documentElement.scrollTop > 150 
            ? <img src={logo} style={logoStyle} className="fixed"/>
            : <img src={logo} style={logoStyle} className="original"/>
            }
        </div>
        <div className='link_button_container'>
            <div className='link_button_side'>
                <img className='link_button_1' src={img1}/>
                <img className='link_button_2' src={img2}/>
            </div>
            <img className='link_button_3' src={img3}/>
            <div className='link_button_side'>
                <img className='link_button_4' src={img4}/>
                <img className='link_button_5' src={img5}/>
            </div>
        </div>
        <div className='link_text_container'>
            <div className='link_text_side'>
                <img className='link_text_1 link_text' src={text1}/>
                <img className='link_text_2 link_text' src={text2}/>
            </div>
            <div className='link_text_center'>
                <img className='link_text_31 link_text' src={text3}/>
                <img className='link_text_32 link_text' src={text3}/>
            </div>
            <div className='link_text_side'>
                <img className='link_text_4 link_text' src={text4}/>
                <img className='link_text_5 link_text' src={text5}/>
            </div>
        </div>
        <div className='link_button_container'>
            <div className='link_button_side'>
                <Link to={'/main/cook'} className='link_button_1 link_button'/>
                <Link to={'/main/fashion'} className='link_button_2 link_button'/>
            </div>
            <Link to={'/main/festival'} className='link_button_3 link_button'/>
            <div className='link_button_side'>
                <Link to={'/main/book'} className='link_button_4 link_button'/>
                <Link to={'/main/news'} className='link_button_5 link_button'/>
            </div>
        </div>
    </div>
  )
}

export default StartPage
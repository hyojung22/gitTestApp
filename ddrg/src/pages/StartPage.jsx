import React, { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router-dom';
import mainCover from '../img/메인img/mainCover.png'
import img1 from '../img/메인img/1cook.png';
import img2 from '../img/메인img/2fashion.png';
import img3 from '../img/메인img/3news.png';
import img4 from '../img/메인img/4book.png';
import img5 from '../img/메인img/5festival.png';
import text1 from '../img/메인img/1cook_text.png';
import text2 from '../img/메인img/2fashion_text.png';
import text3 from '../img/메인img/3news_text.png';
import text3ENd from '../img/메인img/3and_text.png';
import text3_2 from '../img/메인img/3community_text.png';
import text4 from '../img/메인img/4book_text.png';
import text5 from '../img/메인img/5festival_text.png';



/*
    class를 두개 설정 
    => 기본, 상위 fixed 

    ref로 변경된 top 값을 감지 후
    본인이 원하는 조건일때 상위 fixed로 class 변경 
*/

/*
    logo menu button 만들기
    link button 뒤집기
*/

const StartPage = () => {

    const [currentHeight, setCurrentHeight] = useState(document.documentElement.clientHeight)
    useEffect(()=>{
        window.addEventListener('scroll',handleScroll)
        return () =>{
            window.removeEventListener('scroll',handleScroll)
        }
    },[])

    const handleScroll = () =>{        
        var windowY = ~~(document.documentElement.clientHeight);
        var scrollY = ~~(document.documentElement.scrollTop);
        setCurrentHeight(windowY*(1-scrollY/windowY));
    }
    const pageHeight = {
        height:currentHeight
    }



  return (
    <div className='mainRange'>
        <div className='firstPage' style={pageHeight}>
            <img className='coverImg'src={mainCover}/>
        </div>
        <div className='link_button_container'>
            <div className='link_buttonBox left'>
                <Link to={'/main/cook'} className='link_item'>
                    <img className='link_button' src={img1}/>
                    <img className='link_text a' src={text1}/>
                </Link>
                <Link to={'/main/fashion'} className='link_item'>
                    <img className='link_button' src={img2}/>
                    <img className='link_text b' src={text2}/>
                </Link>
            </div>
            <div className='link_buttonBox center'>
                <Link to={'/main/news'} className='link_item'>
                    <img className='link_button' src={img3}/>
                    <img className='link_text c' src={text3}/>
                    <img className='link_textEnd' src={text3ENd}/>
                    <img className='link_text d' src={text3_2}/>
                </Link>
            </div>
            <div className='link_buttonBox right'>
                <Link to={'/main/book'} className='link_item'>
                    <img className='link_button' src={img4}/>
                    <img className='link_text e' src={text4}/>
                </Link>
                <Link to={'/main/festival'} className='link_item'>
                    <img className='link_button' src={img5}/>
                    <img className='link_text f' src={text5}/>
                </Link>
            </div>
        </div>
    </div>
  )
}

export default StartPage
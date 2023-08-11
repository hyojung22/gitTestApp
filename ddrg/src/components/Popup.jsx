import React from 'react'
import marker_icon from '../img/축제img/marker_icon.png'
import homepage_icon from '../img/축제img/homepage_icon.png'

const Popup = () => {

  return (
    <div className='popup'>
        {/* <p className='popup_firstContent'>
            지도 속에 전국의 명소와 전시회, 축제 등 다양한 관광지 정보가 들어 있습니다</p> */}
        <ol className='popup_secondContent'>
          <li>원하는 지역을 선택</li>
          <li><img src={marker_icon} alt='마커 아이콘' className='marker_icon'/>마커 클릭 시</li>
          <p className='popup_thirdContent'>(명소, 전시회, 축제 등 주변 관광지 이름, <br></br>기간, 장소, 홈페이지 정보 제공)</p>
          <li className='popup_fourthContent'><img src={homepage_icon} alt='마커 아이콘' className='homepage_icon'/>홈페이지 클릭 시 <br></br>해당 홈페이지로 이동</li>
        </ol>
    </div>
  )
}

export default Popup
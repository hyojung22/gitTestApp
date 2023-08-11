import React, {useState} from 'react'
import Kakao from '../components/Kakao'
import Popup from '../components/Popup'
import cat_festival from '../img/축제img/cat_festival1.png'

const M_festival = () => {
  const [isPopupOpen, setIsPopupOpen] = useState(false);

  const popupButton = () =>{
    isPopupOpen?setIsPopupOpen(false):setIsPopupOpen(true)
  }

  return (
    <div className='center'>
      <div className='festival_box'>
        {isPopupOpen && <Popup/>}
        <img 
        className='cat_festival' 
        src={cat_festival} alt='Cat Festival' 
        onClick={popupButton}/>
        <p className='festival_title_heading'>다양한 축제를 즐겨보세요.</p>
        <hr className='line'></hr>
        <div className='rounded_map'>
          <Kakao></Kakao>
        </div>
      </div>
    </div>
  )
}

export default M_festival
// components/RecipeDetail.js
import React, { useEffect } from 'react';
import './RecipeDetail.css';
import backImg from '../img/backButton.png'

function RecipeDetail({ recipe, onGoBack }) {
  const manualFields = Array.from({ length: 20 }, (_, index) => `MANUAL${String(index + 1).padStart(2, '0')}`);
  const manualImageFields = Array.from({ length: 20 }, (_, index) => `MANUAL_IMG${String(index + 1).padStart(2, '0')}`);

  const combinedContent = [];
  for (let i = 0; i < Math.max(manualFields.length, manualImageFields.length); i++) {
    if (recipe[manualImageFields[i]]) {
      combinedContent.push({ type: 'image', content: recipe[manualImageFields[i]] });
    }
    if (recipe[manualFields[i]]) {
      combinedContent.push({ type: 'text', content: recipe[manualFields[i]] });
    }
  }

  useEffect(()=>{
    window.scrollTo(0,0)
  },[])

  return (
    <div className='center'>
      <div className='cook_detailBox'>
        <div className='cook_detailBox1'>
          <button className='back-btn' onClick={onGoBack}>
            <img src={backImg}/>
          </button>
          <div className='cook_detailImg'>
            <img className='cook_imgBox' src={recipe.ATT_FILE_NO_MAIN} alt={`${recipe.RCP_NM} 이미지`} />
            <strong className='cook_name'>{recipe.RCP_NM}</strong>
            <hr/>
            <div className='cook_text_between'>
              <div className='cook_square'/>
              <strong className='cook_kind'>{recipe.RCP_PAT2}</strong>
              <div className='cook_square'/>
              <strong className='cook_how'>{recipe.RCP_WAY2}</strong>
            </div>
          </div>
        </div>
        <div className='cook_detailBox2'>
          <strong className='detail-ingredients_name'>| 재료 |</strong>
          <strong className='detail-ingredients'>{recipe.RCP_PARTS_DTLS}</strong>
          {combinedContent.map((item, index) => (
            item.type === 'text' 
            ? <div className='cook_detail_text' key={`${recipe.RCP_SEQ}-${index}`}>{item.content}</div> 
            : <img className='cook_detail_img' src={item.content} alt={`만드는 법 이미지 ${index}`} />
          ))}
        </div>
      </div>

      
    </div>
  );
}

export default RecipeDetail;

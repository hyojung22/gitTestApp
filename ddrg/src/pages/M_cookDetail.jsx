// components/RecipeDetail.js
import React from 'react';
import './RecipeDetail.css';

function M_cookDetail({ recipe, onGoBack }) {
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

  return (
    <div>
      <button className='back-btn' onClick={onGoBack}>뒤로가기</button>
    <div className='detail-Box'>
      <div className='detail-small'>
        <div className='detail-Box2'>
          <h2 className='detail-title'>{recipe.RCP_NM}</h2>
          <div className='detail-imgbox'>
            <img className='detail-img' src={recipe.ATT_FILE_NO_MAIN} alt={`${recipe.RCP_NM} 이미지`} />
            <p className='detail-ingredients'>재료: {recipe.RCP_PARTS_DTLS}</p>
            <p className='detail-cook'>조리 방법: {recipe.RCP_WAY2}</p>
          </div>
        </div>

        <div className='detail-Box3'>
          <h2 className='detail-way-title'>만드는 법</h2>
          <div className='detail-order'>
            <div className='detail-order-box'>
              {combinedContent.map((item, index) => (
                item.type === 'text' ?
                  <div className='order-turn' key={`${recipe.RCP_SEQ}-${index}`}>{item.content}</div> :
                  <div className='detail-order-imgbox' key={`${recipe.RCP_SEQ}-${index}`}>
                    <img className='detail-order-img' src={item.content} alt={`만드는 법 이미지 ${index}`} />
                  </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
  );
}

export default M_cookDetail;

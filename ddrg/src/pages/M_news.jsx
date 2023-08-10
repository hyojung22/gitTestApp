import React, { useState, useEffect } from 'react';
import axios from 'axios'
const M_news = () => {
  const [data, setData] = useState([]); //데이터 변수 설정(받아올 변수)
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get("http://127.0.0.1:5021/news_list"); //get으로 result함수 server에서 axios로 받아옴 
        setData(result.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        // 오류 처리: 사용자에게 오류 메시지를 보여줄 수 있음
      }
    };
    
    fetchData();
  }, []);
  // 
  const toggleExpand = (index) => {
    // 해당 인덱스의 데이터 확장 여부를 토글
    const newData = [...data];
    newData[index].expanded = !newData[index].expanded;
    setData(newData);
  }

  return (
    <div>
      <ul className='news_mainText'>
        {data.map((item, index) => (
          item.prediction === 1 ? (
          <li key={item.id} className='news_box'>
            <div className='news-content'>
              {item.expanded ? item.content : item.content.slice(0, 100)}
              {item.expanded && item.content.length > 100 && <span>...</span>}
            </div>
            {!item.expanded && item.content.length > 100 && (
            <button className='show-more-button' onClick={() => toggleExpand(index)}>
              더 보기
              </button>)}
          </li>)  
          : null ))}
      </ul>
    </div>
  );
};

export default M_news
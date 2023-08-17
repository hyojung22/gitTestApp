import React, { useState, useEffect } from 'react';
import axios from 'axios'
const M_news = () => {
  const [data1, setData1] = useState([]);
  const [data2, setData2] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get("http://127.0.0.1:5021/news_list");
        setData1(result.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        // 오류 처리: 사용자에게 오류 메시지를 보여줄 수 있음
      }
    };
    
    fetchData();
  }, []);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get("http://127.0.0.1:5021/keyword_list");
        setData2(result.data);
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
    const newData = [...data1];
    newData[index].expanded = !newData[index].expanded;
    setData1(newData);
  }

 /** 랜덤으로 3~5개 가져오기 굉장히 짧게. 가볍게 볼 수 있게, 
  *  제목은 
  *  커뮤니티는 팝업창처럼 
  * 
  */
  return (
    <div className='container'>
      {/* news container */}
      <div className='left-content'>
        <ul className='news_mainText'>
          {data1.map((item, index) => (
            item.prediction === 1 ? (
            <li key={item.id} className='news_box'>
              <div className='news-content'>
                {item.expanded ? item.content : item.content.slice(0, (item.content.indexOf('.')+14))}
                {!item.expanded && item.content.length > 100 && <span>...</span>}
              </div>
              <div className='more-box'>
              {!item.expanded && item.content.length > 50 && (
                <button className='show-more-button' onClick={() => toggleExpand(index)}>
                  더 보기
                </button>  
                )}
              {item.expanded && (
                <button className='show-more-button' onClick={() => toggleExpand(index)}>
                  줄이기
                </button>
              )}
              </div>
            </li>)  
            : null ))}
        </ul>
      </div>
      {/* data2 커뮤니티 키워드들 
      keyword에 저장되어있음. */}
      <div className='right-content'>
        <ul className='keywords_box'>
            {data2.slice(0, data2.length).map((item) => (
            <li className='keyword_text'>
              <a className="keyword_link" href={`https://www.google.com/search?q=${encodeURIComponent(item.keyword)}`} target="_blank" rel="noopener noreferrer">
                {item.keyword}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default M_news
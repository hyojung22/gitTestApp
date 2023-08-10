import React, { useState, useEffect } from 'react';
import axios from 'axios'
const M_news = () => {
  const [data, setData] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get("http://127.0.0.1:5021/news_list");
        setData(result.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        // 오류 처리: 사용자에게 오류 메시지를 보여줄 수 있음
      }
    };
    
    fetchData();
  }, []);

  return (
    <ul>
      {data.map((item) => (
        item.prediction === 1 ? (
          <li key={item.id}>
            {item.content}
          </li>
        ) : null
      ))}
    </ul>
  );
};

export default M_news
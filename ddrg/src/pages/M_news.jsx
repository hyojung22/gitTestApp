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

  return (
    <ul>
       {data2.map((item) => (
          <li>
            {item.keyword[0]}
          </li>
      ))}
      {data1.map((item) => (
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
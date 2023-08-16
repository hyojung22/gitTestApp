import React, { useState, useEffect } from 'react';
import { Map, MapMarker, CustomOverlayMap, MarkerClusterer } from 'react-kakao-maps-sdk';
import data from './data.json';
import axios from 'axios'

import './Kakao.css';

const Kakao = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedMarker, setSelectedMarker] = useState(null);

  // const positions = data.positions || [];

  const [positions, setPositions] = useState([]);
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get("http://127.0.0.1:5021/positions_list");
        setPositions(result.data);
      } catch (error) {
        console.error("Error fetching data:", error);
        // 오류 처리: 사용자에게 오류 메시지를 보여줄 수 있음
      }
    };
    
    fetchData();
  }, []);




  const markers = positions.map((position, index) => ({
    id: index,
    position: {
      lat: position.lat,
      lng: position.lng,
    },
  }));

  console.log(positions)
  const handleMarkerClick = (marker) => {
    setSelectedMarker(marker);
    setIsOpen(true);
  };

  return (
    <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
      <Map
        id={`map`}
        center={{
          lat: 37,
          lng: 127.93731667031574,
        }}
        style={{
          width: "1000px",
          height: "580px",
        }}
        level={14}
      >
        <MarkerClusterer averageCenter={true} minLevel={10}>
          {markers.map(marker => (
            <MapMarker
              key={marker.id}
              position={marker.position}
              onClick={() => handleMarkerClick(marker)}
            />
          ))}
        </MarkerClusterer>

        {isOpen && selectedMarker && (
          <CustomOverlayMap position={selectedMarker.position}>
            <div className="wrap">
              <div className="info">
                <div className="title">
                  {positions[selectedMarker.id]?.contents.slice(0,20)}
                  <div
                    className="close"
                    onClick={() => setIsOpen(false)}
                    title="닫기"
                  ></div>
                </div>
                <div className="body">
                  <div className="desc">
                    {/* <div className="content">
                      {positions[selectedMarker.id]?.contents} 
                    </div> */}
                    <div className="period content">
                      {positions[selectedMarker.id]?.period}
                    </div>
                    <div className="location">
                      {positions[selectedMarker.id]?.location}
                    </div>
                    <div>
                      <a
                        href={positions[selectedMarker.id]?.page_url}
                        target="_blank"
                        className="link"
                        rel="noreferrer"
                      >
                        홈페이지
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </CustomOverlayMap>
        )}
      </Map>
    </div>
  );
}

export default Kakao;

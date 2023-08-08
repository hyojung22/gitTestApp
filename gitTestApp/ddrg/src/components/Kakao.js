import React, { useState, useEffect } from 'react';
import { Map, MapMarker, CustomOverlayMap, MarkerClusterer} from 'react-kakao-maps-sdk';
import data from './data.json';
import './Kakao.css'

const Kakao = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [selectedMarker, setSelectedMarker] = useState(null) // 선택된 마커의 정보 저장하기 위한 state

  // 데이터에서 가져온 positions 객체
  const positions = data.positions;

  // 처음에는 빈 배열로 시작합니다.
  const [markers, setMarkers] = useState([]);

  // 컴포넌트가 마운트될 때 데이터를 가져와서 마커 생성
  useEffect(() => {
    // positions 객체가 유효한지 확인합니다.
    if (positions && Array.isArray(positions)) {
      const markerList = positions.map((position, index) => ({
        id: index, // 마커를 구별하기 위한 ID (필요에 따라 다른 유니크한 값으로 변경 가능)
        position: {
          lat: position.lat,
          lng: position.lng,
        },
      }));

      setMarkers(markerList);
    }
  }, [positions]);

  // 마커를 클릭할 때 호출되는 함수
  const handleMarkerClick = (marker) => {
    setSelectedMarker(marker) // 선택된 마커 정보를 설정
    setIsOpen(true) // 오버레이를 표시하기 위해 isOpen을 true로 설정
  }

  return (
    <div style={{display: "flex", justifyContent: "center", alignItems: "center",}}>
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
          {/* 순회하며 모든 마커를 렌더링 */}
          {markers.map(marker => (
            <MapMarker
              key={marker.id}
              position={marker.position}
              // 각 마커를 클릭하면 handleMarkerClick 함수 호출하여 선택된 마커 정보 설정
              onClick={() => handleMarkerClick(marker)} 
            />
          ))}
        </MarkerClusterer>
        
        {/* 선택된 마커에 대한 오버레이 */}
        {isOpen && selectedMarker && (
          <CustomOverlayMap position={selectedMarker.position}>
            {/* 사용자 정의 오버레이 내용 */}
            <div className="wrap">
              <div className="info"> 
                    <div className="title">
                          {positions[selectedMarker.id].title}  
                        <div 
                          className="close" 
                          onClick={() => setIsOpen(false)} 
                          title="닫기"
                        ></div>
                      </div>
                      <div className="body">
                          <div className="desc">
                              <div className="content"> 
                                {positions[selectedMarker.id].contents} 
                              </div>
                              <div className="period content"> 
                                {positions[selectedMarker.id].period}
                              </div>
                              <div className="location">
                                {positions[selectedMarker.id].location}
                              </div>
                              <div>
                                <a 
                                  href={positions[selectedMarker.id].page_url}
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
import React from 'react';
import Cap from '../components/cloth/Cap.jsx';

const M_fashion = () => {
  const max_height = window.innerHeight-100
  const cap_height = max_height

  return (
    <div className='fashion_range' style={{
      height:max_height
      }}>
      <div className='fashion_cap' style={{
        height:cap_height,
        backgroundColor:'black'
      }}>
        <Cap></Cap>
      </div>
    </div>
  )
}

export default M_fashion
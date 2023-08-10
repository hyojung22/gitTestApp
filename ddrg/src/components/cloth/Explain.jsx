import React from 'react'

const Explain = ({explainInfo, explainEnd}) => {

  const style = {
    display : 'flex',
    flexDirection: 'column',
    justifyContent : 'center',
    alignItems : 'center',

    position : 'absolute',
    width : '100%',
    height : '100%'
  }
  const back = {
    width : '80%',
    height : '30%',
    opacity : '0.7',
    backgroundColor : '#3e448b'
  }
  const groub = {
    display : 'flex',
    alignItems : 'center',
    width : '80%',
    height : '30%',
    position : 'absolute'
  }
  console.log(explainInfo[4]);
  // const img = require(`${explainInfo[4]}`)
  const img = require('../../img/패션img/모자/모자1.jpg')

  const handleEnd = () =>{
    explainEnd(false)
  }
  const endStyle = {
    position : 'absolute',
    right : '10%',
    bottom : '35%',
    width : '8vh',
    height : '8vh',
    backgroundColor : 'black'
  }
  return (
    <div style={style}>
      <div style={back}/>
      <div style={groub}>
        <img className='fashion_ex_img' src={img}/>
        <div className='fashion_ex_text'>
          <div className='fashion_ex'>이름 : {explainInfo[2]}</div>
          <div className='fashion_ex'>브랜드 : {explainInfo[1]}</div>
          <div className='fashion_ex'>가격 : {explainInfo[0]}</div>
          <div className='fashion_ex'><a href={explainInfo[3]} style={{textDecoration: 'none'}}>바로가기</a></div>
        </div>
      </div>
      <div onClick={handleEnd} style={endStyle}/>
    </div>
  )
}

export default Explain
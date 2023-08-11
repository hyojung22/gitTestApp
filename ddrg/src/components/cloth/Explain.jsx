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
  const cover = {
    position : 'absolute',
    width : '100%',
    height : '100%',
    opacity : '0.4',
    backgroundColor : 'gray'
  }
  const backBlur = {
    position : 'absolute',
    width : '100%',
    height : '100%',
    backdropFilter: 'blur(10px)'
  }
  const back = {
    position : 'absolute',
    borderRadius: '20px',
    width : '80%',
    height : '30%',
    backgroundColor : 'white'
  }
  const groub = {
    display : 'flex',
    alignItems : 'center',
    width : '80%',
    height : '30%',
    position : 'absolute'
  }
  const img = explainInfo[4]

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
      <div style={cover}/>
      <div style={backBlur}/>
      <div style={back}/>
      <div style={groub}>
        <img className='fashion_ex_img' src={img}/>
        <div className='fashion_ex_text'>
          <div className='fashion_ex a'>이름 : {explainInfo[2]}</div>
          <div className='fashion_ex b'>브랜드 : {explainInfo[1]}</div>
          <div className='fashion_ex c'>가격 : {explainInfo[0]}</div>
          <div className='fashion_ex'><a href={explainInfo[3]} style={{textDecoration: 'none'}}>바로가기</a></div>
        </div>
      </div>
      <div onClick={handleEnd} style={endStyle}/>
    </div>
  )
}

export default Explain
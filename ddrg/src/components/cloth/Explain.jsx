import React from 'react';
import tag from '../../img/패션img/explain_tag.png';
import earth from '../../img/패션img/homepage_icon.png';

const Explain = ({explainInfo, explainEnd}) => {

  const style = { // main center
    display : 'flex',
    flexDirection: 'column',
    justifyContent : 'center',
    alignItems : 'center',

    position : 'absolute',
    width : '100%',
    height : '100%'
  }
  const cover = { // 반투명 배경
    position : 'absolute',
    width : '100%',
    height : '100%',
    opacity : '0.4',
    backgroundColor : '#3e448b'
  }
  // const backBlur = { // 배경 블러
  //   position : 'absolute',
  //   width : '100%',
  //   height : '100%',
  //   backdropFilter: 'blur(1px)'
  // }
  const backTag = { // 흰 사각형
    position : 'absolute',
    borderRadius: '20px',
    width : '50vh',
    height : '100%',
  }
  const contentBox = { // contentBox
    display : 'flex',
    flexDirection : 'column',
    alignItems : 'center',
    width : '38vh',
    maxWidth : '100vw',
    height : '80%',
    position : 'absolute',
    top: '25%',
    // transform: 'rotate(-4deg)',
  }
  const img = explainInfo[4]

  const handleEnd = () =>{
    explainEnd(false);
  }

  return (
    <div style={style} onClick={handleEnd}>
      <div style={cover}/>
      {/* <div style={backBlur}/> */}
      <img style={backTag} src={tag}/>
      <div style={contentBox}>
        <img className='fashion_ex_img' src={img}/>
        <div className='fashion_ex_text'>
          <div className='fashion_ex a'>{explainInfo[2]}</div>
          <div className='fashion_ex b'>{explainInfo[1]}</div>
          <div className='fashion_exGroup'>
            <div className='fashion_ex c'>{explainInfo[0]}</div>
            <div className='fashion_ex'>
              <a href={explainInfo[3]}>
                <img src={earth} style={{height:'5vh'}}/>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Explain
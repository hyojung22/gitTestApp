import React from 'react'

const Bottom = () => {

  const array = []
  for(let i=1;i<91;i++){
    array.push(i)
  }
  const capArr = array.map((e)=>{
    return require(`../../img/패션img/하의/하의${e}.jpg`)
  })

  return (
    <div style={{
      display:'flex',
      height:'100%'
    }}>
      {capArr.map((e, index)=>
        (<img key={index} src={e} className='fashion_item'/>)
      )}
    </div>
  )
}

export default Bottom
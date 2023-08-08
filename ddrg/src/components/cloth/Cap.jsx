import React from 'react'

const Cap = () => {
<<<<<<< HEAD

  const array = []
  for(let i=1;i<91;i++){
    array.push(i)
  }
  const capArr = array.map((e)=>{
    return require(`../../img/패션img/모자/모자${e}.jpg`)
  })

  return (
    <div style={{
      display:'flex',
      height:'100%'
    }}>
      {capArr.map((e, index)=>
        (<img key={index} src={e} className='fashion_item'/>)
      )}
=======
  return (
    <div>
<<<<<<< HEAD:ddrg/src/pages/M_cook.jsx
      <h3>요리</h3>
=======

>>>>>>> 961b13ac3122aa382d546700fd7e0889d78c892b:ddrg/src/components/cloth/Cap.jsx
>>>>>>> 0d37c9426adaf19d9d6cae4bb6ce46cc0f6f41c5
    </div>
  )
}

export default Cap
import './App.css';
import { Routes, Route, useLocation } from 'react-router-dom';

import Logo from './components/Logo';
import StartPage from './pages/StartPage';
import M_book from './pages/M_book'
import M_cook from './pages/M_cook';
import M_cookDetail from './pages/M_cookDetail';
import M_fashion from './pages/M_fashion';
import M_news from './pages/M_news';
import M_festival from './pages/M_festival.jsx';
import NotFound from './pages/NotFound';
// 도서 파트 json은 ../pages/M_book.jsx 에서 import
// 패션 파트 json은 ../components/cloth/Item.jsx 에서 import
// 축제 파트 json은 ../components/Kakao.js 에서 import


function App() {

  const location = useLocation();
  const logoView = !(location.pathname === '/')


  return (
    <div className='app'>
      {logoView && <Logo location={location}/>}
      {/* {logoView && <LogoMenu location={location} style={{position:'absolute'}}/>} */}
      <Routes>
        <Route path='/' element={<StartPage/>}/>
        <Route path='/main/festival' element={<M_festival/>}/>
        <Route path='/main/book' element={<M_book/>}/>
        <Route path='/main/fashion' element={<M_fashion/>}/>
        <Route path='/main/cook' element={<M_cook/>}/>
        <Route path='/main/cook/detail' element={<M_cookDetail/>}/>
        <Route path='/main/news' element={<M_news/>}/>
        <Route path='*' element={<NotFound/>}/>
      </Routes>
    </div>
  );
}

export default App;
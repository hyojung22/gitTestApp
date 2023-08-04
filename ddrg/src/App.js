import './App.css';
import { Routes, Route, useLocation } from 'react-router-dom';

import Logo from './components/Logo';
import FirstPage from './pages/FirstPage';
import Main from './pages/Main';
import M_book from './pages/M_book'
import M_cook from './pages/M_cook';
import M_fashion from './pages/M_fashion';
import M_news from './pages/M_news';
import M_traval from './pages/M_traval';
import NotFound from './pages/NotFound';


function App() {

  const location = useLocation();
  const logoView = !(location.pathname === '/')
  
  return (
    <div className='app'>
      {logoView && <Logo/>}
      <Routes>
        <Route path='/' element={<FirstPage/>}/>
        <Route path='/main' element={<Main/>}/>
        <Route path='/main/traval' element={<M_traval/>}/>
        <Route path='/main/book' element={<M_book/>}/>
        <Route path='/main/fashion' element={<M_fashion/>}/>
        <Route path='/main/cook' element={<M_cook/>}/>
        <Route path='/main/news' element={<M_news/>}/>
        <Route path='*' element={<NotFound/>}/>
      </Routes>
    </div>
  );
}

export default App;
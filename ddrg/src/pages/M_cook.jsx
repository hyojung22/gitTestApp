import React, { useState, useEffect } from 'react';
import { fetchInitialRecipes } from '..//etc/api';
import './RecipeSearch.css';
import RecipeDetail from './RecipeDetail.jsx';

import cookCharacter from '../img/요리img/character.png'
import searchIcon from '../img/요리img/search.png';

function RecipeSearch() {
  const [ingredients, setIngredients] = useState('');
  const [recipes, setRecipes] = useState([]);
  const [error, setError] = useState(null);

  const [selectedRecipe, setSelectedRecipe] = useState(null); // 선택한 레시피 상태 추가
  const [loadedRecipes, setLoadedRecipes] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const initialRecipes = await fetchInitialRecipes();
        setLoadedRecipes(initialRecipes);
      } catch (error) {
        setError('레시피 데이터를 불러오는 중 오류가 발생했습니다.');
      }
    }
    fetchData();
  }, []);

  const handleEnterPress = e =>{
    if(e.key == 'Enter'){
      handleSearch()
    }
  }

  const handleSearch = async () => {
    if (!ingredients) {
      return;
    }

    try {
      setError(null);
      const filtered = loadedRecipes.filter(recipe => {
        const recipeIngredients = recipe.RCP_PARTS_DTLS.toLowerCase();
        const searchIngredients = ingredients.toLowerCase();
        setSelectedRecipe(null);
        return recipeIngredients.includes(searchIngredients);
      });
      setRecipes(filtered);
    } catch (error) {
      console.error('레시피 검색 에러:', error);
      setError('레시피 검색 중 오류가 발생했습니다.');
      setRecipes([]);
    }
  };

  const handleRecipeClick = (recipe) => {
    setSelectedRecipe(recipe);
  };

  const goBack = () => {
    setSelectedRecipe(null);
  }

  // 초기화면
  const [searchBlank, setSearchBlank] = useState(false);
  useEffect(()=>{
    if(ingredients==''&&recipes.length==0){
      setSearchBlank(false)
    }else {
      setSearchBlank(true)
    }
  }, [ingredients])

  useEffect(()=>{
    window.scrollTo(0,0)
  },[])

  return (
    <div className='center'>
        {/* 검색한 레시피 표시 */}
        {selectedRecipe 
        ? (<RecipeDetail recipe={selectedRecipe} onGoBack={goBack} />) 
        : (
          <div className='cook_bigBox'>
            <div className={searchBlank ? 'cook_topBox' : 'cook_topBox_first'}>
              {!searchBlank && <img className='cookCharacter_first' src={cookCharacter}/>}
              <div className='cook_searchBox'>
                <img className='cook_searchIcon' src={searchIcon}/>
                <input className='cook_search'
                  type="text"
                  value={ingredients}
                  onChange={(e) => setIngredients(e.target.value)}
                  onKeyDown={handleEnterPress}
                  placeholder="재료를 입력하세요"
                />
              </div>
              {searchBlank && <img className='cookCharacter' src={cookCharacter}/>}
            </div>
            <div className='resultList'>
              {recipes.map((recipe) => (
                <div className='cook_ilBox' key={recipe.RCP_SEQ}>
                  <button className='cook_atag' onClick={() => handleRecipeClick(recipe)}>
                    <img className='cook_imgBox' src={recipe.ATT_FILE_NO_MAIN} alt={`${recipe.RCP_NM} 이미지`} />
                    <strong className='cook_name'>{recipe.RCP_NM}</strong>
                    <hr/>
                    <div className='cook_text_between'>
                      <div className='cook_square'/>
                      <strong className='cook_kind'>{recipe.RCP_PAT2}</strong>
                      <div className='cook_square'/>
                      <strong className='cook_how'>{recipe.RCP_WAY2}</strong>
                    </div>
                  </button>
                </div>
              ))}
            </div>
          </div>
        )}
    </div>
  );
}

export default RecipeSearch;

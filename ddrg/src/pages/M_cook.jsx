import React, { useState, useEffect } from 'react';
import { fetchInitialRecipes } from '..//etc/api';
import './RecipeSearch.css';
import RecipeDetail from './RecipeDetail';

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


  return (
    <div className='fullBox'>
      <div className='bigBox'>
        <h1 className='title'>레시피 검색</h1>
        <div className='flexContainer'>
          <div className='leftBox'>
            <div className='search-Box'>
              <input className='search-Box2'
                type="text"
                value={ingredients}
                onChange={(e) => setIngredients(e.target.value)}
                placeholder="재료를 입력하세요"
              />
              {/* 재료 검색 버튼 */}
              <button className='search-btn' onClick={handleSearch}>검색</button>
            </div>

            {/* 검색한 레시피 표시 */}
            {selectedRecipe ? (
              <RecipeDetail recipe={selectedRecipe} onGoBack={goBack} />
            ) : (
              <div className='title-Box'>
                <h2 className='resultName'>요리 검색 결과</h2>
                <div className='resultList'>
                  {recipes.map((recipe) => (
                    <div className='ilBox' key={recipe.RCP_SEQ}>
                      <div className='contentBox'>
                        <button className='atag' onClick={() => handleRecipeClick(recipe)}>
                          <img className='imgBox' src={recipe.ATT_FILE_NO_MAIN} alt={`${recipe.RCP_NM} 이미지`} />
                          <p className='cookBox1'>{recipe.RCP_NM}</p>
                          <p className='matBox1'>요리종류 : {recipe.RCP_PAT2}</p>
                          <p className='matBox2'>조리 방법 : {recipe.RCP_WAY2}</p>
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default RecipeSearch;

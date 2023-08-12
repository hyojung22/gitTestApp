// api.js
import axios from 'axios';

const API_KEY = '9f47ae2803314f05bd47';
const BASE_URL = 'https://openapi.foodsafetykorea.go.kr/api';

// 초기 레시피 데이터를 미리 불러오는 함수
export async function fetchInitialRecipes() {
  try {
    const response = await axios.get(
      `${BASE_URL}/${API_KEY}/COOKRCP01/json/1/1000`
    );
    return response.data.COOKRCP01.row;
  } catch (error) {
    console.error('초기 레시피 불러오기 에러:', error);
    throw error;
  }
}

// 재료로 레시피 검색하는 함수
export async function searchRecipesByIngredients(ingredients) {
  try {
    const response = await axios.get(
      `${BASE_URL}/${API_KEY}/COOKRCP01/json/1/1000?q=${encodeURIComponent(ingredients)}`
    );
    const jsonData = response.data.COOKRCP01.row;

    const filteredRecipes = jsonData.filter(recipe => {
      const recipeIngredients = recipe.RCP_PARTS_DTLS.toLowerCase();
      const searchIngredients = ingredients.toLowerCase();
      return recipeIngredients.includes(searchIngredients);
    });

    return filteredRecipes;
  } catch (error) {
    console.error('레시피 검색 에러:', error);
    throw error;
  }
}

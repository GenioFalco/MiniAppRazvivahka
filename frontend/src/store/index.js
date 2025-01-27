import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
  state: {
    user: null,
    tasks: [],
    categories: [],
    currentCategory: null,
    loading: false,
    error: null
  },
  
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
    SET_TASKS(state, tasks) {
      state.tasks = tasks;
    },
    SET_CATEGORIES(state, categories) {
      state.categories = categories;
    },
    SET_CURRENT_CATEGORY(state, category) {
      state.currentCategory = category;
    },
    SET_LOADING(state, loading) {
      state.loading = loading;
    },
    SET_ERROR(state, error) {
      state.error = error;
    }
  },
  
  actions: {
    async initializeApp({ commit }) {
      try {
        commit('SET_LOADING', true);
        // Инициализация данных из Telegram Mini App
        if (window.Telegram?.WebApp) {
          const user = window.Telegram.WebApp.initDataUnsafe?.user;
          commit('SET_USER', user);
        }
        
        // Загрузка категорий с бэкенда
        const response = await axios.get('/api/categories');
        commit('SET_CATEGORIES', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    
    async fetchTasks({ commit }, categoryId) {
      try {
        commit('SET_LOADING', true);
        const response = await axios.get(`/api/categories/${categoryId}/tasks`);
        commit('SET_TASKS', response.data);
      } catch (error) {
        commit('SET_ERROR', error.message);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    
    async submitTask({ commit }, { taskId, answer }) {
      try {
        commit('SET_LOADING', true);
        const response = await axios.post(`/api/tasks/${taskId}/submit`, { answer });
        return response.data;
      } catch (error) {
        commit('SET_ERROR', error.message);
        throw error;
      } finally {
        commit('SET_LOADING', false);
      }
    }
  },
  
  getters: {
    isAuthenticated: state => !!state.user,
    userProgress: state => state.user?.progress || {},
    categoryTasks: state => categoryId => {
      return state.tasks.filter(task => task.categoryId === categoryId);
    }
  }
}) 
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    indexNavSlide: Number,
    fetchData: Array,
  },
  getters: {
    getIndex(state) {
      return state.indexNavSlide
    },
    getData(state){
      return state.fetchData
    }
  },
  mutations: {
    updateIindexNavSlide(state, index) {
      state.indexNavSlide = index
    },
    updatefetchData(state, data) {
      state.fetchData = data
    },
  },
  actions: {

  }
})

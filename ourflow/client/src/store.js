import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    indexNavSlide: Number,
    sizeSlider: Number,
  },
  getters: {
    getIndex(state) {
      return state.indexNavSlide
    },
    getSize(state){
      return state.sizeSlider
    }
  },
  mutations: {
    updateIindexNavSlide(state, index) {
      state.indexNavSlide = index
    },
    updateSizeSlider(state, size) {
      state.sizeSlider = size
    },
  },
  actions: {

  }
})

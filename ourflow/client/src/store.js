import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    indexNavSlide:0,
    facticeSlide:Array
  },
getters: {
    getIndex(state) {
      return state.indexNavSlide
    },
    getSlides(state){
      return state.facticeSlide
    }
},
  mutations: {
    updateIindexNavSlide(state, index){
      state.indexNavSlide = index
    },
    updateFacticeSlide(state, array){
      state.facticeSlide = array
    }
  },
  actions: {

  }
})

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    indexNavSlide: Number,
    sizeScreen:Number,
    fetchData: Array,
    fetchDataSlide: Array,
  },
  getters: {
    getIndex(state) {
      return state.indexNavSlide
    },
    getData(state) {
      return state.fetchData
    },
    getDataSlide(state) {
      return state.fetchDataSlide
    },
    getSize(state){
      return state.sizeScreen
    }
  },
  mutations: {
    updateSizeScreen(state, size){
      state.sizeScreen = size
    },
    updateIindexNavSlide(state, index) {
      state.indexNavSlide = index
    },
    updatefetchData(state, data) {
      var arr = []
      data.map((valpage, j) => {
        valpage.paragraph.map((valpara, i) => {
          if (valpara.type = "slide") {
            arr.push(data[j].paragraph[i])
            delete data[j].paragraph[i]
          }
        })
      })
      state.fetchDataSlide = arr
      state.fetchData = data
    },
  },
  actions: {

  }
})

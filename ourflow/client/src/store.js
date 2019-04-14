import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    indexNavSlide: Number,
    sizeScreen: Number,
    fetchData: Array,
    fetchDataSlide: Array,
    fetchPage: []
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
    getSize(state) {
      return state.sizeScreen
    },
    getPage(state) {
      return state.fetchPage
    },
  },
  mutations: {
    setSizeScreen(state, size) {
      state.sizeScreen = size
    },
    setIndex(state, index) {
      state.indexNavSlide = index
    },
    setfetchData(state, data) {
      var arr = []
      var arr2 = []
      data.map((valpage, j) => {
        state.fetchPage.push(valpage.title_page.toLowerCase())
        valpage.paragraph.map((valpara, i) => {
          if (valpara.type === "slide") {
            arr.push(data[j].paragraph[i])
            delete data[j].paragraph[i]
          }else{
            arr2.push(data[j].paragraph[i])
          }
        })
        data[j].paragraph = arr2
        arr2=[]
      })
      state.fetchData = data
      state.fetchDataSlide = arr
    },
  },
  actions: {

  }
})

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    indexNavSlide: Number,
    sizeScreen: Number,
    fetchData: Array,
    fetchDataSlide: Array,
    fetchDataCoordinate: Object,
    loaded: 0,
    fetchPage: []
  },
  getters: {
    getLoaded(state) {
      return state.loaded
    },
    getDataCoordinate(state) {
      return state.fetchDataCoordinate
    },
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
    setLoaded(state, percentage) {
      state.loaded = percentage
    },
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
          switch (valpara.type.toLowerCase()) {
            case "slide":
              arr.push(data[j].paragraph[i])
              delete data[j].paragraph[i]
              break;
              case "coordinate":
                state.fetchDataCoordinate = data[j].paragraph[i]
                delete data[j].paragraph[i]
                break;
            default:
              arr2.push(data[j].paragraph[i])
              break;
          }
        })
        data[j].paragraph = arr2
        arr2 = []
      })
      state.fetchData = data
      state.fetchDataSlide = arr
    },
  },
  actions: {

  }
})

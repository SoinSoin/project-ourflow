import baseURL from './index.js'
import store from '../store'
var routeApi = '/'
// if (process.env.NODE_ENV !== 'production')
//   routeApi = '/?format=json'


export default {
  async getAllPage() {
    return await baseURL().get(`/api/page${routeApi}`, {
      onDownloadProgress: function (progressEvent) {
        var loaded = store.getters.getLoaded
        var toLoad = Math.floor((progressEvent.loaded * 100) / progressEvent.total)
        var dynamicLoad = () => {
          if (loaded < toLoad) {
            loaded++
            store.commit("setLoaded", loaded)
          } else {
            clearInterval(dynamicLoad);
          }
        }
        setInterval(dynamicLoad, 24)
      }
    })
  },
  async setSendMail(dataMail) {
    return await baseURL().post('/mail/send/', dataMail, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    })
  }
}

import baseURL from './index.js'
import store from '../store'
var routeApi = '/'
if (process.env.NODE_ENV !== 'production')
  routeApi = '/?format=json'


export default {
  async getAllPage() {
    return await baseURL().get(`/api/page${routeApi}`, {
      onDownloadProgress: function (progressEvent) {
        store.commit("setLoaded", Math.floor((progressEvent.loaded * 100) / progressEvent.total))
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

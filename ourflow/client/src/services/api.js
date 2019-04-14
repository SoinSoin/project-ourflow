import baseURL from './index.js'
export default {
  async getAllPage() {
    return await baseURL().get('/api/page/?format=json')
  },
  async setSendMail(dataMail){
    return await baseURL().post('/mail/send/',dataMail, {
      headers:{
        'Content-Type':'application/x-www-form-urlencoded'
      }
    })
  }
}

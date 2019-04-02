import baseURL from './index.js'
export default {
  async getAllPage() {
    return await baseURL().get('/page/?format=json')
  },
  async getNav() {
    return await baseURL().get('/paragraph/title/nav/?format=json')
  },
}

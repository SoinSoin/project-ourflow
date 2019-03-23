import baseURL from './index.js'
export default {
  async getAllPage() {
    return await baseURL().get('/page/?format=json')
  },
}

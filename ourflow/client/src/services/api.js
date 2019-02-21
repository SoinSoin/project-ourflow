import baseURL from './index.js'
export default {
  async getExample() {
    return await baseURL().get('/example')
  },
}

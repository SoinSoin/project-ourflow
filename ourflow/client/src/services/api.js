import baseURL from './index'

export default {
  async exampleMethode() {
    return await baseURL().get('/routeAPI')
  },
}

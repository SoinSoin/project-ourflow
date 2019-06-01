import axios from 'axios' 
export default () => {
  return axios.create({
      baseURL: 'https://api.ourflow.fr'
    })
  }
  // `${window.location.protocol}${process.env.VUE_APP_BASE_API}`
  
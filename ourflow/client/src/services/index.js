import axios from 'axios' 
export default () => {
  return axios.create({
      baseURL: `${window.location.protocol}${process.env.VUE_APP_BASE_API}`
    })
  }

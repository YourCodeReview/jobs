import axios from 'axios'

const IS_LOCAL = true
const LOCAL_URL = 'http://localhost:8000/api/'

const axiosInstance = axios.create({
  baseURL: IS_LOCAL ? LOCAL_URL : '/api/'
})

export default axiosInstance

import axios from 'axios'

const IS_LOCAL = true
const LOCAL_URL = 'http://127.0.0.1:8000/api/'

const axiosInstance = axios.create({
  baseURL: IS_LOCAL ? LOCAL_URL : 'https://jobs.yourcodereview.com:8000/api/'
})

export default axiosInstance

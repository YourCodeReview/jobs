import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'http://68.183.220.246:8000/api/jobs/'
})

export default axiosInstance
import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'https://68.183.220.246:8000/api/jobs/'
})

export default axiosInstance

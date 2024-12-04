import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'https://jobs.yourcodereview.com/api/'
})

export default axiosInstance

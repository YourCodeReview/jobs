import axios from 'axios'

const axiosInstance = axios.create({
  baseURL: 'https://jobs.yourcodereview.com:8000/api/jobs/'
})

export default axiosInstance

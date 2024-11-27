import axiosInstance from '@/services/axiosInstance'

export const apiService = {
  async getCurrentVacancy(id) {
    return (await axiosInstance.get(`jobs/${id}`)).data
  },
  async getJobs(params) {
    return (await axiosInstance.get('jobs/?', { params })).data
  },
  async getAllLocations() {
    return (await axiosInstance.get('locations')).data
  },
  async addJob(data) {
    return (await axiosInstance.post('jobs', data, {
        headers: {
          'Content-Type': 'application/json'
        }
    })).data
  },
  async register(data) {
    return (await axiosInstance.post('register', data, {
        headers: {
          'Content-Type': 'application/json'
        }
    })).data
  },
  async getUuid() {
    return (await axios.get('https://review.gorbunov-ai.ru/auth/get-uuid/')).data
  },
  async getCheckAuth(uuid) {
    return (
      await axios.get('https://review.gorbunov-ai.ru/auth/check-uuid/', {
        params: { uuid_for_login: uuid }
      })
    ).data  
  },
}

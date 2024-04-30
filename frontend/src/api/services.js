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
  }
}

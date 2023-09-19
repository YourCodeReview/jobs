import axiosInstance from '@/services/axiosInstance'

export const apiService = {
  async getCurrentVacancy(id) {
    return (await axiosInstance.get(`${id}`)).data
  },
  async getJobs(params) {
    return (await axiosInstance.get('?', { params })).data
  }
}

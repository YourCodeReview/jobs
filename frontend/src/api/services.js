import axiosInstance from '@/services/axiosInstance'

export const apiService = {
  async getCurrentVacancy(id) {
    return (await axiosInstance.get(`${id}`)).data
  },
  async getJobs() {
    return (await axiosInstance.get('')).data
  }
}

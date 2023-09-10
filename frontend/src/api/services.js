import axiosInstance from '@/services/default'

export const apiService = {
  async getCurrentVacancy(id) {
    return (await axiosInstance.get(`${id}`)).data
  },
  async getJobs() {
    return (await axiosInstance.get('')).data
  }
}
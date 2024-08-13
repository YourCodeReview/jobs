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
  async isUserCanAddNewVacancy(userId) {
    return (await axiosInstance.get(`users/${userId}/can-create-vacancy`)).data // запрос на право создавать вакансии !!! TODO `users/${userId}/can-create-vacancy` согласовать этот API с бекендом или изменить по договоренности Должен возвращать true/false
  }
}

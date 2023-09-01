import axiosInstance from '../services/default'

export const apiService = {
  async getVacancies(params) {
    return (await axiosInstance.get('', { params })).data
  }
}
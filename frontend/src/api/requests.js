import { apiService } from '@/api/services'
import { useRequest } from '@/hooks/useRequest'

export const useGetVacancy = () => {
  return useRequest(apiService.getCurrentVacancy)
}

export const useGetJobs = () => {
  return useRequest(apiService.getJobs)
}
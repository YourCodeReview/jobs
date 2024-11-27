import { apiService } from '@/api/services'
import { useRequest } from '@/hooks/useRequest'

export const useGetVacancy = () => {
  return useRequest(apiService.getCurrentVacancy)
}

export const useGetJobs = () => {
  return useRequest(apiService.getJobs)
}

export const useGetLocations = () => {
  return useRequest(apiService.getAllLocations)
}

export const useAddJob = () => {
  return useRequest(apiService.addJob)
}

export const useRegister = () => {
  return useRequest(apiService.register)
}

export const useGetUuid = () => {
  return useRequest(apiService.getUuid)
}

export const useCheckAuth = () => {
  return useRequest(apiService.getCheckAuth)
}
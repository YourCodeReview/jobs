import { apiService } from '../api/services'
import { useRequest } from '../hooks/useRequest'

export const useGetVacancies = () => {
  return useRequest(apiService.getVacancies)
}
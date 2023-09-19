import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useGetVacancy } from '@/api/requests'

export const useVacancyStore = defineStore('vacancy', () => {
  const { data, loading, error, execute } = useGetVacancy()

  const vacancy = computed(() => data.value)

  const currentId = ref(null)

  const fetchVacancyData = async () => {
    await execute(currentId.value)
  }

  const changeId = (newValue) => {
    currentId.value = newValue
    fetchVacancyData()
  }

  return {
    currentId,
    changeId,
    vacancy,
    loading,
    error
  }
})

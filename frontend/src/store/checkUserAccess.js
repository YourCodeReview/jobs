import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useAddVacancies } from '@/api/requests'

export const useClientStore = defineStore('userAccess', () => {
  const { data, loading, error, execute } = useAddVacancies() // Запрос на проверку прав клиента на создание вакансий
  const userPermissions = computed(() => data.value)
  const clientId = ref(null) 

  // Функция для проверки прав клиента
  const checkClientPermissions = async () => {
    await execute(clientId.value)
  }

  const changeId = (newValue) => {
    clientId.value = newValue
    checkClientPermissions()
  }

  return {
    clientId,
    checkClientPermissions,
    changeId,
    userPermissions,
    loading,
    error
  }
})
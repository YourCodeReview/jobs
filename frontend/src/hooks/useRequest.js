import { ref } from 'vue'

export const useRequest = (requestFunction) => {
  const data = ref(null)
  const loading = ref(false)
  const error = ref('')

  const execute = async (params) => {
    loading.value = true
    try {
      data.value = await requestFunction(params)
    } catch (e) {
      error.value = e.response
      console.log(error.value)
    } finally {
      loading.value = false
    }
  }

  return {
    data,
    loading,
    error,
    execute
  }
}

import { ref } from 'vue'

export const useRequest = (requestFunction) => {
  const data = ref(null)
  const isLoading = ref(false)
  const isError = ref(false)

  const execute = async (params) => {
    isLoading.value = true
    try {
      data.value = await requestFunction(params)
    } catch(e) {
      isError.value = true
      console.log(e);
    } finally {
      isLoading.value = false
    }
  }

  return {
    data,
    isLoading,
    isError,
    execute
  }
}
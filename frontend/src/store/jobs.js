import { defineStore } from 'pinia'
import { ref, computed, onMounted  } from 'vue'
import { useGetJobs } from '@/api/requests'
import debounce from 'lodash.debounce'

export const useJobsStore = defineStore('jobs', () => {
  const { data, loading, error, execute } = useGetJobs()

  const list = computed(() => data.value)

  const fetchQuery = ref({
    skip: 0,
    limit: 10,
    specialities: null,
  })

  const fetchJobsData = async () => {
    await execute(fetchQuery.value)
    console.log(list.value);
    saveQueryToLocalStorage();
  }

  const fetchJobsDataWithDebounce = debounce(async () => {
    await execute(fetchQuery.value)
    saveQueryToLocalStorage();
  }, 1000)

  const changeQuery = (field, newValue) => {
    fetchQuery.value[field] = newValue
    saveQueryToLocalStorage();
  }

  const saveQueryToLocalStorage = () => {
    localStorage.setItem('jobsQuery', JSON.stringify(fetchQuery.value));
  }
  
  const restoreQueryFromLocalStorage = () => {
    const savedQuery = localStorage.getItem('jobsQuery');
    if (savedQuery) {
      fetchQuery.value = JSON.parse(savedQuery);
    }
  }

  onMounted(() => {
    restoreQueryFromLocalStorage();
  })

  return {
    fetchQuery,
    changeQuery,
    list,
    loading,
    error,
    fetchJobsData,
    fetchJobsDataWithDebounce,
  }
})
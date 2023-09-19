import { defineStore } from 'pinia'
import { ref, computed, onMounted, watch } from 'vue'
import { useGetJobs } from '@/api/requests'
import debounce from 'lodash.debounce'

export const useJobsStore = defineStore('jobs', () => {
  const { data, loading, error, execute } = useGetJobs()

  const list = computed(() => data.value)
  const listIsEmpty = computed(() => data.value?.total_count === 0)
  const pages = computed(() => Math.ceil(data.value?.total_count / 10) || 1)

  const fetchQuery = ref({
    skip: 0,
    limit: 10,
    specialities: null
  })

  const page = ref(1)

  const fetchJobsData = async () => {
    await execute(fetchQuery.value)
    saveQueryToLocalStorage()
  }

  const fetchJobsDataWithDebounce = debounce(async () => {
    await execute(fetchQuery.value)
    saveQueryToLocalStorage()
  }, 1000)

  const changeQuery = (field, newValue) => {
    fetchQuery.value[field] = newValue
    saveQueryToLocalStorage()
  }

  const saveQueryToLocalStorage = () => {
    localStorage.setItem('jobsQuery', JSON.stringify(fetchQuery.value))
    localStorage.setItem('page', JSON.stringify(page.value))
  }

  const restoreQueryFromLocalStorage = () => {
    const savedQuery = localStorage.getItem('jobsQuery')
    const savedPage= localStorage.getItem('page')
    if (savedQuery) {
      fetchQuery.value = JSON.parse(savedQuery)
    }
    if (savedPage) {
      page.value = JSON.parse(savedPage)
    }
  }

  watch(fetchQuery.value, () => {
    fetchJobsDataWithDebounce()
  })

  watch(page, () => {
    fetchQuery.value.skip = (page.value - 1) * 10
    fetchJobsDataWithDebounce()
  })

  onMounted(() => {
    restoreQueryFromLocalStorage()
  })

  return {
    fetchQuery,
    changeQuery,
    list,
    listIsEmpty,
    page,
    pages,
    loading,
    error,
    fetchJobsData,
    fetchJobsDataWithDebounce
  }
})

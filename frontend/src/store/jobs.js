import { defineStore } from 'pinia'
import { ref, computed, onMounted } from 'vue'
import { useGetJobs } from '@/api/requests'
import debounce from 'lodash.debounce'

export const useJobsStore = defineStore('jobs', () => {
  const { data, loading, error, execute } = useGetJobs()

  const list = computed(() => data?.value)
  const counter = computed(() => data?.value?.total_count)
  const listIsEmpty = computed(() => data?.value?.total_count === 0)
  const pages = computed(() => Math.ceil(counter.value / 10) || 1)

  const fetchQuery = ref({
    skip: 0,
    limit: 10,
    specialities: null
  })

  const page = ref(1)

  const fetchJobsData = async () => {
    await execute(fetchQuery.value)
    saveToLocalStorage()
  }

  const fetchJobsDataWithDebounce = debounce(async () => {
    await execute(fetchQuery.value)
    saveToLocalStorage()
  }, 1000)

  const changeQuery = (field, newValue) => {
    fetchQuery.value[field] = newValue
    saveToLocalStorage()
  }

  const saveToLocalStorage = () => {
    localStorage.setItem('jobsQuery', JSON.stringify(fetchQuery.value))
  }

  const getFromLocalStorage = () => {
    const savedQuery = localStorage.getItem('jobsQuery')
    if (savedQuery) {
      fetchQuery.value = JSON.parse(savedQuery)
      changeQuery('skip', 0)
    }
  }

  const editCurrentPage = () => {
    fetchQuery.value.skip = (page.value - 1) * 10
    fetchJobsData()
  }

  onMounted(() => {
    getFromLocalStorage()
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
    fetchJobsDataWithDebounce,
    editCurrentPage
  }
})

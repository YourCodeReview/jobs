import { useGetLocations } from '@/api/requests'
import { defineStore } from 'pinia'
import { computed, onMounted, ref } from 'vue'

export const useLocationsStore = defineStore('locations', () => {
  const { data, error, loading, execute } = useGetLocations()

  const fetchedList = computed(() => data?.value)
  const counter = computed(() => data?.value?.total_count)
  const listIsEmpty = computed(() => data?.value?.total_count === 0)

  const locationsList = ref([])

  const fetchLocations = async () => {
    await execute()
    locationsList.value = transformAndSortList(fetchedList.value.data)
  }

  const transformAndSortList = (list) => {
    const uniqueList = [...new Set(list.filter(Boolean).map((item) => item.split(',')[0]))]
    return [...uniqueList].sort((a, b) => a.localeCompare(b))
  }

  onMounted(() => {
    fetchLocations()
  })

  return {
    locationsList,
    error,
    loading,
    counter,
    listIsEmpty
  }
})

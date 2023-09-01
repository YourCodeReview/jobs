import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useModalStore = defineStore('modal', () => {
    const type = ref('')
    const isOpen = ref(false)

    const open = (status = 'login') => {
        type.value = status
        isOpen.value = true
    }

    const close = () => {
        isOpen.value = false
    }

    return { type, isOpen, open, close }
})

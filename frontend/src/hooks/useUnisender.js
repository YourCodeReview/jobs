import axios from 'axios'
import { ref } from 'vue'

const apiKey = import.meta.env.VITE_UNISENDER_API_KEY
const listId = '2'

const unisender = axios.create({
  baseURL: 'https://api.unisender.com/ru/api/',
  headers: {
    'Access-Control-Allow-Origin': 'https://jobs.yourcodereview.com',  // Пример заголовка Content-Type
    'Access-Control-Allow-Headers': '*',
  }
})
const unisender_proxy = axios.create({
  baseURL: 'https://jobs.yourcodereview.com:8000/api/subscribe',
})

export function useUnisender() {
  const data = ref(null)
  const error = ref('')

  const sendEmail = async (email, message) => {
    await unisender
      .post('sendEmail', {
        api_key: apiKey,
        email,
        message
      })
      .then((res) => {
        data.value = res.data
      })
      .catch((err) => {
        error.value = err
      })
  }

  const subscribe = async (email) => {
    try {
      if (!email) {
        return;
      }
      const res = await unisender_proxy
        .post('/', null, {
          params:{
            api_key: apiKey,
            email: email,
          },
        })
        .then((res) => {
          data.value = res.data
        })
        .catch((err) => {
          error.value = err
        })
    } catch (err) {
      error.value = err;
    }
  }

  const getList = async () => {
    await unisender
      .get('getLists', {
        api_key: apiKey
      })
      .then((res) => {
        data.value = res.data
      })
      .catch((err) => {
        error.value = err
      })
  }

  return { sendEmail, subscribe, getList }
}

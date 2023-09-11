import axios from 'axios';
import { ref } from 'vue';

const apiKey = import.meta.env.VITE_UNISENDER_API_KEY;
const listId = '244';

const unisender = axios.create({
  baseURL: 'https://api.unisender.com/ru/api/',
});

export function useUnisender() {
  const data = ref(null)
  const error = ref('')

  const sendEmail = async (email, message) => {
    await unisender.post('sendEmail', {
        api_key: apiKey,
        email,
        message,
      }).then(res => {
        data.value = res.data
      }).catch(err => {
        error.value = err
      })
  };

  const subscribe = async (email) => {
      await unisender.post('subscribe', {
        api_key: apiKey,
        list_id: listId,
        fields: {
          EMAIL: email,
        },
      }).then(res => {
        data.value = res.data
      }).catch(err => {
        error.value = err
      });
  };

  const getList = async () => { 
      await unisender.get('getLists', {
        api_key: apiKey,
      }).then(res => {
        data.value = res.data
      }).catch(err => {
        error.value = err
      })
  };

  return { sendEmail, subscribe, getList };
}
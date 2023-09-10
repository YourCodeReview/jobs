import axios from 'axios';
import { ref } from 'vue';

const apiKey = import.meta.env.VITE_UNISENDER_API_KEY;
const listId = '244';

const unisender = axios.create({
  baseURL: 'https://api.unisender.com/ru/api/',
});

export function useUnisender() {
  const data = ref(null)
  const errorMsg = ref('')

  const sendEmail = async (email, message) => {
    await unisender.post('sendEmail', {
        api_key: apiKey,
        email,
        message,
      }).then(res => {
        data.value = res.data
      }).catch(err => {
        errorMsg.value = err
      })
  };

  const subscribe = async (email, name) => {
      await unisender.post('subscribe', {
        api_key: apiKey,
        list_id: listId,
        fields: {
          EMAIL: email,
          NAME: name,
        },
      }).then(res => {
        data.value = res.data
      }).catch(err => {
        errorMsg.value = err
      });
  };

  const getList = async () => { 
      await unisender.get('getLists', {
        api_key: apiKey,
      }).then(res => {
        data.value = res.data
      }).catch(err => {
        errorMsg.value = err
      })
  };

  return { sendEmail, subscribe, getList };
}
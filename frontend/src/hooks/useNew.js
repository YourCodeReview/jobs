// frontend.js
import axios from 'axios';

export const subscribeNew = async (email) => {
  const proxyUrl = 'https://jobs.yourcodereview.com/subscribe'; // URL вашего прокси-сервера
  const data = { email };

  try {
    console.log('himan')
    const response = await axios.post(proxyUrl, data);
    console.log('gg')
    console.log('Успешный ответ:', response.data);
    return response.data;
  } catch (error) {
    console.error('Ошибка при запросе:', error);
    throw error;
  }
};

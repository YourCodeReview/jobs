// Ваш существующий серверный код
const express = require('express');
const axios = require('axios');

const app = express();
const port = 3000;

// ... Ваши другие настройки и middleware ...

// Маршрут для проксирования запросов к Unisender
app.post('/subscribe', async (req, res) => {
  const apiUrl = 'https://api.unisender.com/ru/api/subscribe';
  const apiKey = '6w9njzto7buimo4ggpsg569t1oacs478ynoij8iy'; // Замените на ваш ключ API

  const data = {
    api_key: apiKey,
    format: 'json',
    list_ids: 2,
    double_optin: 3,
    fields: {
      email: req.query.email
    }
  };
  try {
    console.log('new')
    const response = await axios.post(apiUrl, null, { data });
    console.log('server')
    console.log('Успешный ответ:', response.data);
    res.json(response.data);
  } catch (error) {
    console.error('Ошибка при запросе:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// ... Ваши другие маршруты ...

app.listen(port, () => {
  console.log(`Сервер слушает на порту ${port}`);
});

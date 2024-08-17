import UniSender from 'unisender';

const uniSender = new UniSender({
  api_key: '6w9njzto7buimo4ggpsg569t1oacs478ynoij8iy',
  lang: 'ru' // optional, 'en' by default
});

export const subscribeLow = (email) => {
    return uniSender.subscribe({
      format: 'json',
      list_ids: 2,
      double_optin: 3,
      fields: {
        email: email
      }
    }).then(response => {
      console.log('Message id: ', JSON.stringify(response.result, null, 2));
    }).catch(response => {
      console.log('Error:' + response.error);
    });
  };

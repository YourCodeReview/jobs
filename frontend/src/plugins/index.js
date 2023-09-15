// Plugins
import vuetify from './vuetify'
import pinia from '../store'
import router from '../router'
import '../firebase/firebase'

export function registerPlugins(app) {
  app.use(vuetify).use(pinia).use(router)
}

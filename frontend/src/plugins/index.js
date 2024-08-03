// Plugins
import vuetify from './vuetify'
import pinia from '../store'
import router from '../router'
import { i18n } from './i18n'
import '../firebase/firebase'

export function registerPlugins(app) {
  app.use(vuetify).use(pinia).use(router).use(i18n)
}

import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './registerServiceWorker'
import 'swiper/dist/css/swiper.css'
import './assets/sass/bulma/params.scss'
import './assets/sass/style.scss'
import {
  library
} from '@fortawesome/fontawesome-svg-core'

import {
  fas
} from '@fortawesome/free-solid-svg-icons'

import {
  FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

Vue.component('fa-icon', FontAwesomeIcon)
library.add(fas)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

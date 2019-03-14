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
  fab
} from '@fortawesome/free-brands-svg-icons'

import {
  far
} from '@fortawesome/free-regular-svg-icons'

import {
  FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

// juste en sessous système de clé valeur  faisant ârtie partie de la librairie vue j'assigne à mon objet FontAwesomeIcon le nom d'un composant fa-icon
Vue.component('fa-icon', FontAwesomeIcon)

// ici jajoute mes differents style d'icons à ma librairy fontawesome-svg-core qui va se charger d'interpreter chacune des librairie suivante
library.add(fas)
library.add(fab)
library.add(far)
// va charger toute les librairies (un peu lourd) si je me souviens bien  tu ajouter juste le nom de l'icon à chaque fois  une fois toute les icones choisis il faudra les ajouter à la librairie au cas par ca

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

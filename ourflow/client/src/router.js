import Vue from 'vue'
import Router from 'vue-router'
import BodyApp from './views/BodyApp.vue'
import NodePage from './views/Templates/Pages/NodesPages.vue'
Vue.use(Router)
export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
    path: '/',
    component: BodyApp,
    children: [{
        path: '',
        name: 'home',
        component: NodePage,
      },
      {
        path: '/error',
        name: 'notfound',
      },
      {
        path: ':page',
        name: 'contents',
        component: NodePage,
      }
    ]
  }]
})

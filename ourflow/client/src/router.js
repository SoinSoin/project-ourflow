import Vue from 'vue'
import Router from 'vue-router'
const BodyApp = () => import('./views/BodyApp.vue')
const NodePage = () => import('./views/Templates/Pages/NodesPages.vue')

Vue.use(Router)
const router = new Router({
  mode: 'history',
  base: process.env.VUE_APP_BASE_URL,
  routes: [{
    path: '/',
    component: BodyApp,
    children: [{
        path: '',
        name: 'home',
        props: true,
        component: NodePage,
      },
      {
        path: 'not-found',
        name: 'notfound',
      },
      {
        path: ':page/',
        name: 'contents',
        props: true,
        component: NodePage,
        pathToRegexpOptions: {
          strict: true
        }
      }
    ]
  }]
})
router.beforeEach((to, from, next) => {
  var splitWord = to.path.split("")
  if (splitWord[splitWord.length - 1] !== '/') next({
    path: `${to.path}/`
  })
  else next()
})
export default router

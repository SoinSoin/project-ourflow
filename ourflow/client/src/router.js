import Vue from 'vue'
import Router from 'vue-router'
import AllUsers from './views/AllUsers.vue'
import User from './views/User.vue'
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  // je definis ici mes routes, je vais avoir une route static vide qui va charger les composant si l'utilisateur est à la base de l'url dans notre cas 0.0.0.0:8080 .
  // name : va etre le nom de ma route, je pourais plus facilement  redirigé mes composant grâce a celle-ci
  // component: va être le composant appelé lorsque je serais sur cette route.
  routes: [{
      path: '/',
      name: 'allusers',
      component: AllUsers
    },
    // ici j'ai une route variable, le parametre que je vais faire varier se voit par le : . J'ai donc ici une variable d'url :login que je peux faire varier.
    {
      path: '/user/:login',
      name: 'user',
      component: User
    }
  ]
})

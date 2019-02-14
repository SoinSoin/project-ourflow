import axios from 'axios'
// j'importe le librairie axios, cette librairie permet de racrocher les routes d'une api  tiers à notre application. Cette librairie est basé sur un appelle Ajax
// On peur donc mettre en place via cette librairie CRUD 
// voir : /services/api.js 
export default () => {
  // j'utilise une des methodes axios (.create() dans laquelle on parametre notre base URL il y'a d'autre params voir doc) qui initie la connection entre notre application vue et l'api tiers.
  return axios.create({
    //process.env.VUE_APP_BASE_API est paramétré dans le fichier .env.staging à la racine du projet vue.
      baseURL: process.env.VUE_APP_BASE_API
    })
  }

import baseURL from './index.js'
// j'importe la base de mon url configuré dans /services/index.js
// dans ce fichier nous allons créer des méthodes qui interagisse avec l'api .
// nous pouvons appliqué le classicisme CRUD 
// Create -> .post()
// Read -> .get()
//Update -> .put()
// Delete -> .delete()
// plus d'infos : https://github.com/axios/axios
// Dans notre cas nous avons juste besoin de Read les données je vais donc utiliser seulement la mèthode .get()
export default {
  // ici j'utilise async qui va signaler à mon navigateur que cette methode est asynchrone et que j'attend un resultat avec await.
  // Les methodes asynchrones fontionne sur un système de promesse.
  // Une promesse est une fonction qui s'execute avec un resultat attendu qui peut être disponible maintenant, dans le futur voire jamais. (doc mozilla)
  // Pour que la promesse retourne un resultat il faut d'abord que celle-ci soit résolue.
  
// Je vais te donner un exemple imagé vu que c'est assez méta:
// Je suis sur le marché je vois un vendeur de pomme une pomme c'est 0,40e.
// j'ai 0,40e et j'ai envie d'une pomme.
//  je vais voir le vendeur je lui demande une pomme je lui donne mes sous, ma promesse c'est je vais avoir une pomme.
// J'attend, le vendeur regarde si le compte y est ... Le compte est bon
// Le vendeur me donne la pomme, la promesse entre le vendeur et moi est résolue. Maintenant je fais ce que je veux de ma pomme. 

//Maintenant même schema mais j'ai que 0,30e.
//  je vais voir le vendeur je lui demande une pomme je lui donne mes sous, ma promesse c'est je vais avoir une pomme.
// J'attend, le vendeur regarde si le compte y est ... Le compte n'est pas bon.
// Le vendeur me rend ma monnaie et me dit vous n'avez pas assez c'est pas ce que j'attendais.
// la promess n'est pas résolue elle est en erreur.

  // Dans mon cas je lui dit j'ai la méthode getAllUsers() est asynchrone et qu'elle attend un résultat qui va être le json de l'api.
  // voir: /views/AllUsers.vue
  async getAllUsers() {
    return await baseURL().get('/users')
  },
  // je fais passer  un argument login pour ciblé l'appelle d'un utilisateur
  // voir: /views/User.vue
  async getUser(login) {
    return await baseURL().get(`/users/${login}`)
  },
}

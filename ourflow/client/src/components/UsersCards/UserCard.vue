<template>
  <!-- la balise router-link est une balise spécifique au module vue router et permet d'interagir avec les routes que l'on a créer dans le fichier router.js-->
  <!-- Dans le cas présent j'utilise cette balise afin que quand je clique dessus elle me redirige vers la route que j'ai ciblé qui elle appelle un composant-->
  <!-- dans la balise router-link on peut voir :to ça va etrl'objet à l'interieur va être compilé en lien -->
  <!-- je dit dans cette attibut pour la route qui s'appelle user tu passe au parametre du nom de login la valeur attributeStorageApi.login -->
  <!--  lien utile: https://router.vuejs.org/guide/essentials/named-routes.html -->
  <!--  attributeStorageApi est un props voir plus bas pour le props -->
  <!-- j'utilise les class de bulma -->
  <router-link class="box" :to="{ name: 'user', params: { login: attributeStorageApi.login }}">
    <div class="columns">
      <div class="column is-3">
        <figure class="image is-64x64">
          <img class="is-rounded" :src="attributeStorageApi.avatar_url" alt="Image">
        </figure>
      </div>
      <div class="column is-9">
        <div class="columns">
          <div class="column is-12">
              <h3 class="title is-3">{{attributeStorageApi.login}}</h3>
          </div>
        </div>
        <div class="columns is-mobile">
          <div class="column is-12">
            <h5 class="subtitle is-5">{{attributeStorageApi.id}}</h5>
          </div>
        </div>
      </div>
    </div>
  </router-link>
</template>
<script>
export default {
  name: "usercard",
//   ici je définis une props, une props va être un attribut un peu special.
// grâce au props on peut apporter des modification entre un composant parent et composant enfant (enfant qui est contenue dans le parent)
// dans ce cas la je definis la valeur de ma props dans l'element parent /views/AllUsers.
// à chaque boucle je vais avoir la valeur d'une props ce definit 
  props: {
    attributeStorageApi: {}
  }
};
</script>

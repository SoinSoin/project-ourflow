<template>
  <div class="container">
    {{myattr}}
    <!-- j'utilise le système de columns de bulma et je lui dit avec la classus-multiline que j'aurais plusieurs ligne-->
    <div class="columns is-multiline">
        <!-- pour éviter d'avoir une page blanche et montrer que quelque chose charge je fait une condition avec le v-if-->
        <!-- je dit si mon tableau est vide (different de la taille du beforeMount) tu me retourne loading-->
        <div class="column is-12" v-if="!storageAllUsers.length">
            <strong>loading api github ...</strong>
        </div>
        <!--  si il est plein tu parcours mon tableau avec v-for-->
        <!-- liens utile: -->
        <!-- https://fr.vuejs.org/v2/guide/conditional.html -->
        <!-- https://fr.vuejs.org/v2/guide/list.html -->
        <!-- note les : devant les attributs signifie que je vais passer uen variable -->
        <!-- :key  permet à vue js de savoir que les composants qui se boucle sont unique (avec les api on utilise souvent les id) -->
      <div v-else class="column is-4" v-for="user in storageAllUsers" :key="user.id">
          <!-- ici j'ai du javascript and xml (comme pour les attributs des v-for et v-if) -->
          <!-- cela me permet d'appeler un composant personnaliser dans mon cas user card (/components/UsersCards/UserCard.vue) -->
          <!-- je passe un valeur user à l'attribut  attributeStorageApi qui est une props de mon composant UserCard-->
          <!-- mon composant va etre bouclé autant de fois qu'il y a de valeur dans mon tableau -->
        <UserCard :attributeStorageApi="user"/>
      </div>
    </div>
  </div>
</template>

<script>
// j'importe mon objet api et ces methodes voir /services/api.js & index.js
import Api from "@/services/api.js";
import UserCard from "@/components/UsersCards/UserCard.vue";

// export default sont les propriétés que je vais exporter et qui peuvent être accessible si je l'importe.
export default {
  name: "allusers",
  // components va indiquer à mon composant quels composant enfant vont intervenir en sont sein
  components: {
    UserCard
  },
  // la méthode data va retourner les attributs propre à mon composant accessible uniquement dans ce composant.
  // Pour y accéder je peux utiliser this.myattr dans l'objet export default ou dans mon template en faisant {{myattr}}
  data() {
    return {
      myattr: "je suis un attribut de ce composant",
      storageAllUsers: []
    };
  },
  beforeCreate() {
    console.log("attend on initie mes events ainsi que mon cycle de vie");
  },
  created() {
    console.log(
      "tout c'est bien passé à l'etape précedente je vais pouvoir initié les injections et ma réactivité"
    );
  },
  beforeMount() {
    console.log(
      "bon bah tout ce passe bien, attend je vais pouvoir créer le rendu de mon composant avec ces attributs et ces methodes"
    );
    console.log(this.myattr);
    this.callAllUsers();
  },
  mounted() {
    console.log(
      "Nickel je m'affiche comme je le voulais dans le navigateur, je suis parée pour les evenements utilisateur"
    );
  },

  methods: {
    callAllUsers() {
        // then permet de reourner un callback dans le cas d'une resolution (réponse) voir services/api.js
      Api.getAllUsers().then(res => {
        console.log(res);
        // res va être la reponse que me renvoie la libraire axios
        this.storageAllUsers = res.data;
        console.log("res.data -> ", res.data);
        console.log("this.storageAllUsers -> ", this.storageAllUsers);
        // je veux que ma réponse donne une valeur global à mon attribut storageAllUser pour pouvoir ensuite l'utiliser en global dans mon composant voir <template></template>
      });
    }
  }
};
</script>

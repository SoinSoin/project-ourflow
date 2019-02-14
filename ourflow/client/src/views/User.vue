<template>
  <div class="container">
    <!-- <p>{{$route.params.login}}</p> -->
    <div class="columns">
      <div class="column is-4"></div>
      <div class="column is-4">
        <strong v-if="!storageUser.length">loading api github ...</strong>
        <!-- voir /components/InfoUsers/infoUser.vue -->
        <InfoUser v-else :dataToComponent="storageUser[0]"/>
      </div>
      <div class="column is-4"></div>
    </div>
  </div>
</template>

<script>
import InfoUser from "@/components/InfoUsers/InfoUser.vue";
import Api from "@/services/api.js";
export default {
  name: "user",
  components: {
    InfoUser
  },
  data() {
    return {
      storageUser: []
    };
  },
  beforeMount() {
    this.getUser();
  },
  methods: {
    getUser() {
        // console.log(this.$route.params.login) 
        // this.$route.params.login me permet de recuperer la valeur de ma variable route (voire router.js) et de faire passer en parametre de ma methode getUser() le nom de la personne (voir: /services/api.js)
      Api.getUser(this.$route.params.login).then(res => {
        this.storageUser = [res.data];
        console.log(res.data)
        // je met this.storageUser dans un tableau même si ce n'est pas nécessaire pour pouvoir retourner le  loading lors du chargement
      });
    }
  }
};
</script>
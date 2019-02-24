<template>
  <section id="main-pages">
    <Home v-if="$route.name==='home'"/>
    <Prestation v-if="$route.params.page==='prestation'"/>
    <Contact v-if="$route.params.page==='contact'"/>
    <Portfolio v-if="$route.params.page==='portfolio'"/>
  </section>
</template>
<script>
import Contact from "./Page/Contact.vue";
import Home from "./Page/Home.vue";
import Prestation from "./Page/Prestation.vue";
import Portfolio from "./Page/Portfolio.vue";
export default {
  name: "NodePage",
  components: {
    Contact,
    Home,
    Prestation,
    Portfolio
  },
  beforeMount() {
    this.setMetaTitle();
  },
  beforeUpdate() {
    this.setMetaTitle();
  },
  methods: {
    setMetaTitle() {
      if (this.$route.params.page !== undefined)
        var title = `: ${this.$route.params.page}`;
      else var title = "";
      document.title = `OurFlow${title}`;
    }
  }
  //note faire un appelle d'api ici pour tout le reste
};
</script>

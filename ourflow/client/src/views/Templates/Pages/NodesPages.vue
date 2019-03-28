<template>
  <section id="main-pages">
    <Home v-if="$route.name==='home'"/>
    <Prestation v-if="$route.params.page===$store.getters.getData[1].title_page.toLowerCase()"/>
    <Portfolio v-if="$route.params.page===$store.getters.getData[2].title_page.toLowerCase()"/>
    <Contact v-if="$route.params.page===$store.getters.getData[3].title_page.toLowerCase()"/>
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

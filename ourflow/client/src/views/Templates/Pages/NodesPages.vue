<template>
  <div id="main-pages" class="has-background-white" >
    <Home v-if="$route.name==='home'" :fetchData="$store.getters.getData[$store.getters.getIndex]"/>
    <Prestation v-if="$route.params.page===$store.getters.getData[1].title_page.toLowerCase() " :fetchData="$store.getters.getData[$store.getters.getIndex]"/>
    <Portfolio
      v-if="$route.params.page===$store.getters.getData[2].title_page.toLowerCase()"
      :fetchData="$store.getters.getData[$store.getters.getIndex]"
    />
    <Contact
      v-if="$route.params.page===$store.getters.getData[3].title_page.toLowerCase()"
      :fetchData="$store.getters.getData[$store.getters.getIndex]"
    />
  </div>
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
  data() {
    return {
      isLoading: true
    };
  },
  computed: {
    getDataFetch() {
      return this.$store.getters.getData; 
    },
    getTitleChange() {
      return this.$store.getters.getIndex;
    }
  },
  watch: {
    getTitleChange(index) {
      this.changeMetaTitle();
    }
  },
  beforeMount() {
    this.changeMetaTitle();
  },

  methods: {
    changeMetaTitle() {
      document.title = `OurFlow: ${
        this.$store.getters.getPage[this.$store.getters.getIndex]
      }`;
    }
  }
};
</script>
<style lang="scss">
#main-pages {
  position: relative;
  top:100vh;
  margin-top: 5vh;
  box-shadow: 0 -5px 10px -5px rgba(0, 0, 0, 0.3);
  border-radius: 25px 25px 0 0;
  overflow: hidden;
}
</style>

<template>
  <div id="main-pages" class="has-background-white">
    <component
      :is="componentData[$store.getters.getIndex]"
      :fetchData="$store.getters.getData[$store.getters.getIndex]"
    ></component>
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
      awaiting: true,
      componentNames: [
        { name: "Home", order: 1 },
        { name: "Prestation", order: 2 },
        { name: "Portfolio", order: 3 },
        { name: "Contact", order: 4 }
      ],
      componentData: []
    };
  },
  watch: {
    $route(to, from) {
      this.setIndexUrl(to);
      this.setMetaTitle();
    }
  },
  beforeMount() {
    this.setIndexUrl(this.$route);
    this.setMetaTitle();
    this.addComponentData();
  },
  methods: {
    setMetaTitle() {
      document.title = `OurFlow | ${
        this.$store.getters.getPage[this.$store.getters.getIndex]
      }`;
    },
    setIndexTitle(obj) {
      const index = obj.params.index;
      this.$store.commit("setIndex", index);
    },
    setIndexUrl(selfRoute) {
      if (!isNaN(selfRoute.params.index)) this.setIndexTitle(selfRoute);
      else {
        this.$store.getters.getUrl.map((val, index) => {
          if (val.path === selfRoute.path) {
            this.$store.commit("setIndex", val.url.params.index);
          }
        });
      }
    },
    addComponentData() {
      this.$store.getters.getData.map((val, index) => {
        this.componentNames.map(valbis => {
          if (val.order_page === valbis.order) {
            this.componentData.push(valbis.name);
          }
        });
      });
    }
  }
};
</script>
<style lang="scss">
#main-pages {
  position: relative;
  top: 100vh;
  margin-top: 5vh;
  box-shadow: 0 -5px 10px -5px rgba(0, 0, 0, 0.3);
  border-radius: 25px 25px 0 0;
  overflow: hidden;
}
</style>

<template>
  <div id="main-pages" class="has-background-white">
    <Home v-if="$route.name==='home'" :fetchData="$store.getters.getData[$store.getters.getIndex]"/>
    <div v-for="(component, index) in componentData" :key="index">
      <component
        v-if="$route.params.page===component.page "
        :is="component.component"
        :fetchData="$store.getters.getData[$store.getters.getIndex]"
      ></component>
    </div>
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
      componentNames: [
        { name: "Prestation", order: 2 },
        { name: "Portfolio", order: 3 },
        { name: "Contact", order: 4 }
      ],
      componentData: []
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
    this.addComponentData();
  },

  methods: {
    addComponentData() {
      var obj = Object;
      this.$store.getters.getData.map((val, index) => {
        this.componentNames.map(valbis => {
          if (val.order_page === valbis.order) {
            obj.page = val.title_page.toLowerCase();
            obj.component = valbis.name;
            this.componentData.push(obj);
            obj = {};
          }
        });
      });
    },
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
  top: 100vh;
  margin-top: 5vh;
  box-shadow: 0 -5px 10px -5px rgba(0, 0, 0, 0.3);
  border-radius: 25px 25px 0 0;
  overflow: hidden;
}
</style>

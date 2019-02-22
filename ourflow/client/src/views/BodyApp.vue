<template>
  <div id="body-app">
    <header class="level is-mobile">
      <div class="level-left">ourflow</div>
      <div class="level-right">
        <Nav :itemsNav="dataNamePages" @clicked="onClickGetIndex"/>
      </div>
    </header>
    <Skeleton :indexPage="indexOfPage" v-if="$route.name!=='notfound'"/>
    <NotFound v-else/>
    <Footer/>
  </div>
</template>
<script>
import Skeleton from "./Templates/Skeleton.vue";
import NotFound from "./Templates/NotFound.vue";
import Nav from "@/components/Navs/Nav.vue";
import Footer from "@/components/Footers/Footer.vue";
export default {
  name: "BodyApp",
  components: {
    Skeleton,
    NotFound,
    Footer,
    Nav
  },
  data() {
    return {
      dataNamePages: [],
      indexOfPage: null
    };
  },
  beforeMount() {
    this.fetchNamePage();
  },
  methods: {
    fetchNamePage() {
      var objData = [
        { name: "Accueil", linkto: "home" },
        { name: "Prestation", linkto: "prestation" },
        { name: "Contact", linkto: "contact" }
      ];
      this.dataNamePages = objData;
    },
    onClickGetIndex(value) {
      this.indexOfPage = value;
    }
  }
};
</script>

<style lang="scss">
</style>


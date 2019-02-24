<template>
  <div id="body-app">
    <header class="level is-mobile">
      <div class="level-left">ourflow</div>
      <div class="level-right">
        <Nav :itemsNav="dataNamePages" @returnNavToBody="passIndexBodyToSkeleton"/>
      </div>
    </header>
    <Skeleton
      @returnSkeltonToBody="indexFromSlide"
      :indexToSkeleton="indexFromNav"
      v-if="$route.name!=='notfound'"
    />
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
      indexFromNav: null
    };
  },
  beforeMount() {
    this.fetchNamePage();
  },
  watch: {
    indexFromNav(index) {
      this.indexFromNav = index;
    }
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
    passIndexBodyToSkeleton(navIndex) {
      this.indexFromNav = navIndex;
    },
    indexFromSlide(slideIndex) {
      this.indexFromNav = slideIndex;
    }
  }
};
</script>

<style lang="scss">
</style>


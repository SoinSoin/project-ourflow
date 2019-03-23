<template>
  <div id="body-app">
    <div v-if="dataNamePages.length" id="main-body" class="container is-fluid is-marginless">
      <header class="level is-mobile is-marginless">
        <div class="level-left">
          <div class="level-item">ourflow</div>
        </div>
        <div class="level-right">
          <Nav :itemsNav="dataNamePages" @returnNavToBody="passIndexBodyToSkeleton"/>
        </div>
      </header>
      <Skeleton
        @returnSkeltonToBody="indexFromSlide"
        :indexToSkeleton="indexFromNav"
        :dataToSkeleton="dataNamePages"
        v-if="$route.name!=='notfound'"
      />
      <NotFound v-else/>
      <Footer/>
    </div>
    <div v-else id="main-body" class="container is-fluid is-marginless">
      <p>await ...</p>
    </div>
  </div>
</template>
<script>
import Skeleton from "./Templates/Skeleton.vue";
import NotFound from "./Templates/NotFound.vue";
import Nav from "@/components/Navs/Nav.vue";
import Footer from "@/components/Footers/Footer.vue";
import getApi from "@/services/api.js";
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
      getApi.getAllPage().then(res => (this.dataNamePages = res.data));
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


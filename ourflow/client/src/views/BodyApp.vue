<template>
  <div id="body-app">
    <div v-if="!isLoading" id="main-body" class="container is-fluid is-marginless">
      <!-- header -->
      <header class="level is-mobile is-marginless level-header">
        <div class="level-left level-header-left">
          <BrandNav/>
        </div>
        <div class="level-right level-header-right">
          <transition name="slide">
            <BurgerNav v-if="$store.getters.getSize<1024" @BurgerIsActive="ContainerIsActive"/>
            <Nav v-else/>
          </transition>
        </div>
      </header>
      <!-- end header -->
      <!-- nav responsive -->
      <transition name="slide">
        <ContainerNav v-if="containerIsActive"/>
      </transition>
      <!-- end nav responsive -->
      <!-- template -->
      <Skeleton v-if="$route.name!=='notfound'"/>
      <!-- end template -->
      <NotFound v-else/>
      <Footer/>
    </div>
    <div v-else id="main-body">
      <Loader/>
    </div>
  </div>
</template>
<script>
import Skeleton from "./Templates/Skeleton.vue";
import NotFound from "./Templates/NotFound.vue";
import Nav from "@/components/Navs/Nav.vue";
import BurgerNav from "@/components/Navs/ResponsivesNavs/BurgerNav.vue";
import BrandNav from "@/components/Navs/BrandsNavs.vue";
import ContainerNav from "@/components/Navs/ResponsivesNavs/ContainerNav.vue";
import Footer from "@/components/Footers/Footer.vue";
import Loader from "@/components/Loaders/Loader.vue";
import getApi from "@/services/api.js";
export default {
  name: "BodyApp",
  components: {
    Skeleton,
    NotFound,
    Footer,
    BurgerNav,
    ContainerNav,
    Nav,
    BrandNav,
    Loader
  },
  data() {
    return {
      containerIsActive: false,
      isResponsive: Boolean,
      targetSize: Number,
      isLoading: true,
      isLocate: false
    };
  },
  computed: {
    sizeChange() {
      return this.$store.getters.getSize;
    },
    indexChange() {
      return this.$store.getters.getIndex;
    }
  },
  watch: {
    containerIsActive(bool) {
      document.documentElement.classList.toggle("is-clipped");
    },
    indexChange() {
      this.containerIsActive = false;
    },
    sizeChange(size) {
      this.TargetResponsive(size);
    }
  },

  beforeMount() {
    this.fetchingData();
  },
  mounted() {
    this.$store.commit("updateSizeScreen", window.innerWidth);
    this.EventResize();
  },
  methods: {
    EventResize() {
      window.onresize = () => {
        this.$store.commit("updateSizeScreen", window.innerWidth);
      };
    },
    TargetResponsive(width) {
      if (width > 1024) this.containerIsActive = false;
    },
    ContainerIsActive(ContainerIsActive) {
      this.containerIsActive = ContainerIsActive;
    },
    fetchingData() {
      getApi.getAllPage().then(res => {
        this.isLoading = false;
        this.$store.commit("updatefetchData", res.data);
        if (res.status === 200) this.isLocate = true;
      });
    }
  }
};
</script>

<style lang="scss">
.slide-leave-active {
  -webkit-animation-name: slideOutRight;
  animation-name: slideOutRight;
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@-webkit-keyframes slideOutRight {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
  100% {
    visibility: hidden;
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
  }
}
@keyframes slideOutRight {
  0% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
  100% {
    visibility: hidden;
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
  }
}

.slide-enter-active {
  -webkit-animation-name: slideInRight;
  animation-name: slideInRight;
  -webkit-animation-duration: 0.5s;
  animation-duration: 0.5s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@-webkit-keyframes slideInRight {
  0% {
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
    visibility: visible;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
}
@keyframes slideInRight {
  0% {
    -webkit-transform: translateX(100%);
    transform: translateX(100%);
    visibility: visible;
  }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
}
.level-header {
  position: absolute;
  top: 0;
  .level-header-right {
    z-index: 30;
  }
  .level-header-left {
    z-index: 1;
  }
}
</style>
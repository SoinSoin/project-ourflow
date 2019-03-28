<template>
  <div id="body-app">
    <div v-if="dataNamePages.length" id="main-body" class="container is-fluid is-marginless">
      <header class="level is-mobile is-marginless level-header">
        <div class="level-left level-header-left">
          <div class="level-item">ourflow</div>
        </div>
        <div class="level-right level-header-right">
          <transition name="slide">
            <Nav v-if="!isResponsive" :itemsNav="dataNamePages"/>
            <BurgerNav v-else @BurgerIsActive="ContainerIsActive"/>
          </transition>
        </div>
      </header>
      <transition name="slide">
        <ContainerNav v-if="containerIsActive" :itemsNav="dataNamePages"/>
      </transition>
      <Skeleton :dataToSkeleton="dataNamePages" v-if="$route.name!=='notfound'"/>
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
import BurgerNav from "@/components/Navs/ResponsivesNavs/BurgerNav.vue";
import ContainerNav from "@/components/Navs/ResponsivesNavs/ContainerNav.vue";
import Footer from "@/components/Footers/Footer.vue";
import getApi from "@/services/api.js";
export default {
  name: "BodyApp",
  components: {
    Skeleton,
    NotFound,
    Footer,
    BurgerNav,
    ContainerNav,
    Nav
  },
  data() {
    return {
      dataNamePages: [],
      containerIsActive: false,
      isResponsive: Boolean
    };
  },
  watch: {
    containerIsActive(bool) {
      if (bool) document.documentElement.style.overflow = "hidden";
      else document.documentElement.style = "";
    }
  },
  beforeMount() {
    this.fetchNamePage();
  },
  mounted() {
    this.TargetResponsive(window.innerWidth);
    this.EventResize();
  },
  methods: {
    EventResize() {
      window.onresize = () => {
        this.TargetResponsive(window.innerWidth);
      };
    },
    TargetResponsive(width) {
      if (width < 1024) this.isResponsive = true;
      else {
        this.isResponsive = false;
        this.containerIsActive = false;
      }
    },
    ContainerIsActive(ContainerIsActive) {
      this.containerIsActive = ContainerIsActive;
    },
    fetchNamePage() {
      getApi.getAllPage().then(res => (this.dataNamePages = res.data));
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
    z-index: 10;
  }
}
</style>